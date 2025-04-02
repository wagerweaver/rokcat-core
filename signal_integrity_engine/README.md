# 🔎 Signal Integrity Engine

The Signal Integrity Engine filters and scores raw arbitrage signals before execution — protecting ROKCAT from false positives, low-liquidity traps, or high-risk assets.

It combines configurable rules, token watchlists, and scoring logic to dynamically suppress or rerank unreliable opportunities.

## 📂 Key Files

- `signal_filter.py` — Primary filter logic for false signal suppression
- `signal_scoring.py` — Assigns integrity score based on liquidity, volatility, spread quality
- `token_watchlist.py` — Excludelist and tier list for known risky tokens
- `config.py` — Thresholds for filtering and scoring
- `integration_hook.py` — Reference for upstream scanner integration
- `tests/` — Unit test harness (`test_signal_integrity.py`)

## 📄 References

- [Signal Integrity Engine — Technical Execution Guide] https://docs.google.com/document/d/1c1xCVJ9LNCGFC9tiv_A-LzOwko7e3n69POVPZVh93VE/edit?usp=sharing 
  _Filtering criteria, scoring strategy, and token quality control_

- [Signal Integrity Engine — Implementation Blueprint] https://docs.google.com/document/d/1gmqg5-CRY-5Ngot1xMpc_Vur8lLc-xtE2UA4wfjwYB8/edit?usp=sharing
  _Code components, usage examples, and test outline_

---
