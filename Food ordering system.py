def login():
    global isLogin,operation
    data = {
        'nithish': 'nithish2002',
        'vishwa': 'vish12345',
        'mukesh': 'mukesh123',
        'surya': 'surya2003',
    }
    print("*** please Login for order the food ***")
    username = input("Please enter your username")
    password = input("Please enterr your password")
    if (username.lower(), password) in data.items():
        print("Login Successfull")
        isLogin=1
        operation=1
        foodmenu()
    else:
        print("Login is failed")
        exit()


def personal_detail():
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_no = input("Enter your phone number : ")
    if len(phone_no) == 10:
        print('we will text a one-time code to verify your phone number ..')
        import random as r
        otp = ''
        for i in range(4):
            otp =otp+ str(r.randint(1, 9))
            import time as t
            t.sleep(0.1)
        print('Waiting for OTP', end='', flush=True)
        for _ in range(5):
            print('.', end='', flush=True)
            t.sleep(1)
        print('\n<#>Your verification code is:', otp)
        ot = (input('Please Enter OTP: '))
        print(ot)
        if ot == otp:
            print('Your Number has been verified....')
            t.sleep(0.1)
        else:
            print("Please Enter the phone number correctly : ")
            exit()
        print("")
        print("***Customer details***".center(100))
        print("Name : ", name)
        print("Address : ", address)
        print("Phone Number : ", phone_no)
        login()
        exit()
    else:
        print("Please Enter the phone number correctly : ")
        exit()







isLogin=0

total=0
cart=[]
def maintainCart(dish,price):
    global total,cart
    total=total+price
    cart.append(dish)




print("")
print("***Welcome to our space restarant***".center(100))
operation=int(input("1.Food Menu\n2.Login \n3.signup\nEnter your Option : "))




