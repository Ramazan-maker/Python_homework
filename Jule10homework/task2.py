# Создание пустого словаря для хранения оценок студентов
student_grades = {}

# Функция для добавления оценки студенту
def add_grade(student_name, subject, grade):
    # Проверяем, есть ли запись для данного студента в словаре
    if student_name in student_grades:
        # Если запись уже существует, добавляем новую оценку в словарь для данного студента и предмета
        student_grades[student_name][subject] = grade
    else:
        # Если записи для студента еще нет, создаем новую запись со словарем оценок
        student_grades[student_name] = {subject: grade}

# Функция для получения оценки студента по предмету
def get_grade(student_name, subject):
    # Проверяем, есть ли запись для данного студента в словаре
    if student_name in student_grades:
        # Проверяем, есть ли запись для данного предмета у данного студента
        if subject in student_grades[student_name]:
            # Возвращаем оценку студента по данному предмету
            return student_grades[student_name][subject]
    # Если запись не найдена, возвращаем None
    return None

# Добавление оценок студентам
add_grade("Alice", "Math", 90)
add_grade("Alice", "History", 85)
add_grade("Bob", "Math", 75)
add_grade("Bob", "Science", 80)

# Получение оценок студентов
print(get_grade("Alice", "Math"))  # Вывод: 90
print(get_grade("Bob", "Science"))  # Вывод: 80
print(get_grade("Alice", "English"))  # Вывод: None
