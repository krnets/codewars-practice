def rotate(str_):
    return [str_[i:] + str_[:i] for i in range(1, len(str_) + 1)]
