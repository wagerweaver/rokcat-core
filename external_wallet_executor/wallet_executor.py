class WalletExecutor:
    def __init__(self, signer, gas_checker):
        self.signer = signer
        self.gas_checker = gas_checker

    def execute(self, trade):
        if not self.gas_checker.is_ready(trade.chain):
            return "abort_due_to_gas_shortage"
        tx = self.signer.sign(trade)
        return self._broadcast(tx)

    def _broadcast(self, tx):
        print(f"Broadcasting TX: {tx}")
        return "broadcast_success"
