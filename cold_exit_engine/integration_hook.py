from cold_exit_engine import ColdExitEngine
from rollback_config import ROLLBACK_CONFIG
from notifier import Notifier

engine = ColdExitEngine(ROLLBACK_CONFIG, Notifier(webhook=None))

trade_context = {...}  # filled in by execution monitor
decision = engine.evaluate_trade(trade_context)
