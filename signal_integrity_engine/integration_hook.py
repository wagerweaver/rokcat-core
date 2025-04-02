from signal_filter import SignalFilter
from signal_scoring import SignalScorer
from token_watchlist import TRUSTED_TOKENS
from config import CONFIG

scorer = SignalScorer(TRUSTED_TOKENS, CONFIG["max_spread"])
filter_engine = SignalFilter(CONFIG, scorer)

mock_signal = {
    "token": "SHIB",
    "spread": 2.4,
    "depth": 0.4
}

result = filter_engine.validate(mock_signal)
print("✅ Valid" if result else "❌ Rejected")
