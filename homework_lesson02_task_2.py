# If a person is below 18 years old and is a student, they are eligible for a 20% discount.
# If a person is 18 years old or older and is a student - 15% discount
# If a person is a NOT student - no discount.

# get student status function
def get_is_student(user_input):
    return user_input == 'yes'


# calculate and print discount function
def user_discount(user_age, user_input):
    is_student = get_is_student(user_input)
    if user_age < 18 and is_student:
        print('Get your 20% discount')
    elif user_age >= 18 and is_student:
        print('Get your 15% discount')
    else:
        print("Sorry, no discount")


# initialize input variables with validation of input fields function
def main():
    while True:
        try:
            user_age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        user_input = input("Are you a student (yes or no): ").lower()
        if user_input in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    user_discount(user_age, user_input)


# run main function
main()
