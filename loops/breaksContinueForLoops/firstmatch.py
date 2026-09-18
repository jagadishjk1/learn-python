# Create a list of server names. Ask the user to search for a specific server name. 
# Loop through the list with a for loop — as soon as you find a match
#  print "Found it!" and use break to stop the loop immediately (no need to keep checking the rest).

server_list = ['testing', 'db159', 'prod', 'sql-server']
match_server = input("Enter the server you want to search: ")
found = False

for server in server_list:
    if server == match_server:
        print("Found it! Exit")
        found = True
        break

if not found:
    print(f"{match_server} was not found in the list.")