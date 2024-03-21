# Calculate sum of the corresponding elements from 2 lists
def get_sum(numbers):
    sum_numbers = [sum(number) for number in numbers]
    return sum_numbers


def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    numbers = list(zip(list1, list2))
    print(f'Results: {numbers}')

    results = get_sum(numbers)
    print(f'Results: {results}')


main()
