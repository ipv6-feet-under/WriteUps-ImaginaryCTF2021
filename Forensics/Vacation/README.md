![ImaginaryCTF](../../banner.png)

# Vacation

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|100|Forensics|339|

### Description

```
Roo's cousin was on vacation, but he forgot to tell us where he went! But he posted this image on his social media. Could you track down his location? Submit your answer as ictf{latitude_longitude}, with both rounded to 3 decimal places. Example: ictf{-12.345_42.424} (Note: only the image is needed for this challenge, as this is an OSINT challenge.)	
```

### Attachments

```
https://imaginaryctf.org/r/EA9D-image.jpg
```
I just google searched South Lake Tahoe + Rock Shop and this is where it took me:

https://www.google.com/maps/@38.94711,-119.9614202,3a,61.6y,72.05h,91.14t/data=!3m9!1e1!3m7!1soFk1nXrY9AhpaaIpQOhM2g!2e0!7i16384!8i8192!9m2!1b1!2i27

Just get the coords from the url und put it in flag format.



There is our flag:
```
ictf{38.947_-119.961}
```