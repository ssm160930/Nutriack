$html_link  = "https://docs.google.com/spreadsheets/d/XXXXXXXXXX/pubhtml";
$local_html = "sheets.html";

$file_contents = file_get_contents($html_link);
file_put_contents($local_html,$file_contents);

$dom        = new DOMDocument();
$html       = @$dom->loadHTMLFile($local_html);  //Added a @ to hide warnings - you might remove this when testing
$dom->preserveWhiteSpace = false;


$tables     = $dom->getElementsByTagName('table');
$rows       = $tables->item(0)->getElementsByTagName('tr');
$cols       = $rows->item(0)->getElementsByTagName('td');  //You'll need to edit the (0) to reflect the row that your headers are in.

$row_headers = array();
foreach ($cols as $i => $node) {
    if($i > 0 ) $row_headers[] = $node->textContent;
}

foreach ($rows as $i => $row){
    if($i == 0 ) continue;
    $cols = $row->getElementsByTagName('td');
    $row = array();
    foreach ($cols as $j => $node) {
        $row[$row_headers[$j]] = $node->textContent;
    }
    $table[] = $row;
}

//Convert to csv
$csv = "";
foreach($table as $row_index => $row_details){
    $comma      = false;
    foreach($row_details as $value){
        $value_quotes = str_replace('"', '""', $value);
        $csv .= ($comma ? "," : "") . ( strpos($value,",")===false ? $value_quotes : '"'.$value_quotes.'"'  );
        $comma = true;
    }
    $csv .= "\r\n";
}

//Save to a file and/or output
file_put_contents("result.csv",$csv);
print $csv;
