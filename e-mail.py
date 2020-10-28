#!/usr/bin/python3

#Sending e-mail Using SMTP
#Python provides smtplib module which defines an SMTP client session object that can be used to send e-mail to any machine with an SMTP or ESMTP listener daemon.
"""
smtpObj = smtplib.SMTP([host], [port], [localhostname])

Where:
host - The hostname or IP address of the machine running the SMTP server.
port - If you are providing a hostname, a port is required (usually port 25)
localhostname - If the SMTP server is running on the localmachine, just specify "localhost" for this option.
"""

#The sendmail() Method
#Typically used to send the actual message.

#Sending a Plain Text e-mail
import smtplib

sender = 'sender@fromdomain.com'
receiver = ['receiver@todomain.com']

message = """From: Sender Person <sender@fromdomain.com>
To: Receiver Person <receiver@todomain.com>
Subject: STMP e-mail from Python

This is an e-mail message that was generated and sent using Python!
"""

try:
    smtpObj = smtplib.SMTP('loclahost')
    smtpObj.sendmail(sender, receiver, message)
    print("e-mail successfully sent!")
except:
    print("Error while sending e-mail.")
finally:
    print("\n" + message)

#Sending an HTML e-mail
import smtplib

sender = 'sender@fromdomain.com'
receiver = ['receiver@todomain.com']

message = """From: Sender Person <sender@fromdomain.com>
To: Receiver Person <receiver@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: STMP e-mail from Python in HTML

This is an e-mail message in <b>HTML format</b> that was generated and sent using Python!
"""

try:
    smtpObj = smtplib.SMTP('loclahost')
    smtpObj.sendmail(sender, receiver, message)
    print("e-mail successfully sent!")
except:
    print("Error while sending e-mail.")
finally:
    print("\n" + message)    

#Sending an e-mail with Attachments
"""
Sending an e-mail with mixed content requires the setting of Content-type header to be multipart/mixed.
Then, text and attachment sections can be specified with boundaries.
 - A boundary is started with two hyphens followed by a unique number which cannot appear in the message part of the e-mail.
 - A final boundary denoting the e-mail's final section must also end with two hyphens.
Attached files should be encoded with the pack("m") function to have base64 encoding before transmission.
"""    
import smtplib
import base64

filetosend = "/mnt/c/Users/dgrewal/Documents/Projects/_git/Learning-Python/demofile.txt"

fo = open(filetosend, "rb")     #open and read the file in binary for base64 encoding
fcontent = fo.read()
encodedcontent = base64.b64encode(fcontent)

sender = 'sender@fromdomain.com'
receiver = ['receiver@todomain.com']

marker = "[  SOME UNIQUE MARKER  ]"

body = """
This is an e-mail from Python with an attachment.
"""

#Define the main headers.
part1 = """From: Sender Person <sender@fromdomain.com>
To: Receiver Person <receiver@todomain.com>
Subject: STMP e-mail from Python with Attachment
MIME-Version: 1.0
Content-type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

#Define the ,essage actopm
part2 = """Content-type: text/plain
Content-transfer-encoding:8bit

%s
--%s
""" % (marker, marker)

#Define the attachment section.
part3 = """Content-type: multipart/mixed; name=\%s\"
Content-transfer-encoding:base64
Content-disposition: attachment; filename=%s

%s
--%s--
""" % (filetosend, filetosend, encodedcontent, marker)

message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP('loclahost')
    smtpObj.sendmail(sender, receiver, message)
    print("e-mail successfully sent!")
except:
    print("Error while sending e-mail.")
finally:
    print("\n" + message)   