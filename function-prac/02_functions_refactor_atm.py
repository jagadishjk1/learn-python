
# available balance function
def check_balance(available_balance = 2500):
    print(available_balance)

#deposit function
def deposit():
    deposit_amt = int(input("Please enter the amt for deposit: "))
    available_balance = usr_balance + deposit_amt
    print("Deposit is sucessful.")
    print(f"New available Balance: {available_balance}")
    return available_balance

#withdrawal function
def Withdrawal_amt():
        print(f"your current balance: {usr_balance}")
        Withdrawal_amt = int(input("Please enter the amt for Withdrawal: "))
        if Withdrawal_amt > usr_balance:
            print("withdrawl amt can't exceed the current balance.")
            print("Please try again!")
        else:
            print(f"your withdrawal transction for amt ${Withdrawal_amt} is completed.\n")
            available_balance = usr_balance - Withdrawal_amt
            return available_balance
        



# available_balance = 2500
usr_balance = 2000

#ATM while loop:
while True:
    print("=" * 10 , "#" * 5, "=" * 10)
    user_input = int(input("Please select the option from below menu:\n Press 1 : Check Balance\n Press 2: Deposit\n Press 3 : Withdarwals\n Press 4 : Exit\n Waiting for your input: "))
    print("\n")

    if user_input == 1:
        check_balance(usr_balance)
    elif user_input == 2:   #deposit block
        usr_deposit_balance = deposit()
        usr_balance = usr_deposit_balance            
        print(f"New available Balance: {usr_deposit_balance}")
    elif user_input == 3: # withdrawal
        usr_withdrawal_balance = Withdrawal_amt()
        usr_balance = usr_withdrawal_balance
        print(f"your current balance: {usr_withdrawal_balance}")
    elif user_input == 4:
        print("Exiting \n Thanks for choosing our back, see you again!")
        break
    else: 
        print("Invaild input, Please try again!")




