def get_new_notes(salary, bills):
    disposable_income = salary - sum(bills)
    return max(0, disposable_income // 5)