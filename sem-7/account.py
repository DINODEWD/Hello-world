from errors import InvalidAccountType
from errors import InvalidAccountData

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT", "PAYMENT")
    ACC_VALUES = ("BGN", "USD", "EUR")

    def __init__(self, iban, currency, type) -> None:
        if type not in self.ACC_TYPES:
            raise InvalidAccountType()
        if type not in self.ACC_VALUES:
            raise InvalidAccountData()

        self.iban = iban
        self.currency = currency
        self.type = type
        self.balance = 0
