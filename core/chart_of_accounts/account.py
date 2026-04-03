from decimal import Decimal
from .account_type import AccountType

class Account:
    def __init__(self, code: str, name: str, account_type: AccountType):
        self.code = code
        self.name = name
        self.type = account_type
        self.balance = Decimal("0.00")

    @property
    def normal_balance(self) -> str:
        return self.type.normal_balance
    
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
