from decimal import Decimal
from core.chart_of_accounts.account import Account

class TrialBalanceRow:
    def __init__(self, account_code, account_name, debit, credit):
        self.account_code = account_code
        self.account_name = account_name
        self.debit = debit
        self.credit = credit

class TrialBalance:
    def __init__(self, accounts: list[Account]):
        self.rows: list[TrialBalanceRow] = []
        self.total_debit = Decimal("0.00")
        self.total_credit = Decimal("0.00")

        for acc in accounts:
            if acc.normal_balance == "debit":
                debit = acc.balance if acc.balance > 0 else Decimal("0.00")
                credit = Decimal("0.00")
            else:
                debit = Decimal("0.00")
                credit = acc.balance if acc.balance > 0 else Decimal("0.00")

            self.rows.append(
                TrialBalanceRow(
                    acc.code,
                    acc.name,
                    debit,
                    credit
                )
            )

            self.total_debit += debit
            self.total_credit += credit

    @property
    def is_balanced(self):
        return self.total_debit == self.total_credit
    
    