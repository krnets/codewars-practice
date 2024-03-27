# a = "GDRPLKgdrplkAEYOUIaeyoui"
# b = "AEYOUIaeyouiGDRPLKgdrplk"

# G = "GDRPLKgdrplk"
# A = "AEYOUIaeyoui"

# G = "GDRPLK"
# A = "AEYOUI"
# G += G.lower()
# A += A.lower()

key = "GA-DE-RY-PO-LU-KI".split("-")
G, A = [(s := "".join(x)) + s.lower() for x in zip(*key)]


# def encode(message):
#     return message.translate(str.maketrans(G + A, A + G))


# def decode(message):
#     return encode(message)

# encode = lambda message: message.translate(str.maketrans(G + A, A + G))
# decode = lambda message: encode(message)

encode = lambda m: m.translate(str.maketrans(G + A, A + G))
decode = encode
