
from validator import LoopValidator
from enums import ValidationDecision

def validate_and_dispatch(buy_ex, sell_ex, token, amount):
    decision, reasons = LoopValidator(buy_ex, sell_ex, token, amount).validate()
    if decision == ValidationDecision.HALT:
        print("Aborting trade due to failed validation:")
        for r in reasons:
            print(f" - {r}")
        return False
    elif decision == ValidationDecision.MANUAL_REVIEW:
        print("Trade flagged for manual review:")
        for r in reasons:
            print(f" - {r}")
        # Notify ops or log
        return False
    else:
        print("Trade validated. Proceeding to execution.")
        return True
