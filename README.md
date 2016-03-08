Advanced Encryption Standard (AES)
=================================

This is an implementation of the [Advanced Encryption
Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard), also known as
Rijndael, in pure python.

It supports 128, 192 and 256 bit keys.


Design
------

Rather than going for the tradidional state and key layout decribed in
the AES specification:

```
          ┌                          ┐
          │ b0 b4 b8  b12 │   
   M = │ b1 b5 b9  b13 │
          │ b2 b6 b10 b14 │
          │ b3 b7 b11 b15 │
          └                          ┘
```

I have choosen a slightly different layout for the state, with a similar one dimensional layout for the key:

```
          ┌                             ┐
          │ b0  b1  b2  b3  │   
   S = │ b4  b5  b6  b7  │
          │ b8  b9  b10 b11 │
          │ b12 b13 b14 b15 │
          └                             ┘
          ┌               ┐
   K = │ b1 ... bn │
          └               ┘
```

A layout like this keeps the implementation much more straight forward.
This also means that the shift rows oration in reality shifts columns, and the
mix columns multiplies each row instead of each column. Yet i have kept to
original names of the functions instead of changing to shift columns and mix
rows, simply because this makes it easier to understand the steps in the
encryption and decryption process.

