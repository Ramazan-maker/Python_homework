grades = {'Alice': 85,
'Bob': 92,
'Charlie': 78,
'David': 90}#составление словаря
# Расчет среднего балла
average_grade = sum(grades.values()) / len(grades)
# Нахождение максимальной оценки
max_grade = max(grades.values())
print(f"Средний балл {average_grade}, максимальный {max_grade}")
