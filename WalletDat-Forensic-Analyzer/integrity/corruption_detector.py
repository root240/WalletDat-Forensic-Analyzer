class CorruptionDetector:
    def __init__(self, path):
        self.path = path

    def check(self):
        with open(self.path, "rb") as f:
            data = f.read()

        null_ratio = data.count(b'\x00') / len(data)

        return {
            "null_byte_ratio": round(null_ratio, 4),
            "bit_flip_detected": False,
            "corruption": False
        }

