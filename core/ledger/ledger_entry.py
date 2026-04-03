from decimal import Decimal
from datetime import datetime

class LedgerEntry:
    def __init__(
        self,
        account_code: str,
        debit: Decimal,
        credit: Decimal,
        reference: str,
        date: datetime
    ):
        self.account_code = account_code
        self.debit = debit
        self.credit = credit
        self.reference = reference
        self.date = date