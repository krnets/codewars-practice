from dataclasses import dataclass


@dataclass
class User(object):
    #     def __init__(self, name, balance, checking_account):
    #         self.name = name
    #         self.balance = balance
    #         self.checking_account = checking_account
    name: str
    balance: int
    checking_account: bool

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"{self.name} does not enough money to withdraw")
        self.balance -= amount
        return self.get_balance_message()

    def get_balance_message(self):
        return f"{self.name} has {self.balance}."

    def check(self, other_user, amount):
        if not other_user.checking_account:
            raise ValueError(f"{other_user.name} does not have checking account")
        withdraw_message = other_user.withdraw(amount)
        add_cash_message = self.add_cash(amount)[:-1]
        return "{} and {}".format(add_cash_message, withdraw_message)

    def add_cash(self, money_to_add):
        self.balance += money_to_add
        return self.get_balance_message()
