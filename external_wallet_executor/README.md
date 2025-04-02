# 🔐 External Wallet Executor

The External Wallet Executor handles cross-chain trade execution via externally controlled wallets, enabling flexible routing across EVM-compatible chains without centralized custody.

This module supports custom gas checks, signature handling, and fallback logic for safe execution via MetaMask or Gnosis-style wallets.

## 📂 Key Files

- `wallet_executor.py` — Core execution logic (buy/sell flows, tx handling)
- `signer.py` — Manages signing strategy and wallet session hooks
- `gas_checker.py` — Evaluates gas fees and chain viability before execution
- `config.py` — Wallet parameters, timeouts, thresholds
- `integration_hook.py` — Reference for calling executor from strategy loop
- `tests/` — Unit test harness (`test_wallet_executor.py`)

## 📄 References

- [External Wallet Executor — Technical Execution Guide] https://docs.google.com/document/d/1lPaBzaA8Df2Y1NHdWbzD6RDk5Wn73MDZoigvNnDwbug/edit?usp=sharing 
  _Execution flow, wallet injection, gas logic, and edge handling_

- [External Wallet Executor — Implementation Blueprint] https://docs.google.com/document/d/1gLXS64R-URU6ERgXESiIygnqt3r7d-LQENk2e8NzO88/edit?usp=sharing
  _Code structure, signing logic, and modular integration points_

---
