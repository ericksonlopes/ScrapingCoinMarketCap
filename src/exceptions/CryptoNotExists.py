class CryptoNotExists(Exception):
    def __init__(self, crypto):
        self.crypto = crypto

    def __str__(self):
        return "Crypto {} not exists".format(self.crypto)