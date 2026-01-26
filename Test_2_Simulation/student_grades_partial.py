def print_student(student):
    print(f"Name: {student['name']['first']} {student['name']['last']}")
    print(f"Age: {student['age']}")
    print(f"Grades:", end="")
    for grade in student['grades']:
        print(f" {grade}", end="")
    print()

def ask_student_grades(student):
    while len(student['grades']) < 5:
        new_grade = float(input("Insert new grade: "))
        student['grades'].append(new_grade)

def check_passed_student(student):
    sum_grades = 0
    for grade in student['grades']:
        sum_grades += grade
    average_grade = sum_grades/len(student['grades'])
    if average_grade >= 4.0:
        print(f"{student['name']['first']} {student['name']['last']} passed with mean {average_grade}!")
    else:
        print(f"{student['name']['first']} {student['name']['last']} did not pass with mean {average_grade}!")
    return average_grade

if __name__ == "__main__":
    students = [{
        "name": {
            "first": "Luke",
            "last": "Skywalker"
        },
        "age": 31,
        "grades": [4.5, 4.5]
    }, {
        "name": {
            "first": "Obi-Wan",
            "last": "Kenobi"
        },
        "age": 67,
        "grades": [4.5]
    }, {
        "name": {
            "first": "Darth",
            "last": "Vader"
        },
        "age": 52,
        "grades": [5.5, 2, 3.5]
    }]

    for s in students:
        print_student(student=s)
        ask_student_grades(student=s)
        print("")

    print("Passed students: ")
    class_sum = 0
    for s in students:
        class_sum += check_passed_student(s)
    class_mean = class_sum / len(students)
    print(f"Class mean: {class_mean}")



