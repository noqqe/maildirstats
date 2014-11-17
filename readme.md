# maildirstats

`maildirstats` is just a very small python script which aims to gather some plaintext data about your
local maildir.

I use `offlineimap` and `mairix` for my imap mail account to be able to search through my mails
easily integrated in `mutt`. But as I am interested in statistics in all kind of data I created this
little script to get a short overview of my mails.

# Installation

```bash
$ git clone https://github.com/noqqe/maildirstats
$ cd maildirstats
$ python maildirstats.py
$ # or even better:
$ python maildirstats.py > report.txt
```

But at first specify your maildir path within the script ;)
See below.

# Configuration

The configuration part is just two lines at the top of the script.

```
maildirpath="/path/to/your/Maildir/"
blacklist="<regex>"
```
In my case, RegEx looks something like

```
blacklist="(Archives*|Spam|.mairixdb|Archives.*Social|.*Tech)"
```

If you dont want to exclude any directoy, just comment out the blacklist variable.

# Results

the output that you can expect looks something like this (shortened for readability):

```
### People
1: some@example.org
12: other@example.org
21: another@example.org
[...]

### X-Mailer
46: Microsoft Office Outlook, Build 11.0.5510
50: Microsoft Office Outlook 12.0
55: iPhone Mail (10B329)
70: WWW-Mail 6100 (Global Message Exchange)
97: Apple Mail (2.1077)
[...]

### Year
2008: 40
2009: 1802
2010: 2783
2011: 2451
2012: 1688
2013: 3475
2014: 4821

### Month
01: 1299
02: 1208
03: 1281
04: 1327
05: 1642
[...]
12: 1127

### Day
01: 601
02: 571
03: 495
04: 543
[...]
31: 523

### Weekday
Monday: 2860
Tuesday: 2613
Friday: 2521
Wednesday: 2654
Thursday: 3043
Sunday: 1756
Saturday: 1613

### Hour
00: 425
01: 311
02: 238
03: 253
[...]
23: 241

### Minute
00: 369
01: 310
02: 326
[...]
59: 200
```

