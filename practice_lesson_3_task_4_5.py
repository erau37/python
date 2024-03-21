def atm(amount):
    bills = [10, 20, 50, 100, 200, 500, 1000]
    # Use cuts to make it reversed from the highest bill
    rev_bills = bills[::-1]
    # Empty dictionary to store result in format key-value (bill: count)
    notes = {}

    # Loop through each bill in the list of bills
    for rev_bill in rev_bills:
        # Calculate max count of the bill
        count = amount // rev_bill
        # Add it to dictionary
        notes[rev_bill] = count
        # Calculating remaining amount via subtracting used bills
        amount -= count * rev_bill
    return notes


def main():
    # infinite loop to check validation
    while True:
        # try-except block for ValueError
        try:
            amount = int(input("Enter the amount please: "))
            # As the smallest value in euro is 5, checking if its divisible by 5
            if amount % 5 == 0:
                notes = atm(amount)
                # Make string looks readable with list comprehension
                # Iterate through dictionary, add separator and don't include 0 values
                notes_str = ", ".join([f"{count} note(s) of {bill}" for bill, count in notes.items() if count > 0])
                print(f"Take your money please: {notes_str}")
                break
            # Error message 1
            else:
                print("Enter amount divisible by 5")
        # Error message 2
        except ValueError:
            print("Invalid input. Please enter a number.")


main()


def atm_2(amount_2):
    bills = [5, 10, 20, 50, 100, 200, 500, 1000]
    notes = {}

    for bill in bills:
        # Limit count to 10
        count = min(amount_2 // bill, 10)
        # Checking remaining amount
        amount_2 -= count * bill
        notes[bill] = count

    return notes


def main_2():
    while True:
        try:
            amount_2 = int(input("Enter the amount please: "))
            if amount_2 % 5 == 0:
                notes = atm_2(amount_2)
                notes_str = ", ".join([f"{count} note(s) of {bill}" for bill, count in notes.items() if count > 0])
                print(f"Take your money please: {notes_str}")
                break
            else:
                print("Enter amount divisible by 5")
        except ValueError:
            print("Invalid input. Please enter a number.")


main_2()
