
from .enums import ValidationDecision
from .config import MAX_SLIPPAGE, MIN_SPREAD_MULTIPLIER

class LoopValidator:
    def __init__(self, buy_exchange, sell_exchange, token, amount):
        self.buy = buy_exchange
        self.sell = sell_exchange
        self.token = token
        self.amount = amount
        self.reasons = []

    def validate(self):
        self._check_token_presence()
        self._check_networks()
        self._check_routes()
        self._check_liquidity()
        self._check_spread_vs_costs()

        return self._decision(), self.reasons

    def _check_token_presence(self):
        if not self.buy.has_token(self.token):
            self.reasons.append("Token not listed on buy-side")
        if not self.sell.has_token(self.token):
            self.reasons.append("Token not listed on sell-side")

    def _check_networks(self):
        if self.token.network not in self.buy.supported_networks:
            self.reasons.append("Buy-side network unsupported")
        if self.token.network not in self.sell.supported_networks:
            self.reasons.append("Sell-side network unsupported")

    def _check_routes(self):
        if not self.buy.withdrawals_enabled(self.token.network):
            self.reasons.append("Withdrawals disabled on buy-side")
        if not self.sell.deposits_enabled(self.token.network):
            self.reasons.append("Deposits disabled on sell-side")

    def _check_liquidity(self):
        slippage = self.sell.estimate_slippage(self.token, self.amount)
        if slippage > MAX_SLIPPAGE:
            self.reasons.append(f"Excessive slippage on sell-side ({slippage}%)")

    def _check_spread_vs_costs(self):
        spread = self.sell.get_price(self.token) - self.buy.get_price(self.token)
        fees = self._estimate_total_fees()
        if spread < fees * MIN_SPREAD_MULTIPLIER:
            self.reasons.append("Spread insufficient after fees")

    def _estimate_total_fees(self):
        return (
            self.buy.estimate_gas_fee(self.token, self.amount) +
            self.sell.estimate_gas_fee(self.token, self.amount) +
            self.buy.estimate_exchange_fee(self.token, self.amount) +
            self.sell.estimate_exchange_fee(self.token, self.amount)
        )

    def _decision(self):
        if not self.reasons:
            return ValidationDecision.PROCEED
        elif len(self.reasons) == 1 and "Spread" in self.reasons[0]:
            return ValidationDecision.MANUAL_REVIEW
        else:
            return ValidationDecision.HALT
