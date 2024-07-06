first = int(input("Введите число №1: "))
second = int(input("Введите число №2: "))
third = int(input("Введите число №3: "))
if first == second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')

# Другой способ сравнить элементы
config = [] # создаем пустой лист
first = int(input("Введите число №1: "))
config.append(first)
second = int(input("Введите число №2: "))
config.append(second)
third = int(input("Введите число №3: "))
config.append(third)
count = 0 # Ставим счетчик на 0
for a in range(len(config)): # Перебор элементов списка
    for b in range(a+1, len(config)):
        if config[a] == config[b]:
            count = count+1
            print("Элементы", a, "и", b, "равны")
print('Количество совпадений: ', count)


