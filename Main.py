from database_manager import store_passwords



#Open the connection to the flat file
returning = input("Welcome to the password manager, are you a returning user? (Y/N): ")
while returning != "y" and returning != "Y" and returning != "N" and returning != "n":
    returning = input("Please enter Y/N only: ")
password = input("Please enter your password: ")
if returning == "Y" or returning == "y":
    file = open("password.txt", "r")
    #Check and verify from the flat file
    found = False
    for x in file:
        if x == password+"\n":
            #Grant access
            print("Password found!")
            found = True
            break
    if not found:
        print("Password not found.")
    file.close()

else:
    #Stores it in the flat file. Assuming no collision
    file = open("password.txt", "a")
    file.write(password+"\n")
    file.close()
    print("Successfully stored your password!")


