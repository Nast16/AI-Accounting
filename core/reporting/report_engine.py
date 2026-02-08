from core.reporting.income_statement import IncomeStatement
from core.reporting.balance_sheet import BalanceSheet

class ReportEngine:
    @staticmethod
    def generate(ledger):
        accounts = list(ledger.accounts.values())

        return {
            "income_statement": IncomeStatement(accounts),
            "balance_sheet": BalanceSheet(accounts)
        }