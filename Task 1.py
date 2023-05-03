class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = None

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                if not 0 <= grade <= 10:
                    return 'Ошибка, введите от 0 до 10'
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        grades_list = []
        for value in self.grades.values():
            for element in value:
                grades_list.append(element)
        self.avg_grade = round(sum(grades_list) / len(grades_list), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.avg_grade < other.avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = None

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'

    def get_avg_grade(self):
        grades_list = []
        for value in self.grades.values():
            for element in value:
                grades_list.append(element)
        self.avg_grade = round(sum(grades_list) / len(grades_list), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.avg_grade < other.avg_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Студенты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Alex', 'Jobs', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['GIT']
best_student2.finished_courses += ['Введение в программирование']

# Преподаватели
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

cool_lecturer = Lecturer('Ivan', 'Petrov')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']

cool_lecturer2 = Lecturer('Sergei', 'Ivanov')
cool_lecturer2.courses_attached += ['GIT']
cool_lecturer2.courses_attached += ['Python']

# Проставление оценок студентам
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 6)

cool_reviewer.rate_hw(best_student, 'GIT', 6)
cool_reviewer.rate_hw(best_student, 'GIT', 5)
cool_reviewer.rate_hw(best_student, 'GIT', 8)

cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer.rate_hw(best_student2, 'Python', 7)

cool_reviewer.rate_hw(best_student2, 'GIT', 10)
cool_reviewer.rate_hw(best_student2, 'GIT', 9)
cool_reviewer.rate_hw(best_student2, 'GIT', 10)

# Проставление оценок преподавателям
best_student.rate_lector(cool_lecturer, 'Python', 9)
best_student.rate_lector(cool_lecturer, 'Python', 10)
best_student.rate_lector(cool_lecturer, 'Python', 8)

best_student.rate_lector(cool_lecturer, 'GIT', 8)
best_student.rate_lector(cool_lecturer, 'GIT', 7)
best_student.rate_lector(cool_lecturer, 'GIT', 9)

best_student.rate_lector(cool_lecturer2, 'Python', 9)
best_student.rate_lector(cool_lecturer2, 'Python', 10)
best_student.rate_lector(cool_lecturer2, 'Python', 10)

best_student.rate_lector(cool_lecturer2, 'GIT', 8)
best_student.rate_lector(cool_lecturer2, 'GIT', 6)
best_student.rate_lector(cool_lecturer2, 'GIT', 10)

best_student2.rate_lector(cool_lecturer, 'Python', 7)
best_student2.rate_lector(cool_lecturer, 'Python', 8)
best_student2.rate_lector(cool_lecturer, 'Python', 7)

best_student2.rate_lector(cool_lecturer, 'GIT', 9)
best_student2.rate_lector(cool_lecturer, 'GIT', 9)
best_student2.rate_lector(cool_lecturer, 'GIT', 7)

best_student2.rate_lector(cool_lecturer2, 'Python', 9)
best_student2.rate_lector(cool_lecturer2, 'Python', 10)
best_student2.rate_lector(cool_lecturer2, 'Python', 6)

best_student2.rate_lector(cool_lecturer2, 'GIT', 9)
best_student2.rate_lector(cool_lecturer2, 'GIT', 8)
best_student2.rate_lector(cool_lecturer2, 'GIT', 7)

# Вычисление средней оценки конкретного студента/преподавателя
cool_lecturer.get_avg_grade()
best_student.get_avg_grade()
cool_lecturer2.get_avg_grade()
best_student2.get_avg_grade()

all_students = [best_student.__dict__, best_student2.__dict__]
all_lectors = [cool_lecturer.__dict__, cool_lecturer2.__dict__]


def get_avg_grade_all_students(students, course):
    all_grades = []
    for student in students:
        for key, value in student.items():
            if key == 'grades':
                for k, v in value.items():
                    if k == course:
                        all_grades += v
    avg_grades_list_targeted = round(sum(all_grades) / len(all_grades), 1)
    print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {course}: {avg_grades_list_targeted}')


def get_avg_grade_all_lectors(lectors, course):
    all_grades = []
    for lector in lectors:
        for key, value in lector.items():
            if key == 'grades':
                for k, v in value.items():
                    if k == course:
                        all_grades += v
    avg_grades_list_targeted = round(sum(all_grades) / len(all_grades), 1)
    print(f'Средняя оценка за домашние задания по всем лекторам в рамках курса {course}: {avg_grades_list_targeted}')


# Перегрузка магического метода __str__ у всех классов
print(f'{best_student}\n---\n{cool_lecturer}\n---\n{cool_reviewer}\n')

# Сравнение (через операторы сравнения) между собой лекторов по средней оценке за лекции
# и студентов по средней оценке за домашние задания
print(cool_lecturer < cool_lecturer2)
print(cool_lecturer2 < cool_lecturer)
print(best_student < best_student2)
print(best_student2 < best_student)
print()

# Вычисление средней оценки по всем студентам рамках конкретного курса
get_avg_grade_all_students(all_students, 'Python')
get_avg_grade_all_students(all_students, 'GIT')

# Вычисление средней оценки по всем преподавателям в рамках конкретного курса
get_avg_grade_all_lectors(all_lectors, 'Python')
get_avg_grade_all_lectors(all_lectors, 'GIT')
