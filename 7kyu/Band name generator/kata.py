# def band_name_generator(name):
#     if name[0] == name[-1]:
#         return (name[: len(name) - 1] + name).title()
#     return "The " + name.title()


def band_name_generator(name):
    if name[0] == name[-1]:
        return name.title() + name[1:]
    return "The " + name.title()
