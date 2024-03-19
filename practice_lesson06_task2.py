def get_square(num_input):
    return int(num_input) ** 2


def get_prime(num_input):
    num_input = int(num_input)  # Convert to integer
    if num_input <= 1:
        return False

    for i in range(2, int(num_input ** 0.5) + 1):
        if num_input % i == 0:
            return False
    return num_input


def main():
    num_input = input("Enter your numbers (separated by comma):").split(',')
    square_list = list(map(get_square, num_input))
    prime_list = list(filter(lambda x: x != False, map(get_prime, num_input)))

    print(f'Squares: {square_list}')
    print(f'Prime numbers: {prime_list}')


main()
