turkish_numbers = {
    0: "sıfır", 1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz",
    10: "on", 20: "yirmi", 30: "otuz", 40: "kırk", 50: "elli", 60: "altmış", 70: "yetmiş", 80: "seksen", 90: "doksan", }


def get_turkish_number(num):
    q, r = divmod(num, 10)
    return "%s %s" % (turkish_numbers[10 * q], turkish_numbers[r]) if q and r else turkish_numbers[10 * q] if q else turkish_numbers[num]