import numpy
import random
import pandas as pd
import datetime

k = datetime.date.today()

db = pd.read_csv('example.csv')
#print(db)

#Creates the Array
numbers = list(map(int, input("Enter the Order ID's Seperated by Spaces: ").split()))
#print (numbers)

#Set the integer for the loop used for string generation
length = len(numbers)
i = 0

#Create blank string
string = ""
string += "NUTRIACK" + ","
string += "%s" % k + ","


buffer_var = ""

while i <= length - 1:
    buffer_var = int(numbers[i])
    string +=  str(db.loc[buffer_var,'Name']) + ","
    string +=  str(db.loc[buffer_var,'Calories']) + ","
    string +=  str(db.loc[buffer_var,'Calories, Fat']) + ","
    string +=  str(db.loc[buffer_var,'Total Fat (g)']) + ","
    string +=  str(db.loc[buffer_var,'Sat Fat (g)']) + ","
    string +=  str(db.loc[buffer_var,'Trans Fat (g)']) + "/"
    #string +=  str(db.loc[buffer_var,'Chol (mg)']) + ","
    #string +=  str(db.loc[buffer_var,'Sodium (mg)']) + ","
    #string +=  str(db.loc[buffer_var,'Carbs (g)']) + ","
    #string +=  str(db.loc[buffer_var,'Fiber (g)']) + ","
    #string +=  str(db.loc[buffer_var,'Sugar (g)']) + ","
    #string +=  str(db.loc[buffer_var,'Protien (g)']) + ","
    i = i + 1

string += "eos"
print (string)

from qrcode import *
from PIL import Image
qr = QRCode(version=3)
qr.add_data(string)
qr.make() # Generate the QRCode itself

# im contains a PIL.Image.Image object
im = qr.make_image()

q = random.randint(0,100)

im.save("%s.png" % (q))
