def owned_cat_and_dog(cat_years, dog_years):
    owned_cat = 0 if cat_years < 15 else 1 if cat_years < 24 else 2 + (cat_years - 24) // 4
    owned_dog = 0 if dog_years < 15 else 1 if dog_years < 24 else 2 + (dog_years - 24) // 5
    return [owned_cat, owned_dog]
