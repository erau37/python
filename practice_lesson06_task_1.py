def get_string_lower(str_input):
    return str_input.lower()


def get_string_upper(str_input):
    return str_input.upper()


def main():
    str_input = str(input("Enter your strings (separated by coma):")).split(',')
    lower_list = list(map(get_string_lower, str_input))
    upper_list = list(map(get_string_upper, str_input))

    print(f'Result of lower case: {lower_list}')
    print(f'Result of upper case: {upper_list}')


main()
