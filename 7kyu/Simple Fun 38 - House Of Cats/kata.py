def house_of_cats(legs):
    min = legs % 4 // 2
    max = legs // 2 + 1
    return [*range(min, max, 2)]
