class Transaction:
    def __init__(self,account,amount,date,transfer) -> None:
        self.account=account
        self.amount=amount
        self.date=date
        self.transfer=transfer
