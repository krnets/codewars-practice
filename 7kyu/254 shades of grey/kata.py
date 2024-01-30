# def shades_of_grey(n):
#     return ["#" + 3 * ("{:02x}".format(i)) for i in range(1, min(255, n + 1))]


# def shades_of_grey(n):
#     return ["#" + 3 * ("{:02x}".format(i + 1)) for i in range(min(254, n))]


def shades_of_grey(n):
    return ["#%02x%02x%02x" % (i, i, i) for i in range(1, min(255, n + 1))]

