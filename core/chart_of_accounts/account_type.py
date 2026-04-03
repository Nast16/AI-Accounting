from enum import Enum

class AccountType(Enum):
    ASSET = "debit"
    LIABILITY = "credit"
    EQUITY = "credit"
    REVENUE = "credit"
    EXPENSE = "debit"

    @property
    def normal_balance(self):
        return self.value