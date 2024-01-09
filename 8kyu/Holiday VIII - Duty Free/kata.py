# def duty_free(price, discount, holiday_cost):
#     return holiday_cost // (price * discount / 100)

def duty_free(price, discount, holiday_cost):
    saving_per_bottle = price * discount / 100
    return holiday_cost // saving_per_bottle