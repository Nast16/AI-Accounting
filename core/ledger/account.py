from decimal import Decimal

class Account:
    def __init__(self, code: str, name: str, normal_balance: str):
        self.code = code
        self.name = name
        self.normal_balance = normal_balance  # "debit" / "credit"
        self.balance = Decimal("0.00")

    def apply_debit(self, amount: Decimal):
        if self.normal_balance == "debit":
            self.balance += amount
        else:
            self.balance -= amount

    def apply_credit(self, amount: Decimal):
        if self.normal_balance == "credit":
            self.balance += amount
        else:
            self.balance -= amount