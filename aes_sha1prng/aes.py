import base64
import hashlib
from Crypto.Cipher import AES as _AES


class AES:

    def __init__(self, key: str):
        """Init aes object used by encrypt or decrypt.
        AES/ECB/PKCS5Padding  same as aes in java default.
        """

        self.aes = _AES.new(self.get_sha1prng_key(key), _AES.MODE_ECB)


    @staticmethod
    def get_sha1prng_key(key: str) -> bytes:
        """encrypt key with SHA1PRNG.
        same as java AES crypto key generator SHA1PRNG.
        SecureRandom secureRandom = SecureRandom.getInstance("SHA1PRNG" );
        secureRandom.setSeed(decryptKey.getBytes());
        keygen.init(128, secureRandom);
        :param string key: original key.
        :return bytes: encrypt key with SHA1PRNG, 128 bits or 16 long bytes.
        """

        signature: bytes = hashlib.sha1(key.encode()).digest()
        signature: bytes = hashlib.sha1(signature).digest()
        return signature[:16]
    

    @staticmethod
    def padding(s: str) -> str:
        """Padding PKCS5"""

        pad_num: int = 16 - len(s) % 16
        return s + pad_num * chr(pad_num)


    @staticmethod
    def unpadding(s):
        """Unpadding PKCS5"""
        
        padding_num: int = ord(s[-1])
        return s[: -padding_num]

    
    def encrypt_to_bytes(self, content_str):
        """From string encrypt to bytes ciphertext.
        """

        content_bytes = self.padding(content_str).encode()
        ciphertext_bytes = self.aes.encrypt(content_bytes)
        return ciphertext_bytes
    

    def encrypt_to_base64(self, content_str):
        """From string encrypt to base64 ciphertext.
        """

        ciphertext_bytes = self.encrypt_to_bytes(content_str)
        ciphertext_bs64 = base64.b64encode(ciphertext_bytes).decode()
        return ciphertext_bs64


    def decrypt_from_bytes(self, ciphertext_bytes):
        """From bytes ciphertext decrypt to string.
        """
        
        content_bytes = self.aes.decrypt(ciphertext_bytes)
        content_str = self.unpadding(content_bytes.decode())
        return content_str


    def decrypt_from_base64(self, ciphertext_bs64):
        """From base64 ciphertext decrypt to string.
        """

        ciphertext_bytes = base64.b64decode(ciphertext_bs64)
        content_str = self.decrypt_from_bytes(ciphertext_bytes)
        return content_str


def encrypt_to_bytes(content_str, encrypt_key: str):
    """From string encrypt to bytes ciphertext.
    """

    aes: AES = AES(encrypt_key)
    ciphertext_bytes = aes.encrypt_to_bytes(content_str)
    return ciphertext_bytes


def encrypt_to_base64(content_str, encrypt_key: str) -> str:
    """From string encrypt to base64 ciphertext.
    """

    aes: AES = AES(encrypt_key)
    ciphertext_bs64 = aes.encrypt_to_base64(content_str)
    return ciphertext_bs64


def decrypt_from_bytes(ciphertext_bytes, decrypt_key: str) -> str:
    """From bytes ciphertext decrypt to string.
    """
    
    aes: AES = AES(decrypt_key)
    content_str = aes.decrypt_from_bytes(ciphertext_bytes)
    return content_str


def decrypt_from_base64(ciphertext_bs64, decrypt_key: str) -> str:
    """From base64 ciphertext decrypt to string.
    """

    aes: AES = AES(decrypt_key)
    content_str = aes.decrypt_from_base64(ciphertext_bs64)
    return content_str
