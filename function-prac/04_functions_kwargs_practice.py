"""
Task: **kwargs Practice
Concepts: functions, **kwargs, loops, f-strings

Write a function that accepts server info as keyword arguments
(e.g., name="web1", ip="10.0.0.1", status="running") and prints
each key-value pair in a readable format.
"""
def server_info(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key} = value: {value}")

server_info(name="web1", ip="10.0.0.1", status="running")

