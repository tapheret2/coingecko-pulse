from coingecko_pulse.client import format_usd

def test_format_usd():
    assert format_usd(None) == "n/a"
    assert "$1" in format_usd(1234.5, 1)
