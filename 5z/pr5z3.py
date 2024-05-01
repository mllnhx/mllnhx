# Ввод начального количества страниц от пользователя
pages_per_day = int(input("Введите количество страниц, которые студент прочитал в 1-ый день: "))

# Инициализация переменных
day = 1  # Номер текущего дня
total_pages = pages_per_day  # Общее количество прочитанных страниц

# Цикл с условием для подсчета общего количества прочитанных страниц через 10 дней
while day < 11:
    print(f"День {day}: {pages_per_day} страниц")

    # Увеличение количества страниц на 5% и обновление общего количества прочитанных страниц
    pages_per_day *= 1.05
    total_pages += pages_per_day

    day += 1

# Вывод общего количества прочитанных страниц через 10 дней
print(f"Общее количество страниц, прочитанных студентом через 10 дней: {total_pages:.2f} страниц")