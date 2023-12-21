def spoonerize(words):
    fst, snd = words.split()
    return snd[0] + fst[1:] + " " + fst[0] + snd[1:]
