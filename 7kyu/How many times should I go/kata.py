# def how_many_times(annual_price, individual_price):
#     return annual_price // individual_price + (annual_price % individual_price != 0)


from math import ceil

def how_many_times(annual_price, individual_price):
    return ceil(annual_price / individual_price)
