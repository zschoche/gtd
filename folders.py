#!/usr/bin/python3
import config

from imap_tools import MailBox
with MailBox(config.smtpServer).login(config.smtpUser, config.smtpPassword, initial_folder='INBOX') as mailbox:
    for f in mailbox.folder.list('INBOX'):
        print(f['name'])
