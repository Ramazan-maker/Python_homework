from datetime import date, timedelta

input_date = input('Датa(YYYY-MM-DD): ')
days = input('Количество дней: ')

input_date = date.fromisoformat(input_date)
delta = timedelta(days=int(days))

new_date = input_date + delta
print(new_date)