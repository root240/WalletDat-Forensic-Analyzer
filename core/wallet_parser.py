import os

class WalletParser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        return {
            "file_size": os.path.getsize(self.path),
            "file_type": "Bitcoin Core wallet.dat",
            "encrypted": True
        }

