![ImaginaryCTF](../../banner.png)

# Unpuzzled 2

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|100|Forensics|77|

### Description

```
Puzzler7's evil twin is hiding one more secret. Find it for us. (Note: the flag for this challenge ends with 6148}.)

Note: DO NOT stalk/OSINT puzzler7#7657. This will not help you solve this challenge, and will only lead you away from the right solution.
```

### Attachments

```
None
```
Searching for his username with "sherlock" gives us the following output:

```
┌──(kali㉿kali)-[~]
└─$ sherlock unpuzzler7                
[*] Checking username unpuzzler7 on:
[+] ICQ: https://icq.im/unpuzzler7
[+] Quora: https://www.quora.com/profile/unpuzzler7
[+] Repl.it: https://repl.it/@unpuzzler7
```
While ICQ and Quora are false-positives, we find an interesting source on his repl.it:
https://replit.com/@Unpuzzler7/DiscordBot?v=1
And an even more interesting keep_alive.py:
```py
from flask import Flask
from threading import Thread
import random
import base64

app = Flask('')

@app.route('/')
def home():
  '''
  https://discord.gg/zZCFu4Mgsh
  '''
	return 'Im in!' + '<br>'*100000000 + '/* ' + base64.b64decode('aWN0ZntyM3BsMXRfMXNudF90aDNfcGw0YzNfdDBfc3QwcjNfczNjcjN0c18xY2IyNjE0OH0=').decode() + ' */'

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)
```
base64 decode that string and you get the flag


There is our flag:
```
ictf{r3pl1t_1snt_th3_pl4c3_t0_st0r3_s3cr3ts_1cb26148}
```