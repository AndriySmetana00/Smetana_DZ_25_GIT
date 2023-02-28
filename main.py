print('Good morning!')




def read_file():
  try:
      with open('save_to_file.txt', 'r', encoding='utf-8') as file:
          res = file.readlines()
      return res
  except FileNotFoundError:
      print('File not found')


print(read_file())


def save_to_file(n):
    with open('save_to_file.txt', 'w', encoding='utf-8') as file:
        file.write(str(n))
    return n


num = 0
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


print(save_to_file(num))