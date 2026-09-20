retry_status = 0

while retry_status < 3:
    answer = input("Do you agree? (yes/no): ")
    print(retry_status)
    if answer == "yes":
        print("Glad we are on same page.")
        break
    retry_status += 1
else:
      print("3 strikes, You are out!")