#!/usr/bin/python3
import config
import sys


if len(sys.argv) != 3:
    print("usage: move-new-todos.py [src] [dest]")
else:
    src = str(sys.argv[1])
    dest = str(sys.argv[2])

    from imap_tools import MailBox, AND, OR, NOT
    with MailBox(config.smtpServer).login(config.smtpUser, config.smtpPassword, initial_folder=src) as mailbox:
        mails= mailbox.fetch(OR(to=config.todoMail,from_=config.todoMail))
        mailbox.move(mails, dest)
