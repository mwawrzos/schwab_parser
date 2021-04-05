
class EntryBase:
    def __init__(self, *fields):
        self.date, \
        self.action, \
        self.symbol, \
        self.description, \
        self.quantity, \
        self.fees, \
        self.disbursment_election, \
        self.amount = fields

class ESPP_DepositEntry:
    def __init__(self, base, *fields):
        self.base = base
        self.purchase_date, \
        self.purchase_price, \
        self.subscription_date, \
        self.subscription_fmv, \
        self.purchase_fmv = fields
