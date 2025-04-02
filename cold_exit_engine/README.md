# 🧊 Cold Exit Engine

The Cold Exit Engine serves as ROKCAT’s capital defense layer — designed to gracefully unwind broken arbitrage loops when conditions shift mid-execution. It monitors real-time risk signals and safely routes capital out of compromised trades using a structured rollback framework.

Supports actions like re-selling, neutral bridging, partial exits, or hold-and-monitor fallback states.

## 📂 Key Files

- `cold_exit_engine.py` — Core rollback logic and fallback executor
- `rollback_config.py` — Threshold settings for latency, slippage, liquidity drops
- `triggers.py` — Monitors execution health and defines failure conditions
- `notifier.py` — Optional webhook-based human alert system
- `integration_hook.py` — Reference logic for connecting rollback to the core execution engine
- `tests/` — Unit test harness (`test_cold_exit.py`)

## 📄 References

- [Cold Exit Engine — Technical Execution Guide] https://docs.google.com/document/d/1ILSEi8LNDLT-b8nV2dz89AGHfnFWpV7BbN_wffdab6E/edit?usp=sharing
  _Trigger matrix, decision flow, capital defense rationale_

- [Cold Exit Engine — Implementation Blueprint] https://docs.google.com/document/d/1TXp5HiyJm8WkdwZU7b5MzMgNb9aL6YGnxm7o2jexvTk/edit?usp=sharing
  _File structure, decision engine logic, and rollback paths_

---
