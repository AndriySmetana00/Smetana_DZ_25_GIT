print('Good morning!')



while True:
    print('Possible actions:')
    print('1 - enter number\n2-change number\n3- zero out\n4-quit')
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('Please, enter integer !!!')