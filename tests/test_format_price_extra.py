
from coingecko_pulse.formatters import format_pct, format_price

def test_format_price():
    assert format_price(1234.5) == "$1,234.50"

def test_format_pct():
    assert format_pct(1.5) == "+1.50%"
    assert format_pct(-2) == "-2.00%"
