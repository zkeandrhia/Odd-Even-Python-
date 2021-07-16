#odd and even
while True:
    number = ''
    number = int(input("Enter a number and we will tell if it's an odd or even number: "))
    if number == 'quit':
        break
    if number %2 == 0:
        print(f'{number}, Is an Even Number. ')
    else:
         print(f'{number}, Is an Odd Number. ')