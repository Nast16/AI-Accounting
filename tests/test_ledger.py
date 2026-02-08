from decimal import Decimal
from core.journal.journal_entry import JournalEntry
from core.journal.journal_line import JournalLine
from core.journal.journal_engine import JournalEngine

from core.ledger.account import Account
from core.ledger.posting import PostingEngine
from core.ledger.ledger_engine import LedgerEngine

def test_posting_to_ledger():
    entry = JournalEntry("INV-001")
    entry.add_line(JournalLine("1001", debit=Decimal("100000")))
    entry.add_line(JournalLine("4001", credit=Decimal("100000")))

    JournalEngine.post(entry)

    cash = Account("1001", "Cash", "debit")
    revenue = Account("4001", "Revenue", "credit")

    ledger = LedgerEngine()
    ledger.add_account(cash)
    ledger.add_account(revenue)

    ledger_entries = PostingEngine.generate(entry)
    for le in ledger_entries:
        ledger.post(le)

    assert cash.balance == Decimal("100000")
    assert revenue.balance == Decimal("100000")