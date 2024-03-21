# Loop through numbers from 1 to user input num3
def numbers_list(fizz, buzz, num3):
    result = ""
    for i in range(1, num3 + 1):
        if (i % fizz == 0) and (i % buzz == 0):
            result += 'FB'
        elif i % fizz == 0:
            result += 'F'
        elif i % buzz == 0:
            result += 'B'
        else:
            result += str(i)

        # append separator to the result string except last cycle
        if i != num3:
            result += ' '

    print(f"Output: {result}")


# initialize variables
def main():
    while True:
        try:
            fizz = int(input("Enter number 1: "))
            buzz = int(input("Enter number 2: "))
            num3 = int(input("Enter number 3: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    numbers_list(fizz, buzz, num3)


# run main function
main()
