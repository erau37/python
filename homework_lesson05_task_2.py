def get_avg_students_grade():
    students_info = [
        {"first_name": "Alena", "last_name": "Kolesnik", "courses": ["Python", "Java"]},
        {"first_name": "Maria", "last_name": "Moseichuk", "courses": ["Java", "Frontend"]},
        {"first_name": "Petro", "last_name": "Velichko", "courses": ["Python", "FullStack"]},
        {"first_name": "Oleksii", "last_name": "Valyk", "courses": ["Java"]},
        {"first_name": "Dmytro", "last_name": "Dovbur", "courses": ["FullStack"]}
    ]
    students_more_than_one_group = []
    students_not_frontend = []
    students_python_or_java = []
    for student in students_info:
        course = student["courses"]
        name = student["first_name"]
        surname = student["last_name"]
        if "Frontend" not in course:
            students_not_frontend.append(name + " " + surname)
        if "Python" in course or "Java" in course:
            students_python_or_java.append(name + " " + surname)
        if len(course) >= 2:
            students_more_than_one_group.append(name + " " + surname)

    print(f"Not Frontend: {students_not_frontend}")
    print(f"Python or Java: {students_python_or_java}")
    print(f"At least 2 groups: {students_more_than_one_group}")


get_avg_students_grade()
