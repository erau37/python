def practice_1():
    # sum of the list using for and while
    numbers = list(range(1, 20))
    summa_1 = i = 0

    while i <= len(numbers):
        summa_1 += i
        i += 1
    print(f"Sum of the list with while equals: {summa_1}")

    summa_2 = 0
    for i in list(range(1, 15)):
        summa_2 += i
    print(f"Sum of the list with for equals: {summa_2}")


practice_1()
