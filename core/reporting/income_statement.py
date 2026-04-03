from decimal import Decimal
from core.ledger.account import Account

class IncomeStatement:
    def __init__(self, accounts: list[Account]):
        self.revenue = Decimal("0.00")
        self.expense = Decimal("0.00")

        for acc in accounts:
            if acc.code.startswith("4"):  # Revenue
                self.revenue += acc.balance
            elif acc.code.startswith("5"):  # Expense
                self.expense += acc.balance

    @property
    def profit(self) -> Decimal:
        return self.revenue - self.expense