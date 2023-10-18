print("NUMBER SYSTEM CONVERSION")
print("By: Clyde Joshua C. Belongilot & Michael Andres S. Cabot")
while True:
    num = eval(input('Enter a Number: '))

    print("|--------------------------|")
    print("|[1] Decimal to Binary     |")
    print("|[2] Decimal to Octal      |")
    print("|[3] Decimal to Hexadecimal|")

    choice = input("What operation do you want to convert? ")

    if choice == '1':
        binary = format(num, 'b')
        print("Decimal", num, "Converted to Binary is", binary)
    elif choice == '2':
        octal = format(num, 'o')
        print("Decimal", num, "Converted to Octal is", octal)
    elif choice == '3':
        hexa = format(num, 'x')
        print("Decimal", num, "Converted to Octal is", hexa)
    else:
        print("Invalid Operation!")

    another = input("Do you want to try again?(y/n)")
    if another.lower() != 'y':
        print("Thank You")
        break
