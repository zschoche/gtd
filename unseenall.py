#!/usr/bin/python3
import config
import sys


if len(sys.argv) != 2:
    print("usage: unseenall.py [folder]")
else:
    src = str(sys.argv[1])
 

    from imap_tools import MailBox, MailMessageFlags
    with MailBox(config.smtpServer).login(config.smtpUser, config.smtpPassword, initial_folder=src) as mailbox:
        mails= mailbox.fetch()
        mailbox.flag(mails, MailMessageFlags.SEEN, False)
