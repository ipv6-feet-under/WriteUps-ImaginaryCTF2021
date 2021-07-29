![ImaginaryCTF](../../banner.png)

# Mazed

|Author|Points|Category|Solves|
|---|---|---|---|
|puzzler7|225|Misc|38|

### Description

```
I was making an n-dimensional maze for a different challenge, with the intention for players to exploit the maze. However, it seemed a shame to waste, so here's the raw maze, exploit free.
```

### Attachments

```
https://imaginaryctf.org/r/885D-maze.py
nc chal.imaginaryctf.org 42017
```
Just keep on sending "abdc" until eventually the stars line up perfecty and you get the flag, because we just jump backwards.
The only "problem" here is when there are walls on the 3 corners we jump to before we reach the flag. In that case just try it again..


There is our flag:
```
ictf{I_bet_youre_expecting_a_pun_like_aMAZEing_here_but_Im_a_better_person_than_that}
```