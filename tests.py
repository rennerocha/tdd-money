from money import CurrencyExchange, Money


def test_equality():
    assert Money(4, 'USD') == Money(4, 'USD')
    assert Money(4, 'USD') != Money(3, 'USD')
    assert Money(4, 'BRL') != Money(4, 'USD')
    assert Money(4, 'USD') != Money(4, 'BRL')


def test_multiplication():
    assert Money(2, 'USD') * 2 == Money(4, 'USD')


def test_addition():
    money_sum = Money(2, 'USD') + Money(2, 'USD')
    assert money_sum == Money(4, 'USD')


def test_addition_between_currencies():
    currency_exchange = CurrencyExchange()
    currency_exchange.add_rate('USD', 'BRL', 4)

    one_dollar = Money(1, 'USD', currency_exchange)
    four_reais = Money(4, 'BRL', currency_exchange)

    money_sum = one_dollar + four_reais
    assert money_sum == Money(2, 'USD')

    money_sum = four_reais + one_dollar
    assert money_sum == Money(8, 'BRL')


def test_convert_currencies():
    currency_exchange = CurrencyExchange()
    currency_exchange.add_rate('USD', 'BRL', 4)

    four_reais = Money(4, 'BRL', currency_exchange)
    converted = currency_exchange.convert(four_reais, 'USD')

    assert converted == Money(1, 'USD')


def test_convert_currencies_backref():
    currency_exchange = CurrencyExchange()
    currency_exchange.add_rate('USD', 'BRL', 4)

    one_dolar = Money(1, 'USD', currency_exchange)
    converted = currency_exchange.convert(one_dolar, 'BRL')

    assert converted == Money(4, 'BRL')