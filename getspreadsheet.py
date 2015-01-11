'''
Created on Jan 11, 2015

@author: Kaustubh
'''

import gspread
import base64
import smtplib
import email
from email.MIMEText import MIMEText

def constructmsg(name):
    msgtext = "Hi " + name + ",\n"
    msgtext = msgtext + "test msg\n"
    return msgtext

def get_spreadsheet(conndetails=None,filename=None):    
    gc = gspread.login(conndetails["username"],conndetails["password"])
    wks = gc.open(filename).sheet1
    return wks.get_all_values()

def sendmailfunc(conndetails=None,toaddr,sub):
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    server.login(conndetails["username"],conndetails["password"])    
    for i in range(len(toaddr)):
        msg = email.MIMEMultipart.MIMEMultipart()
        msg['From'] = conndetails["username"]
        msg['To'] = "".join(toaddr[i])
        msg['Subject'] = sub
        msgtext = constructmsg(Namelist[i])
        msg.attach(MIMEText(msgtext,'plain'))
        msg.attach(MIMEText('\nsent via python', 'plain'))
        server.sendmail(msg['From'],msg['To'],msg.as_string())

    server.close()

conndetails={}
conndetails["username"] = "username@gmail.com"
conndetails["password"] = "password"
filename = "Maillist"
mailingdata = get_spreadsheet(conndetails, filename)
##Spreadsheet contain Name in first column and mail address in last column
tolist = [item[-1] for item in mailingdata]
Namelist = [item[0] for item in mailingdata]
sub = "testing mail through python"

    