class ColdExitEngine:
    def __init__(self, config, notifier):
        self.config = config
        self.notifier = notifier

    def evaluate_trade(self, trade_context):
        if Triggers.timeout(trade_context):
            return self._rollback(trade_context, reason="timeout")
        if Triggers.liquidity_drain(trade_context):
            return self._rollback(trade_context, reason="liquidity")
        return "proceed"

    def _rollback(self, trade_context, reason):
        action = self._select_action(trade_context)
        self.notifier.notify(f"Rollback triggered ({reason}) — {action}")
        return action

    def _select_action(self, context):
        if context.can_resell:
            return "resell_on_entry_exchange"
        elif context.can_bridge_out:
            return "bridge_to_safe_wallet"
        else:
            return "pause_and_hold"
