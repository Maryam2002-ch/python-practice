print("give me a number and I tell you the number is even or odd. if you want to quit, enter 'q'.")

while True:
    number = input("\nnumber: ")
    if number.lower() == 'q':
        print("\nHave a good day.")
        break
    else:    
        try:
            if int(number)%2 == 0:
                print(f"\nthe {number} number is even.")
            else:
                print(f"\nthe {number} number is odd.")
        except ValueError:
            print("\nplease enter a valid number.")
