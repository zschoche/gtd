#!/usr/bin/python3
import config
import sys
from datetime import datetime


if len(sys.argv) != 3:
    print("usage: move-new-delayed-todos.py [src] [dest]")
else:
    src = str(sys.argv[1])
    dest = str(sys.argv[2])

    from imap_tools import MailBox, AND, OR, NOT, H
    with MailBox(config.smtpServer).login(config.smtpUser, config.smtpPassword, initial_folder=src) as mailbox:
        mails= mailbox.fetch(AND(header=[H('To', 'todo-'),H('To', config.domain)]))
        for m in mails:
            if len(m.to)!=1:
                raise "To many recipients"+m.to[0]
            if datetime.strptime(m.to[0][5:15], '%d.%m.%Y') > datetime.today():
                mailbox.move(m.uid, dest)


