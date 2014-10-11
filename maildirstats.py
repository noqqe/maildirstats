#!/usr/bin/env python

import os
import sys
import time
import mailbox
from email.header import decode_header

mymaildir="/home/noqqe/Maildir/INBOX/"
people = dict()

box = mailbox.Maildir(mymaildir, factory=mailbox.MaildirMessage)

def getHeader(msg,header):
   m = msg.get(header, 'empty')
   m = decode_header(m)
   m = m[0][0] # transform list(tuple()) into str()
   return m



for msg in box:
    f = getHeader(msg,"From")
    if f in people:
        people[f] += 1
    else:
        people[f] = 1

print people 

