from wallet_executor import WalletExecutor
from signer import Signer
from gas_checker import GasChecker
from config import CONFIG

executor = WalletExecutor(
    signer=Signer(CONFIG["private_key"]),
    gas_checker=GasChecker(CONFIG["gas_thresholds"])
)

mock_trade = type("Trade", (object,), {
    "token": "USDC",
    "chain": "Ethereum"
})()

result = executor.execute(mock_trade)
print(f"Execution result: {result}")
