#!/usr/bin/python3

import json
import config
import sys
import smtplib
import ssl

def sendtodo(sender,receiver,msg):
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(config.smtpServer,config.smtpPort)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(config.smtpUser, config.smtpPassword)
        message = "From: "+sender+"\r\nTo: "+receiver+"\r\nSubject: [TODO] "+msg+"\r\n\r\n"
        server.sendmail(sender, receiver, message)
        server.quit() 
    except Exception as e:
    # Print any error messages to stdout
        print(e)




if len(sys.argv) != 4:
    print("usage: signal-to-mail.py [sender] [receiver] [phone number]")
else:
    sender= str(sys.argv[1])
    receiver = str(sys.argv[2])
    phone = str(sys.argv[3])
    for line in sys.stdin.readlines():
        env = json.loads(line)
        print(env)
        if env['envelope']['source'] == phone:
            sendtodo(sender,receiver, env['envelope']['syncMessage']['sentMessage']['message'])
