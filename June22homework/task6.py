

employees = ["John", "Alice", "Bob", "Alice", "Jane", "John","Ramazan","Ramazan"]
duplicates = []

for employee in employees:
    if employees.count(employee) > 1 and employee not in duplicates:
        duplicates.append(employee)

print("Имена наглецов, попавших в базу дважды:", duplicates)
