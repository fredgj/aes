import unittest

from aes import encrypt, decrypt, KeySizeError, BlockSizeError


class AESTest(unittest.TestCase):
    def test_128bit_key_encrypt(self):
        key = '2b7e151628aed2a6abf7158809cf4f3c'
        block = '6bc1bee22e409f96e93d7e117393172a'

        encrypted = encrypt(block,key, _format='x')
        expected = '3ad77bb40d7a3660a89ecaf32466ef97'

        self.assertEqual(encrypted, expected)

    def test_128bit_key_decrypt(self):
        key = '2b7e151628aed2a6abf7158809cf4f3c'
        block = '3ad77bb40d7a3660a89ecaf32466ef97'

        decrypted = decrypt(block,key, _format='x')
        expected = '6bc1bee22e409f96e93d7e117393172a'

        self.assertEqual(decrypted, expected)

    def test_192bit_key_encrypt(self):
        key = '8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b'
        block = '6bc1bee22e409f96e93d7e117393172a'

        encrypted = encrypt(block,key, _format='x')
        expected = 'bd334f1d6e45f25ff712a214571fa5cc'

        self.assertEqual(encrypted, expected)

    def test_192bit_key_decrypt(self):
        key = '8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b'
        block = 'bd334f1d6e45f25ff712a214571fa5cc'

        decrypted = decrypt(block,key, _format='x')
        expected = '6bc1bee22e409f96e93d7e117393172a'

        self.assertEqual(decrypted, expected)

    def test_256bit_key_encrypt(self):
        key = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4'
        block = '6bc1bee22e409f96e93d7e117393172a'

        encrypted = encrypt(block,key, _format='x')
        expected = 'f3eed1bdb5d2a03c064b5a7e3db181f8'

        self.assertEqual(encrypted, expected)

    def test_256bit_key_decrypt(self):
        key = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4'
        block = 'f3eed1bdb5d2a03c064b5a7e3db181f8'

        decrypted = decrypt(block,key, _format='x')
        expected = '6bc1bee22e409f96e93d7e117393172a'

        self.assertEqual(decrypted, expected)

    def test_keyerror_encrypt(self):
        key = '1'*17
        block = '1'*16
        self.assertRaises(KeySizeError, encrypt, block, key)

    def test_keyerror_decrypt(self):
        key = '1'*17
        block = '1'*16
        self.assertRaises(KeySizeError, decrypt, block, key)

    def test_blockerror_encrypt(self):
        key =   '1'*16
        block = '1'*17
        self.assertRaises(BlockSizeError, encrypt, block, key)

    def test_blockerror_decrypt(self):
        key =   '1'*16
        block = '1'*17
        self.assertRaises(BlockSizeError, decrypt, block, key)


if __name__ == '__main__':
    unittest.main()

