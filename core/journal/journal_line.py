from dataclasses import dataclass
from decimal import Decimal

@dataclass
class JournalLine:
    account_code: str
    debit: Decimal = Decimal("0.00")
    credit: Decimal = Decimal("0.00")

    def is_debit(self) -> bool:
        return self.debit > 0

    def is_credit(self) -> bool:
        return self.credit > 0