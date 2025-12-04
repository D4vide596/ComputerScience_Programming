if __name__ == '__main__':
    account_balance = 10000
    print(f"Initial account balance: CHF {account_balance}")
    operation = int(input("Perform an operation: (+ = Deposit / - = Withdrawal) "))
    print(f"\nYou moved CHF {operation}, your new balance is CHF {account_balance + operation}")