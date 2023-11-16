from student import Student


def calc_sum_scholarship(students: list[Student] | tuple[Student]) -> int:
    return sum(student.get_scholarship() for student in students)


def get_excellent_student_count(students: list[Student] | tuple[Student]) -> int:
    return sum(student.is_excellent() for student in students)


if __name__ == "__main__":
    students = [
        Student("Kirill", 4.4),
        Student("Nastya", 9.3),
        Student("Sasha", 6.5),
        Student("Vanya", 8.7),
        Student("Oleg", 5.7)
    ]

    print(f"The summ scholarship: {calc_sum_scholarship(students)}")
    print(f"Excellent_student_count: {get_excellent_student_count(students)}")