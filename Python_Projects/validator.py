

while True:
    username = input("give me username ")

    x = len(username)
    y = username.count(" ")
    z = username.isalpha()


    if x <= 12 :
        if y == 0 :
            if z == True:
                break
            else:
                print("usrname must contain only letters")
        else:
            print("user name contains spaces ")
        
    else:
        print(" username bigger then 12 characters")

print(f"{username} is a valid username")

