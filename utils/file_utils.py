import os
import hashlib


class FileUtils:
    """
    Safe helper utilities for file-level analysis.
    """

    @staticmethod
    def file_exists(path: str) -> bool:
        return os.path.isfile(path)

    @staticmethod
    def file_size(path: str) -> int:
        return os.path.getsize(path)

    @staticmethod
    def read_bytes(path: str, limit: int = None) -> bytes:
        with open(path, "rb") as f:
            return f.read() if limit is None else f.read(limit)

    @staticmethod
    def sha256(path: str) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()

    @staticmethod
    def is_probably_binary(path: str) -> bool:
        data = FileUtils.read_bytes(path, 1024)
        return b"\x00" in data

    @staticmethod
    def null_byte_ratio(path: str) -> float:
        data = FileUtils.read_bytes(path)
        if not data:
            return 0.0
        return data.count(b"\x00") / len(data)

