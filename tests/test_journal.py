from decimal import Decimal
from core.journal.journal_entry import JournalEntry
from core.journal.journal_line import JournalLine
from core.journal.journal_engine import JournalEngine

def test_valid_journal_entry():
    entry = JournalEntry(reference="INV-001")

    entry.add_line(JournalLine("1001", debit=Decimal("100000")))
    entry.add_line(JournalLine("4001", credit=Decimal("100000")))

    posted = JournalEngine.post(entry)

    assert posted.total_debit() == posted.total_credit()