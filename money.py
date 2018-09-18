class CurrencyExchange:
    _rates = {}

    def add_rate(
        self, from_currency, to_currency, rate
    ):
        self._rates[from_currency] = {}
        self._rates[from_currency][to_currency] = rate

        self._rates[to_currency] = {}
        self._rates[to_currency][from_currency] = 1 / rate

    def convert(self, other, to_currency):
        rate = self._rates[to_currency][other.currency]
        return Money(other.amount // rate, to_currency)


class Money:
    def __init__(
        self, amount, currency, currency_exchange=None
    ):
        self.amount = amount
        self.currency = currency
        self.currency_exchange = currency_exchange

    def __add__(self, other):
        addend = other
        if self.currency_exchange is not None:
            addend = self.currency_exchange.convert(
                other, self.currency
            )

        return Money(
            self.amount + addend.amount, self.currency
        )

    def __eq__(self, other):
        if not self.currency == other.currency:
            return False
        return self.amount == other.amount

    def __mul__(self, multiplier):
        return Money(
            self.amount * multiplier, self.currency
        )

    def __repr__(self):
        return '{} {}'.format(
            self.currency, self.amount
        )
