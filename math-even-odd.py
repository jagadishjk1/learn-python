Number = float(input("Enter a Number you want to check odd or even:"))

# print(Number.is_integer())
if Number.is_integer() is True:
    if Number % 2 == 0:
        print(f"Number {Number} is Even.")
    else:
        print(f"Number {Number} is Odd.")
else:
    print(f"Given number is {Number}. It's a decimal number, Please use only integers like 3, 11, 245, 3456")


if Number > 0:
    print(f"Given number {Number} is Postive number.")
elif Number < 0:
    print(f"Given number {Number} is Negitive number.")
else:
    print(f"Given number {Number} is Zero.")