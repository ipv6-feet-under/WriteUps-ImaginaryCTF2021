![ImaginaryCTF](../../banner.png)

# Flip Flops

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|100|Crypto|160|

### Description

```
Yesterday, Roo bought some new flip flops. Let's see how good at flopping you are.	
```

### Attachments

```
https://imaginaryctf.org/r/7B4E-flop.py
nc chal.imaginaryctf.org 42011
```
encrypt: timmeflag0000000timmeflag0000000timmeflag0000000
XOR first byte with 13, because t XOR g = 13
check resulting string


There is our flag:
```
ictf{fl1p_fl0p_b1ts_fl1pped_b6731f96}
```