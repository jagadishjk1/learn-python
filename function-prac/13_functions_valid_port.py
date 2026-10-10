"""
Task: Port Validator
Concepts: functions, return, validation (True/False), conditionals

Write a function that checks whether a port number is valid.
"""
def is_valid_port(port):

    try:
        port_int = int(port)
        if 1 <= port_int <= 65535:
            return True
        else: 
            return False
    except ValueError:
        return False


user_port = input("Please Enter your port number: ")
port_status = is_valid_port(user_port)

if port_status:
    print(f"Your port {user_port}: Available")
else:
    print(f"Port {user_port} is invalid. Please enter a number between 1 and 65535.")