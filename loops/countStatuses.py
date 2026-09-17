# Create a list of server statuses, e.g. ["running", "stopped", "running", "running", "stopped", "error"]. 
# Loop through it and count how many are "running", "stopped", and "error", then print all three counts.

servers_status = ["running", "stopped", "running", "running", "stopped", "error"]

running = 0
stopped = 0
error = 0

for status in servers_status:
    if status == "running":
        running += 1
    elif status == "stopped":
        stopped += 1
    else:
        error += 1
        
print(f"Total running Servers : {running}")
print(f"Total stopped Servers : {stopped}")
print(f"Total error Servers : {error}")