#!/usr/bin/python3
import config
import sys


if len(sys.argv) != 3:
    print("usage: copyall.py [src] [dest]")
else:
    src = str(sys.argv[1])
    dest = str(sys.argv[2])

    from imap_tools import MailBox
    with MailBox(config.smtpServer).login(config.smtpUser, config.smtpPassword, initial_folder=src) as mailbox:
        mails= mailbox.fetch()
        mailbox.copy(mails, dest)
