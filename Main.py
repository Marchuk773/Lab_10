from Student import Student

if __name__ == '__main__':
    first_student = Student("Igor", "Vozny", 88, 167, "IKNI", "PZ", "Default")
    second_student = Student("Max", "Terzy", 95, 190)
    third_student = Student("Nastya", "Bezpalko", 90)
    print(first_student)
    Student.set_university("KPI")
    print(second_student)
    print(third_student)
    students_list = [first_student, second_student, third_student]
