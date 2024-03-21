def calculate_floor_entrance(apt, floors_amount, apt_amount_floor):
    if apt <= apt_amount_floor:
        return 1, 1
    else:
        apt_entrance = floors_amount * apt_amount_floor
        entrance = (apt - 1) // apt_entrance + 1
        floor = ((apt - 1) % apt_entrance) // apt_amount_floor + 1
        return floor, entrance


def main():
    apt = int(input("Enter apartment number: "))
    floors_amount = int(input("Enter amount of floors: "))
    apt_amount_floor = int(input("Enter amount of apartments per floor: "))
    floor, entrance = calculate_floor_entrance(apt, floors_amount, apt_amount_floor)
    print(f'Entrance: {entrance}')
    print(f'Floor: {floor}')


main()
