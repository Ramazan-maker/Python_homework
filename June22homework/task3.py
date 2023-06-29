my_list= []

for i in range(5):
  my_list.append(float(input("Введите числа: ")))

maximum = max(my_list)
minimum = min(my_list)

for i in range(len(my_list)):
  if my_list[i] == maximum:
    my_list[i] = minimum
  elif my_list[i] == minimum:
    my_list[i] = maximum

print(my_list)

