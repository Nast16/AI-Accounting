from core.reporting.income_statement import IncomeStatement
from core.reporting.balance_sheet import BalanceSheet
from core.reporting.trial_balance import TrialBalance

class ReportEngine:
    @staticmethod
    def generate(ledger):
        accounts = list(ledger.accounts.values())

        return {
            "trial_balance": TrialBalance(accounts),
            "income_statement": IncomeStatement(accounts),
            "balance_sheet": BalanceSheet(accounts)
        }