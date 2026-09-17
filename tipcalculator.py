# Ask for a bill amount and number of people. Ask if they want a 10%, 15%, or 20% tip (as input choice). 
# Calculate and print the total bill and amount per person, using an f-string with 2 decimal places (f"{value:.2f}").

# Start with Task 5 — think carefully about the order of your if-elif checks, 
# since order matters here (e.g., check invalid ranges first, or go from highest score downward). Paste your code when ready.

bill_amount = float(input("Please enter your bill amount: $"))
print (''' 
For 10%, Enter A
For 15%, Enter B
For 20%, Enter C
''')
tip_percent = input("Please enter the percentage you want to tip(A, B, C): ")
number_of_people = int(input("Please enter the number of people: "))
validate_tip = tip_percent.lower().startswith(('a','b','c'))
if validate_tip:
    if tip_percent.lower() == 'a':
        print(f"bill amt: ${bill_amount}")
        print(f"Tip amt: 10%")
        total_amt = (bill_amount * 0.10) + bill_amount 
        amount_per_person = total_amt / number_of_people
        print(f"Amount per person: ${amount_per_person:.2f}")
        print(f"Total bill amt: ${total_amt:.2f}")
    elif tip_percent.lower() == 'b':
        print(f"bill amt: ${bill_amount}")
        print(f"Tip amt: 15%")
        total_amt = (bill_amount * 0.15) + bill_amount
        amount_per_person = total_amt / number_of_people
        print(f"Amount per person: ${amount_per_person:.2f}") 
        print(f"Total bill amt: ${total_amt:.2f}")
    elif tip_percent.lower() == 'c':
        print(f"bill amt: ${bill_amount}")
        print(f"Tip amt: 20%")
        total_amt = (bill_amount * 0.20) + bill_amount
        amount_per_person = total_amt / number_of_people
        print(f"Amount per person: ${amount_per_person:.2f}") 
        print(f"Total bill amt: ${total_amt:.2f}")
else:
    print("Tip amount shouldn't be more than 20%. Please try again.")