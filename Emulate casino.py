import pypyodbc as odbc
from art import tprint

tprint('CASINO 777', font='bulbhead')


def initializ():
    while True:
        print("\n1) Войти"
              "\n2) Зарегестрироваться"
              "\n3) Выйти")
        try:
            choice = int(input("Действие: "))
            if choice >= 1 and choice <= 3:
                match choice:
                    case 1:
                        sign_in()
                    case 2:
                        sign_up()
                    case 3:
                        break
            else:
                print("Неверная команда!")
        except ValueError:
            print("Введено неверное значение")


def sign_up():
    login = input("Введите логин: ")
    cursor.execute(f"""
           SELECT Login
           FROM Users
""")
    records = [line[0] for line in cursor]
    # print(records)
    if login in records:
        print("Такой логин уже существует! Повторите попытку!")
    else:
        password = input("Введите пароль: ")
        print(f"""INSERT INTO dbo.Users 
             VALUES ('{login}','{password}',0);
                """)
        cursor.execute("INSERT INTO dbo.Users VALUES ('{}','{}',0);".format(login,password))
        conn.commit()
        print("\nРегистрация завершена!")

def sign_in():
    login = input("Введите логин: ")
    cursor.execute(f"""
        SELECT Login
        FROM Users
    """)
    EXIST = False
    for line in cursor:
        if line[0] == login:
            EXIST = True
            break
    if EXIST:
        password = input("Введите пароль: ")
        cursor.execute(f"""
                    SELECT Password
                    FROM Users
                    WHERE Login={login}
                """)
        TRUE_PASS = False
        for line in cursor:
            if line[0] == password:
                TRUE_PASS = True
                break
        if TRUE_PASS:
            print("Авторизация прошла успешно\n")
            sign_menu(login)
        else:
            print("Неверный пароль! Повторите попытку. Для выхода введите 0")
    else:
        print("Неверный логин! Повторите попытку.")


def sign_menu(login):
    print(f"Добро пожаловать, {login}")
    while True:
        cursor.execute(f"""
           SELECT Cash
           FROM Users
           WHERE Login={login}
       """)
        for line in cursor:
            cash = line[0]
        print("Счет: {:0.2f}$".format(cash))
        print("\n1) Рулетка"
              "\n2) Слоты"
              "\n3) Пополнить баланс"
              "\n4) Выйти")
        try:
            choice = int(input("Действие: "))
            match choice:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    print(f"Всего доброго, {login}!")
                    break
        except ValueError:
            print("Введено неверное значение")


def main():
    initializ()


DRIVER_NAME = "SQL Server"
SERVER_NAME = "WIN\SQLEXPRESS"
DATABASE_NAME = "Casino"

connection = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection)
cursor = conn.cursor()

main()
