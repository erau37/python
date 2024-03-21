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
    with open('numbers_file.txt', 'r') as file:
        for line in file:
            fizz, buzz, num3 = map(int, line.strip().split(','))
            numbers_list(fizz, buzz, num3)


# run main function
main()
