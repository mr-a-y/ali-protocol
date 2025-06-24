
while True:
    try:
        price = float(input("give me price of the iteam "))
    

    except ValueError: 
        print("why you no give me number ")
    else:
        break


while True:
    try:
        amount = int(input("how many you trying to buy "))
    except ValueError:
        print("whyb you no give number ")
    else :
        break 

ans = price * amount
print(f"the total price is {round(ans,2)}")