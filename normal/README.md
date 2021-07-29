![ImaginaryCTF](../../banner.png)

# Normal

|Author|Points|Category|Solves|
|---|---|---|---|
|puzzler7|150|Reversing|109|

### Description

```
Norse senor snorts spores, abhors non-nors, adores s'mores, and snores.	
```

### Attachments

* [Makefile](Makefile)
* [normal.v](normal.v)
* [normal_solver.py](normal_solver.py)

In this reverse challenge we are given a Makefile and a normal.v. The normal.v is the file of interest as it contains [Verilog](https://de.wikipedia.org/wiki/Verilog)-Code:
The important part is called by the `normal flagchecker(wrong, flag)` function. In here the flag gets NOR-ed with two ciphers in several steps and finally with `wrong`:
```v
module normal(out, in);
    output [255:0] out;
    input [255:0] in;
    wire [255:0] w1, w2, w3, w4, w5, w6, w7, w8; 

    wire [255:0] c1, c2;
    assign c1 = 256'h44940e8301e14fb33ba0da63cd5d2739ad079d571d9f5b987a1c3db2b60c92a3;
    assign c2 = 256'hd208851a855f817d9b3744bd03fdacae61a70c9b953fca57f78e9d2379814c21;
    
    nor n1 [255:0] (w1, in, c1);
    nor n2 [255:0] (w2, in, w1);
    nor n3 [255:0] (w3, c1, w1);
    nor n4 [255:0] (w4, w2, w3);
    nor n5 [255:0] (w5, w4, w4);
    nor n6 [255:0] (w6, w5, c2);
    nor n7 [255:0] (w7, w5, w6);
    nor n8 [255:0] (w8, c2, w6);
    nor n9 [255:0] (out, w7, w8);
endmodule
```
To find out what `wrong` hast to be we need to simplify the NOR-expressions. 

A function like `nor n1 [255:0] (X, Y, Z)` NORes `Y` and `Z` and writes it into `X`. So we can translate each function to something like `X : not (Y or Z)` while we can already simplify `Y` and `Z` from steps before and insert it. We can use [WolframAlpha](https://www.wolframalpha.com/) if we dont want to simplify it by ourselves, as WolframAlpha already gives us minimized forms in different variants.

For better readability and interaction with WolframAlpha we changed the names of the variables in the minimzing process:
```
in --> A
c1 --> B
c2 --> C
```

By symplifying and minimizing each funtcion we can set up the following table:

|Verilog|simplified logical expression|
|---|---|
|`nor n1 [255:0] (w1, A, B);`|`w1 = not (A or B)`|
|`nor n2 [255:0] (w2, A, w1);`|`w2 = not A and B`|
|`nor n3 [255:0] (w3, B, w1);`|`w3 = A and not B`|
|`nor n4 [255:0] (w4, w2, w3);`|`not ((not A and B) or (A and not B))`|
|`nor n5 [255:0] (w5, w4, w4);`|`w5 = A XOR B`|
|`nor n6 [255:0] (w6, w5, C);`|`w6 = not ((A XOR B) or (C))`|
|`nor n7 [255:0] (w7, w5, w6);`|`not ((A XOR B) or (not ((A XOR B) or (C))))`|
|`nor n8 [255:0] (w8, C, w6);`|`w8 = not ((C) or (not ((A XOR B) or (C))))`|
|`nor n9 [255:0] (out, w7, w8);`|`not ((not ((A XOR B) or (not ((A XOR B) or (C))))) or (not ((C) or (not ((A XOR B) or (C))))))`|

The last expression can be minized to: `out = not (A XOR B XOR C)`.

So finally we get the expression we need: `wrong = not (flag XOR c1 XOR c2)`.
Now we can set up a [normal_solver.py](python script) to get our flag:

In the file you can see that we just need the given inputs, set up functions for the logical expressions XOR, AND and NOT and translate our minimized expression `wrong = not (flag XOR c1 XOR c2)` into some python code:
```py
wrong = byte_xor(flag, c1)
wrong = byte_xor(wrong, c2)
wrong = byte_not(wrong)

print(wrong)
```


There is our flag:
```
ictf{A11_ha!1_th3_n3w_n0rm_n0r!}
```
