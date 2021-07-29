![ImaginaryCTF](../../banner.png)

# Stackoverflow

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|50|Pwn|413|

### Description

```
Welcome to Stack Overflow! Get answers to all your programming questions right here!
```

### Attachments

* [stackoverflow](stackoverflow)
* nc chal.imaginaryctf.org 42001

We are given a NetCat-Connection and an executable. Let's first get a look at nc:
```sh
└─$ nc chal.imaginaryctf.org 42001
Welcome to StackOverflow! Before you start ~~copypasting code~~ asking good questions, we would like you to answer a question. What's your favorite color?
green
Thanks! Now onto the posts!
ERROR: FEATURE NOT IMPLEMENTED YET
```
The programm asks for a color, answeres a short text and throws an error.
Let's get a look at the executable to find out what it does. Therefor we can use ghidra to analyze the file.

![ghidra.PNG](ghidra.PNG)



There is our flag:
```
ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}
```
