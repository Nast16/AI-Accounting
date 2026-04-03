from datetime import date
from .period import AccountingPeriod

class PeriodManager:
    def __init__(self):
        self.periods: list[AccountingPeriod] = []

    def add_period(self, period: AccountingPeriod):
        self.periods.append(period)

    def find_period(self, check_date: date) -> AccountingPeriod:
        for period in self.periods:
            if period.contains(check_date):
                return period
        
        raise ValueError("No accounting period found for date.")