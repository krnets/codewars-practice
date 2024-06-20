def travel(r, zipcode):
    if not zipcode:
        return ":/"
    house_numbers, street_town = [], []
    for address in r.split(","):
        parts = address.split(" ")
        if " ".join(parts[-2:]) == zipcode:
            house_numbers.append(parts[0])
            street_town.append(" ".join(parts[1:-2]))
    return "{}:{}/{}".format(zipcode, ",".join(street_town), ",".join(house_numbers))
