import deal
from decimal import Decimal


@deal.inv(lambda obj: obj.balance >= Decimal(0))
@deal.inv(lambda obj: isinstance(obj.balance, Decimal))
class BankAccount:
    def __init__(self, balance=Decimal(0)):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счёт."

    @deal.pre(lambda self, amount: amount > Decimal(0))
    def withdraw(self, amount):
        self.balance -= amount
        return f"{amount} средств успешно сняты с счёта."

    def check_balance(self):
        return f"Баланс счёта: {self.balance}"


def test_bank():
    bank = BankAccount(Decimal('-1'))
    bank = BankAccount(-1)

    bank = BankAccount(Decimal('0.3'))
    bank.withdraw(Decimal('0.2'))
    assert bank.balance == Decimal('0.1')


if __name__ == '__main__':
    test_bank()
