MAX_LİNES = 3


def deposit():
    while True:
        amount = input("\nWhat would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 !")
        else:
            print("Please enter a valid number !")
    
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LİNES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LİNES:
                break
            else:
                print("Enter a valid number of lines !")
        else:
            print("Please enter a valid number !")
    
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()