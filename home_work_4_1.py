my_list_1 = [0, 1, 0, 12, 3]
print("Вхідні дані:", my_list_1)
my_list_2 = []
count = 0

for number in my_list_1:
    if number != 0:
        my_list_2.append(number)
    else:
        count += 1
print("Відформатований список", my_list_2 + [0] * count)
