print('Good morning!')



while True:
    print('Possible actions:')
    print('1 - enter number\n2-change number\n3- zero out\n4-quit')
    try:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            num = int(input("Enter your number: "))
        elif choice == 2:
            new_num = int(input("Enter new number: "))
            num = new_num
        elif choice == 3:
            num = 0
        elif choice == 4:
            break
        else:
            print('Wrong choice! Please, enter 1, 2, 3 or 4')
    except ValueError:
        print('Please, enter integer !!!')