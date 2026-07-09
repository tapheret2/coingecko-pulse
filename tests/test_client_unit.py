from coingecko_pulse.client import CoinGecko


def test_client_constructs():
    c = CoinGecko()
    c.close()
