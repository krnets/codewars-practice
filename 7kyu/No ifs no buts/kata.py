def no_ifs_no_buts(a, b):
    eq_sm_gr = ("equal to", "smaller than", "greater than")[a < b or (not a == b) + (a > b)]
    return "{} is {} {}".format(a, eq_sm_gr, b)
