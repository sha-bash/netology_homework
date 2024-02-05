class Student:
    def __init__(self, name, surname, gender, courses):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = courses
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculate_average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return round(total_grades / total_courses, 1) if total_courses > 0 else 0
    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()
    
    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()
    
    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()
    
    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()
    
    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()
    
    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, courses):
        super().__init__(name, surname)
        self.courses_attached = courses
        self.grades = {}
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculate_average_grade()}"
    
    def calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return round(total_grades / total_courses, 1) if total_courses > 0 else 0
    
    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()
    
    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()
    
    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()
    
    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()
    
    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()
    
    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade > 10:
                return 'Ошибка: оценка не может быть больше 10'
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender', ['Python'])
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached.append('Python')

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

student1 = Student('Alice', 'Jones', 'Female', ["Python", "Java"])
student2 = Student('Bob', 'Brown', 'Male', ["Python", "Java"])
lecturer1 = Lecturer('John', 'Doe', ["Python", "Java"])
lecturer2 = Lecturer('Jane', 'Smith', ["Python", "Java"])

student1.grades["Python"] = [8]
student1.grades["Java"] = [7]
student2.grades["Python"] = [9]
student2.grades["Java"] = [6]
lecturer1.grades["Python"] = [10]
lecturer1.grades["Java"] = [9]
lecturer2.grades["Python"] = [5]

def calculate_students_average_grade(students, course):
    grades_sum = 0
    students_count = 0
    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            grades_sum += sum(student.grades[course])
            students_count += 1
    if students_count > 0:
        average_grade = grades_sum / students_count
    else:
        average_grade = 0
    return average_grade

def calculate_lecturers_average_grade(lecturers, course):
    grades_sum = 0
    lecturers_count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            grades_sum += sum(lecturer.grades[course])
            lecturers_count += 1
    if lecturers_count > 0:
        average_grade = grades_sum / lecturers_count
    else:
        average_grade = 0
    return average_grade

students = [student1, student2]
lecturers = [lecturer1, lecturer2]
course = "Python"

students_average_grade = calculate_students_average_grade(students, course)
lecturers_average_grade = calculate_lecturers_average_grade(lecturers, course)

print(f"Средняя оценка за домашние задания по курсу {course} составляет: {students_average_grade}")
print(f"Средняя оценка за лекции по курсу {course} составляет: {lecturers_average_grade}")

print(best_student.grades)

lecturer1 = Lecturer('John', 'Doe', "Java")
lecturer2 = Lecturer('Jane', 'Smith', "Python")

student1 = Student('Alice', 'Jones', 'female', 'Python')
student2 = Student('Bob', 'Brown', 'male', 'Python')

print(lecturer1 > lecturer2)  # True, если первый лектор имеет более высокую среднюю оценку за лекции
print(lecturer1 != lecturer2)  # True, если средние оценки за лекции у лекторов различны

print(student1 < student2)  # True, если первый студент имеет более низкую среднюю оценку за домашние задания
print(student1 == student2)  # True, если средние оценки у студентов различны