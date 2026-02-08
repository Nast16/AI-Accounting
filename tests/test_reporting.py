from decimal import Decimal
from core.journal.journal_entry import JournalEntry
from core.journal.journal_line import JournalLine
from core.journal.journal_engine import JournalEngine

from core.ledger.account import Account
from core.ledger.posting import PostingEngine
from core.ledger.ledger_engine import LedgerEngine

from core.reporting.report_engine import ReportEngine

def test_financial_reports():
    entry = JournalEntry("INV-001")
    entry.add_line(JournalLine("1001", debit=Decimal("100000")))
    entry.add_line(JournalLine("4001", credit=Decimal("100000")))

    JournalEngine.post(entry)

    ledger = LedgerEngine()
    ledger.add_account(Account("1001", "Cash", "debit"))
    ledger.add_account(Account("4001", "Revenue", "credit"))

    for le in PostingEngine.generate(entry):
        ledger.post(le)

    reports = ReportEngine.generate(ledger)

    assert reports["income_statement"].profit == Decimal("100000")
    assert reports["balance_sheet"].assets == Decimal("100000")