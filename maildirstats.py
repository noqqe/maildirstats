#!/usr/bin/env python

import os
import re
import sys
import time
import mailbox
import operator
import email.utils
from email.header import decode_header

### Settings
# Path to your Maildir directory
maildirpath="/home/noqqe/Maildir/"

# Blacklist regex here (uncomment and fill with regex if you want to enable)
#blacklist="(Spam|\\.mairixdb|Archives.*Social|.*Tech)"

### Runtime
# Generate list of maildirs without blacklisted ones
try:
    dirs = [k for k in os.listdir(maildirpath) if re.match(blacklist,k) is None ]
except:
    dirs = os.listdir(maildirpath)

# Initialize objects
people = dict()
mailYear = dict()
mailMonth = dict()
mailDay = dict()
mailWeekday = dict()
mailHour = dict()
mailMinute = dict()
xmailers = dict()

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
    f = re.sub(r'.*<(.*)>.*',r'\1',f)
    scoreMap(f,people)

def mailDate(msg):
    date = getHeader(msg,"Date")
    try:
        date = email.utils.parsedate(date)
        date = time.localtime(time.mktime(date))
        scoreMap(time.strftime("%Y", date),mailYear)
        scoreMap(time.strftime("%m", date),mailMonth)
        scoreMap(time.strftime("%d", date),mailDay)
        scoreMap(time.strftime("%A", date),mailWeekday)
        scoreMap(time.strftime("%H", date),mailHour)
        scoreMap(time.strftime("%M", date),mailMinute)
    except:
        pass

def mailers(msg):
    m = getHeader(msg,"X-Mailer")
    scoreMap(m,xmailers)

for box in dirs:
    try:
        maildir = mailbox.Maildir(maildirpath + box, factory=mailbox.MaildirMessage)
        for msg in maildir:
            senderList(msg)
            mailDate(msg)
            mailers(msg)
    except:
        pass

print "### People"
for x in sorted(people.items(), key=operator.itemgetter(1)):
    print str(x[1])+": "+str(x[0])
print ""

print "### X-Mailer"
for x in sorted(xmailers.items(), key=operator.itemgetter(1)):
    print str(x[1])+": "+str(x[0])
print ""

print "### Year"
for x in sorted(mailYear.items(), key=operator.itemgetter(0)):
    print str(x[0])+": "+str(x[1])
print ""

print "### Month"
for x in sorted(mailMonth.items(), key=operator.itemgetter(0)):
    print str(x[0])+": "+str(x[1])
print ""

print "### Day"
for x in sorted(mailDay.items(), key=operator.itemgetter(0)):
    print str(x[0])+": "+str(x[1])
print ""

print "### Weekday"
for x in mailWeekday.items():
    print str(x[0])+": "+str(x[1])
print ""

print "### Hour"
for x in sorted(mailHour.items(), key=operator.itemgetter(0)):
    print str(x[0])+": "+str(x[1])
print ""

print "### Minute"
for x in sorted(mailMinute.items(), key=operator.itemgetter(0)):
    print str(x[0])+": "+str(x[1])
print ""

