from coingecko_pulse.client import format_mcap

def test_format_b():
    assert format_mcap(1.5e9) == "1.50B"

def test_format_m():
    assert format_mcap(2.5e6) == "2.50M"
