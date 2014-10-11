#!/usr/bin/env python

import os
import sys
import time
import mailbox
import operator
from email.header import decode_header
import email.utils

# Settings
box="/home/noqqe/Maildir/INBOX/"
box = mailbox.Maildir(box, factory=mailbox.MaildirMessage)
people = dict()
mailYear = dict()
mailMonth = dict()
mailDay= dict()

# Functions (low level)
def getHeader(msg,header):
   m = msg.get(header, 'empty')
   m = decode_header(m)
   m = m[0][0] # transform list(tuple()) into str()
   return m

# Functions (high level)
def senderList(msg):
    f = getHeader(msg,"From")
    if f in people:
        people[f] += 1
    else:
        people[f] = 1

def mailDate(msg):
    date = getHeader(msg,"Date")
    date = email.utils.parsedate(date)
    full = time.strftime("%F %H:%M:%S", date)
    y = time.strftime("%Y", date)
    if y in mailYear:
        mailYear[y] += 1
    else:
        mailYear[y] = 1
    m = time.strftime("%m", date)
    if m in mailMonth:
        mailMonth[m] += 1
    else:
        mailMonth[m] = 1
    d = time.strftime("%d", date)
    if d in mailDay:
        mailDay[d] += 1
    else:
        mailDay[d] = 1
 
# Runtime
for msg in box:
    #senderList(msg)
    mailDate(msg)

#print sorted(people.items(), key=operator.itemgetter(1)) 
print sorted(mailYear.items(), key=operator.itemgetter(1)) 
print sorted(mailMonth.items(), key=operator.itemgetter(1)) 
print sorted(mailDay.items(), key=operator.itemgetter(1)) 

