from decimal import Decimal

from core.journal.journal_entry import JournalEntry
from core.journal.journal_line import JournalLine
from core.journal.journal_engine import JournalEngine

from core.chart_of_accounts.account_type import AccountType

class ClosingEngine:

    RETAINED_EARNINGS_CODE = "3200"

    @staticmethod
    def generate_closing_entry(ledger, period):

        entry = JournalEntry(f"CLOSING-{period}")

        retained_total = Decimal("0")

        for acc in ledger.accounts.values():

            if acc.type in (AccountType.REVENUE, AccountType.EXPENSE):

                balance = acc.balance

                if balance == 0:
                    continue

                if acc.type == AccountType.REVENUE:
                    entry.add_line(
                        JournalLine(acc.code, debit=balance)
                    )
                    retained_total += balance
                
                if acc.type == AccountType.EXPENSE:
                    entry.add_line(
                        JournalLine(acc.code, credit=balance)
                    )
                    retained_total -= balance
        
        if retained_total > 0:
            entry.add_line(
                JournalLine(
                    ClosingEngine.RETAINED_EARNINGS_CODE,
                    credit=retained_total
                )
            )
        else:
            entry.add_line(
                JournalLine(
                    ClosingEngine.RETAINED_EARNINGS_CODE,
                    debit=abs(retained_total)
                )
            )
        
        JournalEngine.post(entry)

        return entry