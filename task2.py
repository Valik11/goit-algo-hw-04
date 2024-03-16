def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cats_list.append({"id": id, "name": name, "age": age})
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return cats_list

# Приклад використання функції:
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
