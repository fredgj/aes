Advanced Encryption Standard (AES)
=================================

This is an implementation of the [Advanced Encryption
Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard), also known as
Rijndael, in pure python.

It supports 128, 192 and 256 bit keys.


Design
------

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cmathbf%7BK%7D+%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bllll%7Db_%7B0%7D++%26+%5Ccdots+%26+b_%7Bn%7D%5Cend%7Barray%7D%5Cright%5D&fc=Black&im=jpg&fs=16&ff=modern&edit=)

Rather than going for the tradidional state and key layout decribed in
the AES specification:

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cmathbf%7BM%7D+%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bllll%7Db_%7B0%7D+%26+b_%7B4%7D+%26+b_%7B8%7D++%26+b_%7B12%7D%5C%5Cb_%7B1%7D+%26+b_%7B5%7D+%26+b_%7B9%7D++%26+b_%7B13%7D%5C%5Cb_%7B2%7D+%26+b_%7B6%7D+%26+b_%7B10%7D+%26+b_%7B14%7D%5C%5Cb_%7B3%7D+%26+b_%7B7%7D+%26+b_%7B11%7D+%26+b_%7B15%7D%5Cend%7Barray%7D%5Cright%5D&fc=Black&im=jpg&fs=16&ff=modern&edit=)

I have choosen a slightly different layout for the state:

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cmathbf%7BS%7D+%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bllll%7Db_%7B0%7D++%26+b_%7B1%7D++%26+b_%7B2%7D++%26+b_%7B3%7D%5C%5Cb_%7B4%7D++%26+b_%7B5%7D++%26+b_%7B6%7D++%26+b_%7B7%7D%5C%5Cb_%7B8%7D++%26+b_%7B9%7D++%26+b_%7B10%7D+%26+b_%7B11%7D%5C%5Cb_%7B12%7D+%26+b_%7B13%7D+%26+b_%7B14%7D+%26+b_%7B15%7D%5Cend%7Barray%7D%5Cright%5D&fc=Black&im=jpg&fs=16&ff=modern&edit=)


with a similar one dimensional layout for the key:


A layout like this keeps the implementation much more straight forward.
This also means that the shift rows oration in reality shifts columns, and the
mix columns multiplies each row instead of each column. Yet i have kept to
original names of the functions instead of changing to shift columns and mix
rows, simply because this makes it easier to understand the steps in the
encryption and decryption process.

