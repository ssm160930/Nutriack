import pandas as pd
import urllib.request

url = 'https://docs.google.com/spreadsheets/d/1LIg_wkURgOc-ZQxICjY_XUhDrxnpn2etR8bY73lMzL0/gviz/tq?tqx=out:csv&sheet=Sheet2'
urllib.request.urlretrieve(url, 'data.csv')
