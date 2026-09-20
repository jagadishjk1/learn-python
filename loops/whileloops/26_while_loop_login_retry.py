"""
Task: Login Retry
Concepts: while loop, break, counter

Let the user attempt a password up to 3 times. If they enter the
correct password, print "Access granted" and stop immediately.
If they fail all 3 attempts, print "Account locked."
"""
retry_status = 0
password = "Admin@123"


while retry_status < 3:
    user_pass = input("Please Enter your password: ")
    if user_pass == password:
        print ("Access granted")
        break
    else:
        print ("Incorrect password, Please try again!")
    retry_status += 1
else:
    print ("Account locked.")

# print("checking weather the script continues, even when loop hit the break line.")