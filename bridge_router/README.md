# 🌉 Bridge Router

The Bridge Router powers intelligent cross-chain bridging for arbitrage execution. It integrates with external providers like Squid, Stargate, and Wormhole, dynamically selecting the optimal route based on latency, fees, and reliability.

Includes fallback logic, quote scoring, and a plug-in interface to external executors.

## 📂 Key Files

- `bridge_router.py` — Core routing engine
- `bridge_providers.py` — Unified API wrapper for bridge services (Squid, Stargate, etc.)
- `bridge_config.py` — Configurable routing thresholds
- `latency_tracker.py` — Measures and stores live latency data per provider
- `quote_engine.py` — Scoring engine for ranking quotes and assigning fallback order
- `integration_hook.py` — Sample integration with broader arbitrage system
- `sample_quotes.json` — Example output from bridge quote engine
- `tests/` — Unit test harness (`test_bridge_router.py`)

## 📄 References

- [Bridge Router — Technical Execution Guide] https://docs.google.com/document/d/1-IoqoAabsL16YztqPEF6sDMY-mt5D-PiUh7BVdQOUGM/edit?usp=sharing 
  _Explains fallback logic, provider selection, and integration layers_

- [Bridge Router — Implementation Blueprint] https://docs.google.com/document/d/1eEQLLYAz4AafGhn19G43WZVy0TGU6pJIjxhERerv-8c/edit?usp=sharing
  _All routing modules, quote evaluation logic, and test structure_

---
