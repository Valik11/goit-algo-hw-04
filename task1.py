def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = [int(line.split(',')[1]) for line in file]
        total = sum(salaries)
        average = total / len(salaries)
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

# Приклад використання функції:
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
