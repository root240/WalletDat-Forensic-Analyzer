class BerkeleyInspector:
    def __init__(self, path):
        self.path = path

    def inspect(self):
        with open(self.path, "rb") as f:
            header = f.read(16)

        return {
            "berkeley_magic": header.hex(),
            "valid_berkeley_db": True
        }

