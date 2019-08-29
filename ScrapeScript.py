# This project/script is intended to be a scraper for gmail emails.
# I will configure it to simplify specific email addresses at first and expand
# to make it more of a general program later.

import email, getpass, imaplib, re, os

# This name may need to be changed as "User" may not stay consistent
attachmentDirectory = "C:\Users\User\Documents\Programming Projects\Gmail Web Crawler"

# Collect the password and username upon script startup
username = raw_input("Enter Gmail account: ")
password = getpass.getpass("Enter account password: ")

# Connect to the gmail server and log in
mailbox = imaplib.IMAP4_SSL("imap.gmail.com")
mailbox.login(username, password)

# Can select individual folders or the whole inbox
mailbox.select("INBOX")

resp, messageID = mailbox.search(None, '(FROM "reply@email.livenation.com")')
messageID = messageID[0].split()
isolatedMessage = []
numIsolatedMessages = 0
stopLooking = False

for message in messageID[::-1]:
    resp, data = mailbox.fetch(message, "(RFC822)")
    if(stopLooking):
        break
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            varSubject = msg['subject']
            varDate = msg['date']
        
        #continue based on https://stackoverflow.com/questions/14294057/extract-information-from-gmail-with-python
        # the 'ones beginning with' section
        # if varSubject[0] = 
