from decimal import Decimal

from core.chart_of_accounts.account import Account
from core.chart_of_accounts.account_type import AccountType

from core.ledger.ledger_engine import LedgerEngine

from core.closing.closing_engine import ClosingEngine

def test_closing_entry_generation():

    ledger = LedgerEngine()

    ledger.add_account(Account("1001","Cash",AccountType.ASSET))
    ledger.add_account(Account("4001","Revenue",AccountType.REVENUE))
    ledger.add_account(Account("5001","Expense",AccountType.EXPENSE))
    ledger.add_account(Account("3200","Retained Earnings",AccountType.EQUITY))

    ledger.accounts["4001"].balance = Decimal("100000")

    entry = ClosingEngine.generate_closing_entry(ledger, None)

    assert entry.total_debit() == entry.total_credit()