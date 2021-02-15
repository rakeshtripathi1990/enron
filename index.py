# This Python 3 environment comes with many helpful analytics libraries installed

import numpy as np # linear algebra
import pandas as pd # data processing from the given csv file
import re

from subprocess import check_output
print(check_output(["ls", "../enron"]).decode("utf8")) #All the files are kept in enron directory
#This will print the file name

myCsvEmails = pd.read_csv("../enron/emails.csv") #Where emails.csv is downloaded from the given url : https://www.kaggle.com/wcukierski/enron-email-dataset
print(type(myCsvEmails))

#To get the length of the emails
len(myCsvEmails)

myCsvEmails.head()

myCsvEmails['message'][10]
#It will return Message-ID: <15464986.1075855378456.JavaMail.evans@thyme> Date: Fri, 4 May 2001 13:51:00

fromMailer = re.compile(r'From:\s(\w)+(\.)?(\w)*@(\w)+.com')
toMailer = re.compile(r'To:\s(\w)+(\.)?(\w)*@(\w)+.com')
mailFrom = fromMailer.search(myCsvEmails['message'][1])
mailEnm = toMailer.search(myCsvEmails['message'][1])
if mailFrom:
    print(mailFrom.group())
if mailEnm:
    print(mailEnm.group())


fromSet = set()
for i in range(len(myCsvEmails)):
    totmf = fromMailer.search(myCsvEmails['message'][i])
    if totmf:
        if totmf.group() not in fromSet:
            fromSet.add(totmf.group())
toSet = set()
for i in range(len(myCsvEmails)):
    totme = toMailer.search(myCsvEmails['message'][i])
    if totme:
        if totme.group() not in toSet:
            toSet.add(totme.group())

print("From emails:", len(fromSet))
print("To emails:", len(toSet))            