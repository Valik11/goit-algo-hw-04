import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для коректної роботи кольорів у терміналі
init()

# Функція для виведення структури директорії
def print_directory_structure(startpath):
    # Перетворення шляху на об'єкт Path для зручності роботи з файловою системою
    startpath = Path(startpath)
    # Використання rglob для рекурсивного обходу всіх файлів та піддиректорій
    for path in sorted(startpath.rglob('*')):
        # Якщо об'єкт є директорією, виводимо його ім'я синім кольором
        if path.is_dir():
            print(Fore.BLUE + str(path.relative_to(startpath)) + Style.RESET_ALL)
        # Якщо об'єкт є файлом, виводимо його ім'я зеленим кольором
        else:
            print(Fore.GREEN + str(path.relative_to(startpath)) + Style.RESET_ALL)

# Основний блок скрипта
if __name__ == '__main__':
    # Перевірка на наявність одного аргументу командного рядка
    if len(sys.argv) != 2:
        print('Використання: python task3.py "D:\шлях\до\вашої\директорії"')
    else:
        # Зчитування шляху до директорії
        directory_path = sys.argv[1]
        # Перевірка, чи існує директорія за вказаним шляхом
        if not Path(directory_path).is_dir():
            print("Помилка: вказаний шлях не існує або не є директорією.")
        else:
            # Виведення структури директорії
            print_directory_structure(directory_path)



