import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

def main():

    print("Добро пожаловать! Вот доступные задачи:")
    tasks = [
        "distance0",
        "circle1",
        "operations2",
        "favorite_movies3",
        "my_family4",
        "zoo5",
        "songs_list6",
        "secret7",
        "garden8",
        "shopping9",
        "store10"
    ]

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    try:
        choice = int(input("Выберите номер задачи для выполнения (1-11): "))
        if choice < 1 or choice > len(tasks):
            print("Неверный номер задачи. Выберите число от 1 до 11.")
            return

        filenames = [
            "distance0",
            "circle1",
            "operations2",
            "favorite_movies3",
            "my_family4",
            "zoo5",
            "songs_list6",
            "secret7",
            "garden8",
            "shopping9",
            "store10"
        ]

        selected_module = filenames[choice - 1]
        print(f"Запуск задачи: {tasks[choice - 1]}")

        exec(f"import {selected_module}")

    except ValueError:
        print("Пожалуйста, введите корректный номер задачи (число).")
    except ModuleNotFoundError:
        print("Не удалось найти указанный модуль. Проверьте название файла.")

if __name__ == "__main__":
    main()

    
    





