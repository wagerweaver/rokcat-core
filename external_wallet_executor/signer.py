class Signer:
    def __init__(self, private_key):
        self.key = private_key

    def sign(self, trade):
        return f"signed_tx_for_{trade.token}_on_{trade.chain}"
