# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

number = abs(float(input("Введите вещественное число:\n'")))
summa = 0
while round(number, 9) % 10 != 0:
    number = round(number, 9) * 10
    int(number)
while number > 0:
    digit = number % 10
    summa += digit
    number = number // 10
print(f"Сумма цифр вещественного числа: {int(summa)}")