def expanded_form(num):
    integer, decimal = str(num).split(".")
    int_parts = " + ".join(x.ljust(len(integer) - i, "0") for i, x in enumerate(integer) if x != "0")
    dec_parts = " + ".join((x + "/1").ljust(i + 4, "0") for i, x in enumerate(decimal) if x != "0")
    return int_parts if not dec_parts else dec_parts if not int_parts else int_parts + " + " + dec_parts
