import sqlite3
import hashlib

db = sqlite3.connect("users.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    login TEXT UNIQUE,
    password TEXT
)
""")

db.commit()


while True:
    print("\n1 - Реєстрація")
    print("2 - Вхід")
    print("3 - Вихід")

    choice = input("Виберіть пункт: ")

    if choice == "1":
        login = input("Введіть логін: ")
        password = input("Введіть пароль: ")

        cursor.execute("SELECT * FROM users WHERE login = ?", (login,))
        user = cursor.fetchone()

        if user:
            print("Такий користувач вже існує!")
        else:
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            cursor.execute(
                "INSERT INTO users (login, password) VALUES (?, ?)",
                (login, password_hash)
            )

            db.commit()
            print("Реєстрація успішна!")

    elif choice == "2":
        login = input("Введіть логін: ")
        password = input("Введіть пароль: ")

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute(
            "SELECT * FROM users WHERE login = ? AND password = ?",
            (login, password_hash)
        )

        user = cursor.fetchone()

        if user:
            print("Вхід дозволено")
        else:
            print("Вхід заборонено")

    elif choice == "3":
        break

    else:
        print("Невірний вибір")


db.close()