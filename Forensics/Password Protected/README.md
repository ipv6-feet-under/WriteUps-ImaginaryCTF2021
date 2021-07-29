![ImaginaryCTF](../../banner.png)

# Password Protected

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|150|Forensics|26|

### Description

```
I made a pwn challenge for you guys to test. To make sure only the best hackers test my challenge, I made sure that I encrypted my files with a 16 character long randomly generated password. Good luck!

Note: I do all my pwn on Ubuntu 18.	
```

### Attachments

```
https://imaginaryctf.org/r/F338-leaks.txt
https://imaginaryctf.org/r/EC4F-encrypted.zip
```
We are given two files: an encrypted zip with the following content:
```
libc.so.6
runme
flag.txt
```
and a leaks.txt:
```
gets(): 0x00005555555daaf0
puts(): 0x00005555555db5a0
printf(): 0x00005555555b8e10
malloc(): 0x00005555555f1260
```

The challenge here was propably to do a known plaintext attack with the right offset and the plaintext from leaks.txt or something. However we just took the libc.so.6 file from the "String Editor 1"-Challenge, zipped it on a Ubuntu 18 subsystem into "plain.zip" and ran:
```
.\bkcrack -C encrypted.zip -c libc.so.6 -P plain.zip -p libc.so.6
```
We then used the extracted keys and the tool again to set a new password and read the flag.txt.


There is our flag:
```
ictf{dont_use_zipcrypto_5e2b32f3}
```