def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    months_needed = 0
    money_saved = 0

    depreciation_old_car = start_price_old
    depreciation_new_car = start_price_new

    variable_percent_loss = percent_loss_by_month / 100
    current_percent_loss_by_month = percent_loss_by_month

    while depreciation_old_car + money_saved < depreciation_new_car:
        depreciation_old_car -= depreciation_old_car * variable_percent_loss
        depreciation_new_car -= depreciation_new_car * variable_percent_loss

        money_saved += saving_per_month
        months_needed += 1

        if months_needed & 1:
            current_percent_loss_by_month += 0.5
            variable_percent_loss = current_percent_loss_by_month / 100

    money_leftover = round(depreciation_old_car + money_saved - depreciation_new_car)
    return [months_needed, money_leftover]
