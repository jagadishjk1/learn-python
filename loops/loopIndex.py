# Create a list of at least 4 server names. Loop through it using range(len(list)) and print each one with its position, like:

# 1: web1
# 2: db1
# 3: cache1
# 4: web2

servers_list = ['web1', 'db1', 'cache1', 'web2']
print (len(servers_list))


for i in range(len(servers_list)):
    print(f"position {i+1}: {servers_list[i]}")
