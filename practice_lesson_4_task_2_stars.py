def get_stars(number):
    for i in range(1, number + 1, 2):
        print(" " * ((number - i) // 2) + "*" * i)

    for i in range(number - 2, 0, -2):
        print(" " * ((number - i) // 2) + "*" * i)


def main():
    while True:
        number = int(input("Enter the number:"))
        if number % 2 != 0 and number > 0:
            get_stars(number)
            break
        else:
            print("Invalid input. Please enter only positive odd numbers")


main()
