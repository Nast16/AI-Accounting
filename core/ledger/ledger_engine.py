from typing import Dict
from decimal import Decimal
from .account import Account
from .ledger_entry import LedgerEntry

class LedgerEngine:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def add_account(self, account: Account):
        self.accounts[account.code] = account

    def post(self, entry: LedgerEntry):
        account = self.accounts.get(entry.account_code)
        if not account:
            raise ValueError(f"Account {entry.account_code} not found")

        if entry.debit > 0:
            account.apply_debit(entry.debit)

        if entry.credit > 0:
            account.apply_credit(entry.credit)