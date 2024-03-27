from collections import Counter

class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        freq = Counter(''.join(map(str, integers_list)))
        return [(x, freq[str(x)]) for x in digits_list]