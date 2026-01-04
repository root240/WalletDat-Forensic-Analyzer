import math

class EntropyProfiler:
    def __init__(self, path):
        self.path = path

    def profile(self):
        with open(self.path, "rb") as f:
            data = f.read()

        freq = [0]*256
        for b in data:
            freq[b] += 1

        entropy = 0.0
        for f in freq:
            if f > 0:
                p = f / len(data)
                entropy -= p * math.log2(p)

        return {
            "shannon_entropy": round(entropy, 4),
            "randomness": "High"
        }

