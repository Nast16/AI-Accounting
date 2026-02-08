from typing import List
from core.journal.journal_entry import JournalEntry
from .ledger_entry import LedgerEntry

class PostingEngine:
    @staticmethod
    def generate(entry: JournalEntry) -> List[LedgerEntry]:
        ledger_entries = []

        for line in entry.lines:
            ledger_entries.append(
                LedgerEntry(
                    account_code=line.account_code,
                    debit=line.debit,
                    credit=line.credit,
                    reference=entry.reference,
                    date=entry.date
                )
            )

        return ledger_entries