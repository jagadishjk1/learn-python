"""
Task: Server Health Report Generator
Concepts: functions, parameters, return, *args, **kwargs, loops,
          if-elif-else, string formatting

Build a small tool that takes info about multiple servers and
generates a readable health report, including a summary count
of how many servers are healthy vs. unhealthy.
"""
import random

def check_server(name, cpu, memory, status):
    if status == "running":
        if cpu > 90 or memory >90:
            server_health = "unhealthy"
        else:
            server_health = "healthy"
    else:
        server_health = "stopped."
    return server_health

def print_report(name, cpu, memory, status, health):
    if status == "running":
        print(f"[{name}] CPU: {cpu}% | memory: {memory}% | Status: {status} | Health: {health}")
    else:
        print(f"{name} server: Stopped.")

names = ["db1", "master", "testing1", "prod1", "pre_prod"]
status_list = ["running", "stopped"]

servers_checked = 0
healthy_servers = 0
unhealth_servers = 0

for server in names:
    server_cpu = random.randint(1, 100)
    server_memory = random.randint(1, 100)
    server_status = random.choice(status_list)
    server_health = check_server(name=server, cpu=server_cpu, memory=server_memory, status=server_status)
    print_report(name=server, cpu=server_cpu, memory=server_memory, status=server_status, health=server_health)
    servers_checked += 1
    if server_health == "healthy":
        healthy_servers +=1
    else:
        unhealth_servers += 1

print("="*10, "#"*5, "="*10)
print(f"Total servers checked: {servers_checked}")
print(f"Healthy: {healthy_servers}")
print(f"Unhealthy: {unhealth_servers}")

        