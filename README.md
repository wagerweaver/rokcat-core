# 🧠 ROKCAT Core

This repository contains the **core logic modules** powering the ROKCAT arbitrage system — a semi-automated, capital-efficient trading engine designed to identify and execute cross-exchange and cross-chain arbitrage opportunities in real time.

---

## 📦 Current Modules

### `loop_validator/`

The `loop_validator` module ensures the **entire arbitrage loop is valid and executable** before any capital is deployed. It prevents partial trade paths and broken exit routes by validating:

- Token availability on both buy/sell exchanges
- Network compatibility
- Deposit/withdrawal status
- Liquidity depth and slippage
- Spread coverage relative to total fees

🔒 **Decision outputs:** `PROCEED`, `HALT`, or `MANUAL_REVIEW`  
🔎 Built with modular, testable classes and integrated enums/configs

---

## 🧪 Testing

Basic unit tests are included in `loop_validator/tests/`.  
Future test cases will cover:

- Simulated exchange and token mocks  
- Loop failures (withdrawal disabled, token missing, etc.)  
- Edge-case validation logic

---

## 📚 Future Modules (Planned)

- `bridge_router/` – Intelligent bridging engine with fallback and quote scoring  
- `discount_buy/` – Delayed-exit holding logic for undervalued token pickups  
- `execution_orchestrator/` – Unified execution layer for buy, transfer, and sell routes

---

## 🤝 Contributing

This repository is currently private and in early-stage development.  
To request access or collaborate, please contact [Your Name] or open a private issue once permissions are granted.

---

## 🧰 Requirements (Planned)

- Python 3.10+
- Virtualenv or Poetry (for environment isolation)
- CI-ready structure for validator + bridging modules

---

## 📄 License

Private and unlicensed until further notice.

---
