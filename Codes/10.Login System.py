print("Create Account")
username = input("Enter Username:")
password = input("Enter Password:")

print("Your account has been created successfully!")

print("Login Now!")
username2=input("Username:")
password2=input("Password:")

if username==username2 and password==password2:
    print("Login Successfull!")
else:
    print("Invalid Credentials!")
