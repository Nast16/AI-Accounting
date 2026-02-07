def generate_journal_entry(tx):
    """
    Simple deterministic double entry logic for MVP
    Args:
        tx (dict): a transaction object read from CSV
    Returns:
        dict: journal entry with debit and credit accounts
    """
    journal = {}
    ttype = tx.get("transaction_type")
    pmeth = tx.get("payment_method")

    if ttype == "expense" and pmeth == "cash":
        journal = {"debit": "Beban", "credit": "Kas", "amount": tx["amount"]}
    elif ttype == "revenue" and pmeth == "cash":
        journal = {"debit": "Kas", "credit": "Pendapatan", "amount": tx["amount"]}
    else:
        # Placeholder logic
        journal = {"debit": None, "credit": None, "amount": tx["amount"]}

    return journal