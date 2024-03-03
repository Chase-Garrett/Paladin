import unittest
import AES_Sub_Bytes as a

class TestAES_Sub_Bytes(unittest.TestCase):

    def test_encrypt_hex(self):
        self.assertEqual(a.byteSub_encrypt(0xD62948DFA9B4DF52148FCDA234D878FC), 0xf6a5529ed38d9e00fa73bd3a1861bcb0)

    def test_decrypt_hex(self):
        self.assertEqual(a.byteSub_decrypt(0xf6a5529ed38d9e00fa73bd3a1861bcb0), 0xD62948DFA9B4DF52148FCDA234D878FC)



if __name__ == '__main__':
    unittest.main()