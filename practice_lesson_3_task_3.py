def print_itself_reversed():
    with open('practice_lesson_3_task_3.py', 'r') as file:
        source = file.read()
        s = source[::-1]
        print(s)


print_itself_reversed()
