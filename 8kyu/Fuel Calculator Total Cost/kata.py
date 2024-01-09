"""Purchases of 2 or more litres get a discount of 5 cents per litre, 
    purchases of 4 or more litres get a discount of 10 cents per litre, 
    and so on every two litres, 
    up to a maximum discount of 25 cents per litre. 
    But total discount per litre cannot be more than 25 cents. 
    Return the total cost rounded to 2 decimal places.  """


# def fuel_price(litres, price_per_litre):
#     ans = 0

#     if litres >= 10:
#         ans = litres * (price_per_litre - 0.25)
#     elif litres >= 8:
#         ans = litres * (price_per_litre - 0.2)
#     elif litres >= 6:
#         ans = litres * (price_per_litre - 0.15)
#     elif litres >= 4:
#         ans = litres * (price_per_litre - 0.1)
#     elif litres >= 2:
#         ans = litres * (price_per_litre - 0.05)
#     else:
#         ans = litres * price_per_litre

#     return round(ans, 2)

# def fuel_price(litres, price_per_litre):
#     return litres * max(price_per_litre - 0.05 * (litres // 2), price_per_litre - 0.25)

def fuel_price(litres, price_per_litre):
    ans = litres * (price_per_litre - min(0.05 * (litres // 2), 0.25))
    return round(ans, 2)
