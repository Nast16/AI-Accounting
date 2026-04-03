from datetime import date

class AccountingPeriod:
    def __init__(self, name: str, start_date: date, end_date: date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.closed = False

    def contains(self, check_date: date) -> bool:
        return self.start_date <= check_date <= self.end_date
    
    def close(self):
        self.closed = True