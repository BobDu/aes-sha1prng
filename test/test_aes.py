import unittest
from aes_sha1prng import encrypt_to_base64, decrypt_from_base64


class TestAES(unittest.TestCase):

    def test_encrypt_to_base64(self):
        assert encrypt_to_base64('0123456789', 'key') == '0SxwG6JwrDGJ7a0Vwv8Xow=='

    def test_decrypt_from_base64(self):
        assert decrypt_from_base64('0SxwG6JwrDGJ7a0Vwv8Xow==', 'key') == '0123456789'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAES)
    unittest.TextTestRunner(verbosity=2).run(suite)
