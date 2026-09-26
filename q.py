class People:
    people = {
        "Dima": "14-22",
        "Sasha": "23-31",
        "Ivan": "32-40"
    }

name = input("Введіть ім'я: ")

try:
    print("Вікова група:", People.people[name])
except KeyError:
    print("Користувача не знайдено.")