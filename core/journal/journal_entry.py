from datetime import datetime
from typing import List
from decimal import Decimal

from .journal_line import JournalLine

class JournalEntry:
    def __init__(self, reference: str, date: datetime | None = None):
        self.reference = reference
        self.date = date or datetime.now()
        self.lines: List[JournalLine] = []

    def add_line(self, line: JournalLine):
        self.lines.append(line)

    def total_debit(self) -> Decimal:
        return sum((line.debit for line in self.lines), Decimal("0.00"))

    def total_credit(self) -> Decimal:
        return sum((line.credit for line in self.lines), Decimal("0.00"))