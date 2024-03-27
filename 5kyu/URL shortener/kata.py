from itertools import product, chain
from string import ascii_lowercase


class Url_shortener:
    def __init__(self) -> None:
        self.db = {}
        self.keys = chain.from_iterable(product(ascii_lowercase, repeat=k) for k in range(1, 5))

    def shorten(self, long_url: str) -> str:
        if long_url in self.db:
            return self.db[long_url]

        self.short_url = "short.ly/" + "".join(next(self.keys))
        self.db[long_url] = self.short_url
        self.db[self.short_url] = long_url

        return self.short_url

    def redirect(self, short_url: str) -> str:
        return self.db.get(short_url, "")
