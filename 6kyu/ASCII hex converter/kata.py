class Converter:
    @staticmethod
    def to_ascii(h):
        return "".join(chr(int(h[i : i + 2], 16)) for i in range(0, len(h), 2))

    @staticmethod
    def to_hex(s):
        return "".join(f"{ord(c):x}" for c in s)
