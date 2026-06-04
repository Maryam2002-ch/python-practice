print("Enter a message. I resversed it for you. If you want to quit, enter 'q'.")

while True:
    message = input("\nmessage: ")
    if message.lower() == 'q':
        print("\nHave a good day.")
        break
    elif not message:
        print("\nYou didn't enter any message.")
        continue

    message_revers = '' .join(reversed(message))

    print('\n', message_revers)
