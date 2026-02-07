from src.core.journal_engine import generate_journal_entry

def test_expense_cash():
    tx = {"transaction_type": "expense", "payment_method": "cash", "amount": 500000}
    entry = generate_journal_entry(tx)
    assert entry["debit"] == "Beban"
    assert entry["credit"] == "Kas"