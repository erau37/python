def get_best_weak_student(students_info):
    student_avg_info = []
    for student in students_info:
        grade = student["grades"]
        grade_avg = sum(grade) / len(grade)
        student_avg_info.append(
            {"first_name": student["first_name"], "last_name": student["last_name"], "grade_avg": grade_avg})
    print(student_avg_info)
    return student_avg_info


def get_avg_students_grade():
    students_info = [
        {"first_name": "Alena", "last_name": "Kolesnik", "grades": [10, 5, 6, 9, 2, 7]},
        {"first_name": "Maria", "last_name": "Moseichuk", "grades": [12, 5, 10, 11, 9, 9]},
        {"first_name": "Petro", "last_name": "Velichko", "grades": [12, 5, 11, 11, 9, 8]},
        {"first_name": "Oleksii", "last_name": "Valyk", "grades": [7, 2, 1, 0, 6, 8]}
    ]
    student_avg_info = get_best_weak_student(students_info)
    max_result = 0
    min_result = 12
    best_student_list = []
    weak_student_list = []

    for student in student_avg_info:
        grade = student["grade_avg"]
        name = student["first_name"]
        surname = student["last_name"]
        if grade > max_result:
            max_result = grade
            best_student_list = [name + " " + surname]
        elif grade == max_result:
            best_student_list.append(name + " " + surname)
        if grade < min_result:
            min_result = grade
            weak_student_list = [name + " " + surname]
        elif grade == min_result:
            weak_student_list.append(name + " " + surname)

    print(f"Best student(s): {', '.join(best_student_list)}, average grade: {max_result}")
    print(f"Weak student(s): {', '.join(weak_student_list)}, average grade: {min_result}")


get_avg_students_grade()
