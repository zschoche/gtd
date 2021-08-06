#!/usr/bin/python3
import config
import sys
from datetime import datetime


if len(sys.argv) != 3:
    print("usage: move-delayed-todos.py [src] [dest]")
else:
    src = str(sys.argv[1])
    dest = str(sys.argv[2])
    addr = "todo-"+datetime.today().strftime("%d.%m.%Y")+config.domain

    from imap_tools import MailBox, AND, OR, NOT
    with MailBox(config.smtpServer).login(config.smtpUser, config.smtpPassword, initial_folder=src) as mailbox:
        mails=mailbox.fetch(OR(to=addr))
        mailbox.move(mails, dest)
