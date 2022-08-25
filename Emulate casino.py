import pypyodbc as odbc
from art import tprint
from random import randint
from random import choice

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
        cursor.execute("INSERT INTO dbo.Users VALUES ('{}','{}',0);".format(login, password))
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
                    WHERE Login='{login}'
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
           WHERE Login='{login}'
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
                    roulette(login)
                case 2:
                    slot(login)
                case 3:
                    balance(login)
                case 4:
                    print(f"Всего доброго, {login}!")
                    break
        except ValueError:
            print("Введено неверное значение")


def roulette(login):
    print("\nДобро пожаловать в рулетку")
    while True:
        # print("Счет: {:0.2f}$".format(cash))
        # variat = []
        print("\n1) Четное значение"
              "\n2) Нечетное значение"
              "\n3) Красное"
              "\n4) Черное"
              "\n5) Точное значение"
              "\n6) Выйти")
        try:
            choice = int(input("Действие: "))
            match choice:
                case 1:
                    variat = [i for i in range(2, 37, 2)]
                    kf = 2
                    # print(variat)
                case 2:
                    variat = [i for i in range(1, 36, 2)]
                    # print(variat)
                    kf = 2
                case 3:
                    variat = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 30, 32, 34, 36]
                    kf = 2
                case 4:
                    variat = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
                    kf = 2
                case 5:
                    num = int(input("Введите число от 1 до 36: "))
                    variat = []
                    variat.append(num)
                    kf = 36
                case 6:
                    break
                case _:
                    break
        except ValueError:
            print("Введено неверное значение")
        cursor.execute(f"""
                   SELECT Cash
                   FROM Users
                   WHERE Login='{login}'
               """)
        for line in cursor:
            cash = line[0]
        summ = int(input("Введите сумму ставки: "))
        if summ > cash:
            print("Ошибка! Недостаточно средств!")
            break


        a = randint(0, 36)
        print(a)
        print(a in variat)
        if a in variat:
            cursor.execute(f"""
                UPDATE Users 
                SET cash={cash+summ*(kf-1)} 
                WHERE Login='{login}'
                           """)
            print('Поздравляем!')
        else:
            cursor.execute(f"""
                    UPDATE Users 
                    SET cash={cash - summ} 
                    WHERE Login='{login}'
                                       """)
        conn.commit()
def balance(login):
    money = int(input("Введите сумму, на которую хотите пополнить счет: "))
    cursor.execute(f"""
                       SELECT Cash
                       FROM Users
                       WHERE Login='{login}'
                   """)
    for line in cursor:
        cash = line[0]
    cursor.execute(f"""
           UPDATE Users 
           SET Cash={cash + money} 
           WHERE Login='{login}'
                      """)
def slot(login):
    print("\nДобро пожаловать! 1 слот = 50$")
    cursor.execute(f"""
                       SELECT Cash
                       FROM Users
                       WHERE Login='{login}'
                   """)
    for line in cursor:
        cash = line[0]
    if cash<50:
        print("Ошибка! Недостаточно средств!")
    else:
        m = ['🍌','🍇','🍍']
        a = choice(m)
        b = choice(m)
        c = choice(m)
        print(a,b,c)
        if a==b and b==c:
            print('Поздравляем!')
            cursor.execute(f"""
                    UPDATE Users 
                    SET cash={cash*10} 
                    WHERE Login='{login}'
                               """)
        elif a==b or b==c or a==c:
            print('Поздравляем!')
            cursor.execute(f"""
                    UPDATE Users 
                    SET cash={cash*2} 
                    WHERE Login='{login}'
                               """)
        else:
            cursor.execute(f"""
                        UPDATE Users 
                        SET cash={cash-50} 
                        WHERE Login='{login}'
                                           """)
    conn.commit()
def main():
    initializ()


DRIVER_NAME = "SQL Server"
SERVER_NAME = "LAPTOP-4ARO0MSO\SQLEXPRESS"
DATABASE_NAME = "Casino"

connection = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection)
cursor = conn.cursor()

main()
