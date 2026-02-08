from .journal_entry import JournalEntry

class JournalValidationError(Exception):
    pass


class JournalValidator:
    @staticmethod
    def validate(entry: JournalEntry):
        if len(entry.lines) < 2:
            raise JournalValidationError("Journal entry must have at least 2 lines")

        for line in entry.lines:
            if line.debit > 0 and line.credit > 0:
                raise JournalValidationError(
                    "A journal line cannot have both debit and credit"
                )

        if entry.total_debit() != entry.total_credit():
            raise JournalValidationError(
                "Total debit must equal total credit"
            )