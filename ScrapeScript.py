# This project/script is intended to be a scraper for gmail emails.
# I will configure it to simplify school emails at first and expand
# to make it more of a general program later.

import email, getpass, imaplib, re, os

# This name may need to be changed as "User" may not stay consistent
attachmentDirectory = "C:\Users\User\Documents\Programming Projects\Gmail Web Crawler"

username = raw_input("Enter Gmail account: ")
password = getpass.getpass("Enter account password: ")

server = imaplib.IMAP4_SSL("imap.gmail.com")
server.login(username, password)
