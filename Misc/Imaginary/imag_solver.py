#!/usr/bin/env python3

from pwn import *
import sys

host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user

def calc(math):
	if math.startswith('__'): return 'sth'
	if math.startswith('You'): print(r.recvline()); return 'sth'
	math = math.replace('i','j')
	
	sol = str(eval(math))
	sol = sol.replace('j','i')
	sol = sol.replace('(','')
	sol = sol.replace(')','')
	return sol

r = remote(host, port)

r.recvuntil('out!)\n\n')




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


'''
' Correct!\n'
Current task: (40+41i) - (6+9i) - (2+40i) - (3+36i) - (5+36i) - (37+13i) + (30+22i) - (17+7i) - (47+9i) + (49+14i) + (44+40i) + (8+6i) - (23+46i) - (36+28i) - (30+40i) - (28+46i) + (29+44i) - (14+47i) + (12+3i) + (19+43i) - (19+47i) - (46+17i) + (28+32i) + (48+19i) + (43+28i) + (44+46i) + (45+6i) - (36+15i) - (15+47i) - (39+14i) + (31+34i) - (20+48i) - (18+7i) - (28+21i) + (41+42i) - (23+14i) + (13+33i) + (28+5i) + (38+49i) - (34+12i) + (28+7i) - (24+30i) - (7+39i) + (29+6i) + (19+18i) - (42+13i) - (2+39i) - (50+17i) + (25+40i) - (18+14i) + (25+38i) + (2+16i) + (49+35i) + (4+11i) + (8+18i) + (50+20i) - (3+50i) - (41+9i) + (26+15i) - (39+40i) + (5+8i) - (2+40i) - (8+32i) - (19+29i) + (9+5i) - (0+37i) - (44+18i) + (31+50i) - (23+37i) - (4+19i) - (10+40i) + (15+46i) + (15+50i) - (12+24i) + (14+50i) - (47+44i) - (7+9i) - (41+13i) - (30+10i) + (46+26i) - (5+9i) + (24+13i) - (49+38i) - (12+36i) + (35+26i) + (29+10i) + (42+39i) + (20+32i) - (48+29i) - (38+44i) - (31+33i) - (30+33i) + (23+45i) + (27+31i) + (44+48i) + (26+11i) - (6+5i) - (8+9i) - (20+26i) + (40+36i) - (4+11i) - (9+35i) + (27+27i) - (27+32i) - (47+13i) + (50+15i) + (23+24i) + (14+46i) + (8+44i) + (1+25i) + (37+3i) + (18+40i) - (26+10i) + (28+43i) + (45+3i) - (7+44i) + (43+36i) + (11+26i) + (22+15i) - (48+45i) + (13+30i) - (44+39i) - (25+49i) + (46+3i) - (20+48i) - (28+0i) - (28+15i) + (32+27i) - (34+10i) - (36+31i) + (38+15i) - (41+6i) + (31+36i) - (33+25i) + (33+37i) + (33+43i) - (14+13i) - (12+18i) + (3+3i) - (15+15i) - (24+30i) - (24+38i) - (38+50i) - (41+40i) - (0+7i) - (46+14i) - (0+13i) + (20+49i) + (7+0i) - (3+50i) - (19+42i) - (47+42i) + (8+5i) + (5+30i) + (44+12i) + (12+41i) + (30+17i) - (13+10i) + (16+7i) + (34+15i) + (16+15i) + (25+46i) + (22+38i) - (8+13i) + (23+12i) + (47+37i) + (13+16i) - (40+28i) + (21+40i) + (24+11i) - (7+32i) - (8+35i) - (32+42i) - (39+24i) - (47+10i) - (10+13i) - (2+35i) - (23+14i) - (24+20i) + (50+5i) + (32+14i) + (42+50i) - (41+5i) - (24+35i) - (50+45i) - (14+6i) + (17+45i) - (39+0i) - (42+8i) + (22+13i) + (42+18i) - (5+35i) - (15+46i) - (10+23i) - (32+10i) + (20+5i) + (48+7i) - (41+50i) - (47+6i) - (7+41i) + (22+8i) - (41+6i) + (0+12i) + (32+25i) - (27+18i) - (22+20i) + (6+3i) + (41+35i) + (11+16i) + (18+7i) + (20+42i) - (39+25i) + (31+28i) + (1+20i) + (12+45i) - (17+0i) + (12+33i) - (42+23i) - (37+29i) - (42+3i) + (22+17i) + (32+3i) - (31+12i) + (47+50i) + (16+20i) - (30+25i) - (27+39i) + (27+24i) + (48+26i) - (5+0i) + (15+22i) - (2+18i) + (0+20i) - (0+29i) - (5+18i) - (1+30i) + (38+14i) + (25+10i) - (22+22i) + (14+2i) - (6+44i) - (22+1i) - (43+33i) + (39+40i) + (45+37i) + (36+29i) + (18+17i) - (1+34i) + (17+40i) + (12+15i) - (28+37i) - (8+10i) - (22+14i) - (0+6i) + (42+34i)

Calculated: 69-291i

b' Correct!\n'
b"You did it! Here's your flag!\n"
b'ictf{n1c3_y0u_c4n_4dd_4nd_subtr4ct!_49fd21bc}\n'
b'\n'
[*] Closed connection to chal.imaginaryctf.org port 42015 '''
