def practice_1():
    print("Enter the number 1 please:\n")
    number = int(input())

    # checking if number is even or odd
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


practice_1()


def practice_2():
    print("Enter the number 2 please:\n")
    number = int(input())
    # checking if number is even or odd, /3 and /5, and not /10

    if number % 2 != 0:
        if number % 3 == 0 and number % 5 == 0 and number % 10 != 0:
            print(f"{number} is odd, 3 and 5 and not 10")
        else:
            print(f"{number} doesn't match conditions")
    else:
        print(f"{number} is even")


practice_2()


def practice_3():
    print("Enter the number 3 please:\n")
    number = int(input())

    # checking
    divisors = []
    i = 1
    while i <= number:
        if number % i == 0:
            divisors.append(i)
        i += 1
    print(f"All divisors of {number}: {divisors}")


practice_3()


def practice_4():
    print("Enter the number 4 please:\n")
    number = input()

    for i in range(len(number)):
        digit = number[i]
        multiplier = 10 ** (len(number) - i - 1)
        print(f'Digit: {digit}, Multiplier: {multiplier}')


# 123

practice_4()
