# luhn, all, any
# import os.path.walk, os.path.join


def luhn_check(credit_card: str) -> bool:
    """
    test credit cards
    https://developer.paypal.com/docs/payflow/payflow-pro/payflow-pro-testing/#credit-card-numbers-for-testing
    https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D1%83%D0%BD%D0%B0
    """
    return True


# +15
assert luhn_check('4111111111111111') is True
assert luhn_check('4111111111111112') is False
assert luhn_check('   4111111111111111   ') is True
assert luhn_check('4111 1111 1111 1111') is True
assert luhn_check('  4111 1111 1111 1111  ') is True
assert luhn_check('411111111111111a') is False
