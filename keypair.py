from Crypto.Hash import SHA
from Crypto.Hash import RIPEMD160
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512


class KeyPair:
    private_key: str
    public_key: str

    def genKeyPair(self):
        key = RSA.generate(2048)
        self.private_key = key.export_key()
        file_out = open("private_key.pem", "wb")
        file_out.write(self.private_key)
        file_out.close()

        self.public_key = key.publickey().export_key()
        file_out = open("public_key.pem", "wb")
        file_out.write(self.public_key)
        file_out.close()

    def printKeyPair(self):
        self.private_key = open("private_key.pem", "rb")
        self.public_key = open("public_key.pem", "rb")
        print(self.private_key.read())
        print(self.public_key.read())

