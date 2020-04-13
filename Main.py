from Student import Student


def main():
    first_student = Student("Igor", "Vozny", 88, 167)
    second_student = Student("Max", "Terzy", 95)
    third_student = Student("Oleg")
    print(first_student)
    Student.set_university("KPI")
    print(second_student)
    print(third_student)


main()
