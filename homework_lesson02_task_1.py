# Fixed examples from lecture
def example_if():
    print("Give it to me!")
    number = int(input())

    if number >= 100:
        print("Thanks, man!")
    elif (number > 10) and (number < 100):
        print("OK :(")
    else:
        print("WHAAAAT????")
    if number > 1000:
        print("!!!!WOOOOWWWW!!!")


example_if()


def example_all():
    data = [True, True, True, True]
    result = all(data)
    print(result)


example_all()


def example_any():
    data = [False, False, True, False]
    result = any(data)
    print(result)


example_any()


def example_tren():
    test = True
    result = 'Test is True' if test else 'Test is False'
    print(result)


example_tren()


def example_tren_2():
    test = True
    print('ttt' if test else 'fff')


example_tren_2()


def example_tren_3():
    test = True
    result = 'Test is True' if test else None
    print(result)


example_tren_3()


def example_tren_4():
    test = True
    result = test and 'Test is True' or 'Test is False'
    print(result)


example_tren_4()
