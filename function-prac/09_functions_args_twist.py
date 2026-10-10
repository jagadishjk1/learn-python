"""
Task: *args with a Twist
Concepts: *args, conditionals, string formatting

Write a function that accepts any number of server names (*args)
and returns a formatted string listing them, numbered.
"""
def server_name_clean(*args):
    # print(args)
    count = 1
    result = ""
    for server in args:
        cleaned_name = server.strip()
        result += f"{count}. {cleaned_name}\n"
        count += 1
    return result

formatted_output = server_name_clean(*tuple((input("Please enter the server names with (like., server1, server2): ")).split(",")))
print(formatted_output)