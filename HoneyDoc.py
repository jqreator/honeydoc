#!/usr/bin/env python
#Honey Document Generator v1.0.1
#Copyright (C)2015 Jacob Parks - jqreator at gmail dot com
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#Release notes:
#v1.0.0 - Initial release
#v1.0.1 - Made beacon an option instead of the default and removed unused options
#v1.0.2 - Updated img tag to use better form

import argparse
import random
import sys

#Set default document values
docTitle = "Employee Information" #Title of document
numRec = 10 #Number of records to create
imgURL = "http://127.0.0.1/hello.png" #URL of tracking image
fileExt = "doc" #Default file extension

#Declare variables
n = 0
tRow = ""

#Import name list
with open("names.txt") as nameDoc:
    nameList = nameDoc.read().splitlines()
listLen = len(nameList)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--title", help="Specify a custom document title. Default is " + docTitle)
parser.add_argument("-c", "--count", help="Number of fake records to create. Default is " + str(numRec))
parser.add_argument("-b", "--beacon", help="Include a beacon image. Default is " + imgURL, action="store_true")
parser.add_argument("-u", "--url", help="Set a custom URL for the beacon image.")
parser.add_argument("-e", "--ext", help="File extension. Default is " + fileExt)
args = parser.parse_args()
if args.title:
    docTitle = args.title
if args.count:
    numRec = int(args.count)
if args.url:
    imgURL = args.url
if args.ext:
    fileExt = args.ext

#Generate a random fake SSN
def getSSN():
    num1 = random.randint(100,999)
    num2 = random.randint(10,99)
    num3 = random.randint(1000,9999)
    return str(num1) + "-" + str(num2) + "-" + str(num3)

#Generate a random name
def getName():
    fNameNum = random.randint(0,listLen - 1)
    lNameNum = random.randint(0,listLen - 1)
    return nameList[fNameNum] + " " + nameList[lNameNum]

#Create table rows
while n < numRec:
    ss = getSSN()
    name = getName()
    tRow = tRow + "<tr><td width=200>" + name + "</td><td>" + ss + "</td></tr>"
    n = n + 1

html1 = """
        <html>
	<body>
	<p><font size="6"><b><c>
	"""

html2 = """
        </c></b></font></p>
	<table style="width:100%">
	<tr>
	<th align="left">Name</th>
	<th align="left">Social Security</th>
        """

imgTag = '<img src="' + imgURL + '" width="1" height="1" border="0"/></table>'

html3 = """
	</body>
	</html>
	"""

#Build file contents with beacon included
if args.beacon == True:
    toWrite = html1 + docTitle + html2 + tRow + imgTag + html3
else:
    toWrite = html1 + docTitle + html2 + tRow + html3
	
#Write the file
f = open("honeydoc." + fileExt,"w")
f.write(toWrite)
f.close()
