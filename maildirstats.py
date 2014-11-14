#!/usr/bin/env python

import os
import re
import sh
import sys
import time
import mailbox
import operator
from email.header import decode_header
import email.utils

# Settings
boxesdir="/home/noqqe/Maildir/"
blacklist="(Archives.TMT*|Spam|Archives.noris*|.mairixdb|Archives.*Social|.*Tech)"
dirs = [k for k in os.listdir(boxesdir) if re.match(blacklist,k) is None ]

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

def scoreMap(value,map):
    if value in map:
        map[value] += 1
    else:
        map[value] = 1

# Functions (high level)
def senderList(msg):
    f = getHeader(msg,"From")
    scoreMap(f,people)

def mailDate(msg):
    date = getHeader(msg,"Date")
    try:
        date = email.utils.parsedate(date)
        full = time.strftime("%F %H:%M:%S", date)
        scoreMap(time.strftime("%Y", date),mailYear)
        scoreMap(time.strftime("%m", date),mailMonth)
        scoreMap(time.strftime("%d", date),mailDay)
    except:
        pass 
 
# Runtime
for box in dirs:
    print box
    try: 
        maildir = mailbox.Maildir(boxesdir + box, factory=mailbox.MaildirMessage)
        for msg in maildir:
            senderList(msg)
            mailDate(msg)
    except:
        pass

print sorted(people.items(), key=operator.itemgetter(1)) 
print sorted(mailYear.items(), key=operator.itemgetter(1)) 
print sorted(mailMonth.items(), key=operator.itemgetter(1)) 
print sorted(mailDay.items(), key=operator.itemgetter(1)) 

