# core/chart_of_accounts/predefined.py

from .account import Account
from .account_type import AccountType

def default_coa():
    return {
        "1001": Account("1001", "Cash", AccountType.ASSET),
        "1101": Account("1101", "Accounts Receivable", AccountType.ASSET),

        "2001": Account("2001", "Accounts Payable", AccountType.LIABILITY),

        "3001": Account("3001", "Owner Equity", AccountType.EQUITY),

        "4001": Account("4001", "Revenue", AccountType.REVENUE),

        "5001": Account("5001", "Expense", AccountType.EXPENSE),
    }
