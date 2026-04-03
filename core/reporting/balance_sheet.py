from decimal import Decimal
from core.ledger.account import Account

class BalanceSheet:
    def __init__(self, accounts: list[Account]):
        self.assets = Decimal("0.00")
        self.liabilities = Decimal("0.00")
        self.equity = Decimal("0.00")

        for acc in accounts:
            if acc.code.startswith("1"):      # Asset
                self.assets += acc.balance
            elif acc.code.startswith("2"):    # Liability
                self.liabilities += acc.balance
            elif acc.code.startswith("3"):    # Equity
                self.equity += acc.balance

    @property
    def is_balanced(self) -> bool:
        return self.assets == (self.liabilities + self.equity)