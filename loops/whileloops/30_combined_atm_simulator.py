"""
Task: Simple ATM Simulator
Concepts: while True, if-elif-else, break, accumulator

Simulate a basic ATM with a starting balance. Menu options: check
balance, deposit, withdraw, exit. Withdrawals can't exceed the
current balance. Keep looping until the user exits.
"""

available_balance = 2500

while True:
    print("=" * 10 , "#" * 5, "=" * 10)
    user_input = int(input("Please select the option from below menu:\n Press 1 : Check Balance\n Press 2: Deposit\n Press 3 : Withdarwals\n Press 4 : Exit\n Waiting for your input: "))
    print("\n")

    if user_input == 1:
        print(f"Available balance: ${available_balance}")
    elif user_input == 2:
        deposit_amt = int(input("Please enter the amt for deposit: "))
        available_balance += deposit_amt
        print("Deposit is sucessful.")
        print(f"New available Balance: {available_balance}")
    elif user_input == 3:
        print(f"your current balance: {available_balance}")
        Withdrawal_amt = int(input("Please enter the amt for Withdrawal: "))
        if Withdrawal_amt > available_balance:
            print("withdrawl amt can't exceed the current balance.")
            print("Please try again!")
        else:
            print(f"your withdrawal transction for amt ${Withdrawal_amt} is completed.\n")
            available_balance -= Withdrawal_amt
            print(f"your current balance: {available_balance}")
    elif user_input == 4:
        print("Exiting \n Thanks for choosing our back, see you again!")
        break
    else: 
        print("Invaild input, Please try again!")