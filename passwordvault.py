attempts = 3
password = "3434"

while attempts > 0:
    name = input("Enter password: ")
    if name == password:
        print("ACCESS Granted".upper())
        break
    else:
        attempts -=1
        print(f"You have {attempts} attempts left")
else:
    print("ACCESS DENIED you have been locked out try again later".upper())
