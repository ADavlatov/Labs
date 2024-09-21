# Лабораторная работа №2. Задание №3
# БВТ2403 - Давлатов Амирхан

# Проверяем делится ли число n на числа от 2 до корня из n
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
