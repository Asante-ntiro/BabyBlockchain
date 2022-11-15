from Crypto.Hash import SHA
from Crypto.Hash import RIPEMD160
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512



class Signature:
    plaintext: str
    key: str
    hash_algorithm: str
    sign: str

    def signData(self, plaintext, key, hash_algorithm=Crypto.Hash.SHA512):
        signer = PKCS1_v1_5.new(RSA.importKey(key))
        hash_value = hash_algorithm.new(plaintext)
        return signer.sign(hash_value)

    def verifySignature(self, sign, plaintext, key, hash_algorithm=Crypto.Hash.SHA512):
        hash_value = hash_algorithm.new(plaintext)
        verifier = PKCS1_v1_5.new(RSA.importKey(key))
        return verifier.verify(hash_value, sign)

    def getSignature(self):
        private_key = open("private_key.pem", "rb")
        message = 'Signature RSA'
        signature = Signature().signData(message.encode(encoding='utf-8'), private_key.read())
        return signature

    def printVerifySignature(self):
        public_key = open("public_key.pem", "rb")
        message1 = 'Signature RSA'
        print(Signature().verifySignature(Signature().getSignature(), message1.encode('utf-8'), public_key.read()))

    def printSignature(self):
        private_key = open("private_key.pem", "rb")
        message = 'Signature RSA'
        signature = Signature().signData(message.encode(encoding='utf-8'), private_key.read())
        print(signature)

