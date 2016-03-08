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

.. math::
 \mathbf{M} = \left[\begin{array}
 {llll}
 b_{0} & b_{4} & b_{8}  & b_{12}\\
 b_{1} & b_{5} & b_{9}  & b_{13}\\
 b_{2} & b_{6} & b_{10} & b_{14}\\
 b_{3} & b_{7} & b_{11} & b_{15}
 \end{array}\right]

I have choosen a slightly different layout:

.. math::
 \mathbf{State} = \left[\begin{array}
 {llll}
 b_{0}  & b_{1}  & b_{2}  & b_{3}\\
 b_{4}  & b_{5}  & b_{6}  & b_{7}\\
 b_{8}  & b_{9}  & b_{10} & b_{11}\\
 b_{12} & b_{13} & b_{14} & b_{15}
 \end{array}\right]

and a similar one dimensional layout for the key:

.. math::
 \mathbf{Key} = \left[\begin{array}
 {llll}
 b_{0}  & ...  & b_{n}
 \end{array}\right]

A layout like this keeps the implementation much more straight forward.
This also means that the shift rows oration in reality shifts columns, and the
mix columns multiplies each row instead of each column. Yet i have kept to
original names of the functions instead of changing to shift columns and mix
rows, simply because this makes it easier to understand the steps in the
encryption and decryption process.

