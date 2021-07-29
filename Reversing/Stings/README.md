![ImaginaryCTF](../../banner.png)

# Stings

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|100|Reversing|291|

### Description

```
Enter the beehive. Don't get stung.

(Note: the password/flag is in the format ictf{.*})	
```

### Attachments

```
https://2021.imaginaryctf.org/r/stings
```
launch it in gdb-peda and run <<< $(python2.7 -c 'print "ictf{str1ngs_4r3nt_h1dd3n_17b21a69}"') you can go one by one with starting ictf and see what is compared until you retrieved the whole flag

![IMAGE_FOR_EXAMPLE](GOOD_IMAGE_TITLE.png)



There is our flag:
```
ictf{str1ngs_4r3nt_h1dd3n_17b21a69}
```