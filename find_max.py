print("give me a list of numbers (split with space). If you want to quit, enter 'q'.")

while True:
    numbers = input('\nnumbers: ')
    if numbers.lower() == 'q':
        print("Have a good day.")
        break
    elif not numbers:
        print("\nYou didn't enter any numbers.")
        continue

    numbers = numbers.split()
    
    try:
        numbers = [int(num) for num in numbers]
        print(f"\ntTis is your list: {numbers}")
        print(f"This is max of your list: {max(numbers)}")
    
    except ValueError:
        print("\nPlease enter valid numbers.")
