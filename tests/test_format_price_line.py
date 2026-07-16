from coingecko_pulse.client import format_price_line

def test_format_price_line():
    assert "BTC" in format_price_line("btc", 100000.0)
    assert "n/a" in format_price_line("eth", None)
