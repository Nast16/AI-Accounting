from .journal_entry import JournalEntry
from .validator import JournalValidator

class JournalEngine:
    @staticmethod
    def post(entry: JournalEntry):
        JournalValidator.validate(entry)
        return entry