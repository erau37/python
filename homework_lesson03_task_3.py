# Loop through numbers from 1 to user input num3
def numbers_list(fizz, buzz, num3):
    # List comprehension to loop each number in the file and assign proper values
    results = [
        'FB' if (i % fizz == 0) and (i % buzz == 0) else 'F' if i % fizz == 0 else 'B' if i % buzz == 0 else str(i) for
        i in range(1, num3)]
    # Write results in file with new line and spaces
    with open('results.txt', 'a') as file:
        file.write(' '.join(results) + '\n')
    # Print the result for visibility
    print(f"Output: {' '.join(results)}")


# Main function to define variables
def main():
    # Open file in write mode to clear the previous run
    with open('results.txt', 'w'):
        pass
    # Open file to read numbers
    with open('numbers_file.txt', 'r') as file:
        for line in file:
            fizz, buzz, num3 = map(int, line.strip().split(','))
            numbers_list(fizz, buzz, num3)


# run main function
main()