def foodmenu():

    global isLogin,cart,total,operation

    if (operation == 1):
        #print("   ***Welcome to our space restarant***  ")
        isNextItem=1
        while(isNextItem==1):
            country = int(input("1.Indian food\n2.Chinese food\n3.American food\nEnter your Food  Preferece in the listed Country:"))
            if (country == 1):
                veg_nonveg = int(input("1.Veg Food\n2.Non-veg Food\n Enter your Food Preference : "))

                if (veg_nonveg == 1):
                    print("***Indian Veg Foods***")
                    print("1.Idly - ₹.10\n2.Dosai - ₹.50\n3.Pongal - ₹.30\n4.Chappathy - ₹.20\n5.Poori - ₹.15")
                    if (isLogin==0):
                        login()
                    addFood=1
                    while (addFood==1):
                        whichDish=int(input("which dish do you want (0 to finish) : "))
                        if (whichDish==1):
                            maintainCart("idly",10)
                        elif (whichDish == 2):
                            maintainCart("Dosai", 50)
                        elif (whichDish == 3):
                            maintainCart("Pongal", 30)
                        elif (whichDish == 4):
                            maintainCart("Chappathy", 20)
                        elif (whichDish == 5):
                            maintainCart("Poori", 15)

                        addFood=int(input("Again you want to order in indian food (1 to continue and 0 to finish) : "))


                elif (veg_nonveg == 2):
                    print("**Indian Non-Veg Food")
                    print("1.Chicken Biriyani - ₹.180\n2.Chicken Fried Rice - ₹.100\n3.Mutton Briyani - ₹.250\n4.Chicken 65 - ₹.120\n5.Tandoori Chicken - ₹.500")
                    if (isLogin == 0):
                        login()
                    addFood = 1
                    while (addFood == 1):
                        whichDish = int(input("which dish do you want (0 to finish) : "))
                        if (whichDish==1):
                            maintainCart("chicken briyani",180)
                        elif (whichDish == 2):
                            maintainCart("Chicken Fried Rice", 100)
                        elif (whichDish == 3):
                            maintainCart("Mutton Briyani", 250)
                        elif (whichDish == 4):
                            maintainCart("Chicken 65", 120)
                        elif (whichDish == 5):
                            maintainCart("Tandoori Chicken", 500)

                        addFood=int(input("Again you want to order in indian food (1 to continue and 0 to finish) : "))


            elif (country == 2):
                veg_nonveg_c = int(input("1.Veg Food\n2.Non-veg Food\n Enter your Food Preference : "))
                if (veg_nonveg_c == 1):
                    print("***Chinese Veg Food***")
                    print("1.Char Siu Ricebowl - ₹.180\n(Char silu With Delicious Mushroom topping)")
                    print("\n2.Wonton Soup - ₹.100\n(Noodles With Fresh Vegetables and Savory Spices)")
                    print("\n3.Wonton Soup - ₹.280\n(Fluffy CLoud-like steamed buns stuffed with slices of chinese barbecued or roasted pork seasoned with soy sauce)")
                    if (isLogin == 0):
                        login()
                    addFood = 1
                    while (addFood == 1):
                        whichDish = int(input("which dish do you want (0 to finish) : "))
                        if (whichDish==1):
                            maintainCart("Char Siu Ricebowl",180)
                        elif (whichDish == 2):
                            maintainCart("Wonton Soup", 100)
                        elif (whichDish == 3):
                            maintainCart("Wonton Soup", 280)

                        addFood = int(input("Again you want to order in Chinese Veg Food (1 to continue and 0 to finish) : "))


                elif (veg_nonveg_c == 2):
                    print("***Chinese Non-veg Food***")
                    print("1.Fried Kwetiauw - ₹.180\n(Fried Kwetiauw, served with special spices and fried egg)")
                    print("\n2.Frieed Dumpling - ₹.100\n(Dumpling containing fresh and tasty sea food)")
                    print("\n3.Dimsum - ₹.280\n(Dim sum containing fresh and tasty sea food)")
                    if (isLogin == 0):
                        login()
                    addFood = 1
                    while (addFood == 1):
                        whichDish = int(input("which dish do you want (0 to finish) : "))
                        if (whichDish==1):
                            maintainCart("Fried Kwetiauw",180)
                        elif (whichDish == 2):
                             maintainCart("Frieed Dumpling", 100)
                        elif (whichDish == 3):
                            maintainCart("Dimsum", 280)

                        addFood = int(input("Again you want to order in Chinese Non-veg Food (1 to continue and 0 to finish) : "))

            elif (country == 3):
                veg_nonveg_e = int(input("1.Veg Food\n2.Non-veg Food\n Enter your Food Preference : "))
                if (veg_nonveg_e == 1):
                    print("***American Veg Foods***")
                    print("1.Veg Burger - ₹.150\n2.sallad - ₹.80\n3.Pizza Mania - ₹.180\n4.Panner sandwich - ₹.280\n5.Doughnut - ₹.100")
                    if (isLogin == 0):
                        login()
                    addFood = 1
                    while (addFood == 1):
                        whichDish = int(input("which dish do you want (0 to finish) : "))
                        if (whichDish==1):
                            maintainCart("Veg Burger",150)
                        elif (whichDish == 2):
                            maintainCart("sallad", 80)
                        elif (whichDish == 3):
                            maintainCart("Pizza Mania", 180)
                        elif (whichDish == 4):
                            maintainCart("Panner sandwich", 280)
                        elif (whichDish == 5):
                            maintainCart("Doughnut", 100)

                        addFood = int(input("Again you want to order in American Veg Foods (1 to continue and 0 to finish) : "))


                elif (veg_nonveg_e == 2):
                    print("***American Non-veg Foods***")
                    print("1.Chicken Burger - ₹.250\n2.Double Cheese Burger - ₹.330\n3.Hamburger - ₹.150\n4.Chicken Pizza - ₹.300\n5.Hot dogs - ₹.100")
                    if (isLogin == 0):
                        login()
                    addFood = 1
                    while (addFood == 1):
                        whichDish = int(input("which dish do you want (0 to finish) : "))
                        if (whichDish==1):
                            maintainCart("burger",250)
                        elif (whichDish == 2):
                            maintainCart("burger", 250)
                        elif (whichDish == 3):
                            maintainCart("burger", 250)
                        elif (whichDish == 4):
                            maintainCart("burger", 250)
                        elif (whichDish == 5):
                            maintainCart("burger", 250)

                        addFood = int(input("Again you want to order in American Non-veg Foods (1 to continue and 0 to finish) : "))

            isNextItem = int(input("Do you want to order food in any other country :"))
            print(f"dish ordered ",cart," Total price = ",total)
    if(operation==2):
        login()
    if(operation==3):
        personal_detail()




foodmenu()