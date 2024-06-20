# def stock_list(list_of_art, list_of_cat):
#     if not list_of_art or not list_of_cat:
#         return ""

#     categories = {}

#     for cat in list_of_cat:
#         categories[cat] = 0

#         for art in list_of_art:
#             book_code, n = art.split()

#             if book_code.startswith(cat):
#                 categories[cat] += int(n)

#     return " - ".join(f"({k} : {v})" for k, v in categories.items())


def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""
    categories = dict.fromkeys(list_of_cat, 0)

    for cat in list_of_cat:
        for art in list_of_art:
            book_code, n = art.split()
            if book_code.startswith(cat):
                categories[cat] += int(n)

    return " - ".join("({} : {})".format(k, v) for k, v in categories.items())
