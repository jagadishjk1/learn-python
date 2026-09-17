# Create a nested list representing 3 servers, each with [name, ip, status]:
servers = [
    ["web1", "10.0.0.1", "running"],
    ["db1", "10.0.0.2", "stopped"],
    ["cache1", "10.0.0.3", "running"]]

# 1. Print the name of the 2nd server
print(servers[1][0])   # db1

# 2. Print the status of the 3rd server
print(servers[2][2])   # running

# Change the status of the 1st server to "stopped", then print the updated servers list
servers[0][2] = "stopped"
print(servers)
