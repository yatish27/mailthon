#!/usr/bin/env python
# encoding: utf-8

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Client(object):

    def __init__(self, usr, psw, from_address):
        self.username = usr
        self.password = psw
        self.from_address = from_address
        self.server = self.get_server()

    def get_server(self):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        return(server)

    def header_msg(self):
        msg = MIMEMultipart()
        msg['From'] = self.from_address
        msg['To'] = self.to_addr
        msg['Subject'] = self.subject
        return(msg)

    def deliver(self, subject, to_addr, body):
        self.to_addr = to_addr
        self.subject = subject

        msg = self.header_msg()

        msg.attach(MIMEText(body, 'plain'))
        self.server.sendmail(self.from_address, self.to_addr, msg.as_string())
        self.server.close()

    def quit(self):
        self.server.close()

if __name__ == '__main__':

    # Fill these in with the appropriate info...
    usr = 'usr@example.com'
    psw = 'password'
    fromaddr = 'test'
    toaddr = "test2"

    # Send notification email
    client = Client(usr, psw, fromaddr)
    client.deliver("Mailthon: Testing", toaddr, "This is test body sent to you")
