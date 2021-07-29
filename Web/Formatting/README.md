![ImaginaryCTF](../../banner.png)

# Formatting

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|100|Web|302|

### Description

```
Wait, I thought format strings were only in C???	
```

### Attachments

```
https://imaginaryctf.org/r/14BD-stonks.py
nc chal.imaginaryctf.org 42014
```
I just googled python format strings vulnerability and followed the [first thing I found](https://www.netsparker.com/blog/web-security/format-string-vulnerabilities/).

```py
flag = open("flag.txt").read()
```

So flag is our secret value and we can manipulate the argument `a`:

```
{a.__init__.__globals__[flag]}
```


There is our flag:
```
ictf{c4r3rul_w1th_f0rmat_str1ngs_4a2bd219}
```