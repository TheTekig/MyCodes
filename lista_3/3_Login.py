print("\nYou need to register yourself to get our services!\n")
user = str(input("User:\n"))
print("\nYour password must have 6 characters and different from the user\n")
password = str(input("New_Password:\n"))
conpassword = str(input("Confirm_New_Password:\n"))

while password != conpassword:
    print("\nerror!\nPassword doesn't match, try again!\n")
    password = str(input("New_Password:\n"))
    conpassword = str(input("Confirm_New_Password:\n"))
    

while password.upper() == user.upper() or len(str(password)) <= 6:
    print("error!\nYour Password probably has less than 6 chacteres or you´re using the user name in the Password!\nTry Again!\n")
    password = str(input("NewPassword:\n"))
    conpassword = str(input("Confirm_New_Password:\n"))

print("\nUser:%s\nPassword:%s\n" %(user,password))
