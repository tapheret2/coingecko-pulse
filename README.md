# coingecko-pulse

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Tiny **zero-API-key** crypto pulse CLI using [CoinGecko](https://www.coingecko.com/) public endpoints.

```bash
pip install -e .
cg-pulse top --n 15
cg-pulse price bitcoin ethereum solana
cg-pulse snapshot -o pulse.json
```

Built for data-science students who want a clean JSON feed without exchange API keys.

**Not financial advice.** Rate limits apply on free public API.

## License

MIT
