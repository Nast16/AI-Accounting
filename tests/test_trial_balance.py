from decimal import Decimal

from core.journal.journal_entry import JournalEntry
from core.journal.journal_line import JournalLine
from core.journal.journal_engine import JournalEngine

from core.ledger.ledger_engine import LedgerEngine
from core.ledger.posting import PostingEngine

from core.chart_of_accounts.account import Account
from core.chart_of_accounts.account_type import AccountType

from core.reporting.report_engine import ReportEngine

def test_trial_balance_balanced():
    entry = JournalEntry("INV-001")
    entry.add_line(JournalLine("1001", debit=Decimal("100000")))
    entry.add_line(JournalLine("4001", credit=Decimal("100000")))

    JournalEngine.post(entry)

    ledger = LedgerEngine()
    ledger.add_account(Account("1001", "Cash", AccountType.ASSET))
    ledger.add_account(Account("4001", "Revenue", AccountType.REVENUE))
    
    for le in PostingEngine.generate(entry):
        ledger.post(le)

    reports = ReportEngine.generate(ledger)

    tb = reports["trial_balance"]

    assert tb.is_balanced
