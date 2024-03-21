def sum_list(input_numbers):
    summa = 0
    for item in input_numbers:
        summa += item
    return summa


def divisions(dividend, divisor):
    result = int(dividend / divisor)
    result_remain = dividend % divisor
    return [result, result_remain]


def main():
    with open('file_test.txt', 'r') as file:
        for line in file:
            numbers = line.strip().split(';')
            # print(f'{numbers}')
            if len(numbers) > 1:
                numbers_str = numbers[0]
                input_list = numbers_str.split()
                input_numbers = [int(item) for item in input_list]
                # print(f'{input_numbers}')
                summ_numbers = sum_list(input_numbers)
                div = divisions(summ_numbers, len(input_numbers))
                output = numbers[1]
                output_list = output.split()
                output_numbers = [int(item) for item in output_list]
                results = div == output_numbers

                if results == True:
                    print(f'1: Results are valid: {results}')
                else:
                    print(f'1: Results are invalid: {results}')


main()
