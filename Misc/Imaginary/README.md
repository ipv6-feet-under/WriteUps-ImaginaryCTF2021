![ImaginaryCTF](../../banner.png)

# Imaginary

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|100|Misc|185|

### Description

```
What's ImaginaryCTF without good old sqrt(-1)?
```

### Attachments

* [imaginary.py](imaginary.py)
* nc chal.imaginaryctf.org 42015

* [imag_solver.py](imag_solver.py)

We are given a NetCat-Connection and an executable. Let's first get a look at nc:
```
└─$ nc chal.imaginaryctf.org 42015

Welcome to the Imaginary challenge! I'm gonna give you 300 imaginary/complex number problems, and your job is to solve them all. Good luck!

Sample input: (55+42i) + (12+5i) - (124+15i)
Sample output: -57+32i

Sample input: (23+32i) + (3+500i) - (11+44i)
Sample output: 15+488i

(NOTE: DO NOT USE eval() ON THE CHALLENGE OUTPUT. TREAT THIS IS UNTRUSTED INPUT. Every once in a while the challenge will attempt to forkbomb your system if you are using eval(), so watch out!)

(18+48i) + (44+40i)
> 62+88i 
Correct!
(18+40i) - (15+49i) + (21+4i)
> 21+12i
That's incorrect. :(

```
So the program asks to calculate 300 complex number problems. After sending our solution it answeres `Correct!` or `That's incorrect. :(`. Besides we get the hint to not use the `eval()`-function as it will forkbomb our system from time to time. But let's not get tricked and get a look at the [imaginary.py](imaginary.py) to see what we can do.

At first get a look at that eval()-problem, as we do not want to write our own evaluation-function neither get forkbombed:
```py
	o = random.randint(0,50)
	if o > 0:
    [...]
	else:
		n = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
		payload = f"__import__['os'].system('{n}(){{ {n}|{n} & }};{{{n}}}')"
		print(payload)
		input("> ")
		print("Correct!")
```
The script tells us that there is a random integer `o` between 0 and 50. When it is exactly 0 we will get this payload otherwise it gives us the complex number problem.
As the payload is hardcoded and always starts with `__import[...]` we can just check for that before executing the `eval()` to avoid the forkbomb.

The rest of the script is just generating complex number problems with random integers in the format `(X [+,-] Yi) [+-] (X2 [+,-] Y2i) ...`. Internally the problem is solved with the unknown `solve()`-function and compared with our input.

Now we know enough to set up our own script [imag_solver.py](imag_solver.py).

The solving part is done in the `calc(math)`-function as it accepts a string and solves the math problem with the `eval()` function, even if we are not "allowed" to use it... (but it's a CTF you know ;-) 
```py
def calc(math):
	if math.startswith('__'): return 'sth'
	if math.startswith('You'): print(r.recvline()); return 'sth'
	math = math.replace('i','j')
	
	sol = str(eval(math))
	sol = sol.replace('j','i')
	sol = sol.replace('(','')
	sol = sol.replace(')','')
	return sol
```
To get rid of the forkbomb we just check if the string starts with those `__` from `"__import__['os']...`. In this case we don't `eval()` the input, but just returning 'sth' as the answere. In the other cases it can only be the math problems as we know the original source code. As the `eval()` understands complex numbers with 'j's instead of 'i's we have to replace them first and get rid of the brackets. No we can calculate the problem with `eval(math)` very easy. To match the input format of the program, we have to change the 'j's back to 'i's and delete those brackets again.

The final part is just the interaction and the loop to solve 300 problems with some prints to know it works:

```py
[...]
math = r.recvuntil('\n')
math = math.decode('utf-8')
print("Current task: " + math)
r.recvuntil('>')
sol = calc(math)
print("Calculated: " + sol + '\n')
r.send(sol + '\n')
i=0

while i<299:
	corr = r.recvline()
	#corr = corr.decode('utf-8')
	print(corr)
	if corr == b' Correct!\n':
		math = r.recvuntil('\n')
		math = math.decode('utf-8')
		print("Current task: " + math)
		r.recvuntil('>')
		sol = calc(math)
		print("Calculated: " + sol + '\n')
		r.send(sol + '\n')
		i += 1
	else:
  		break

print(r.recvline())
print(r.recvline())
print(r.recvline())

```
After one solution before the loop to await the first "Correct!" and 299 solves in the loop we can recieve the flag.

There is our flag:
```
ictf{n1c3_y0u_c4n_4dd_4nd_subtr4ct!_49fd21bc}
```
