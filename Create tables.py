import pypyodbc as odbc

"""
Список констант
"""

DRIVER_NAME = "SQL Server"
SERVER_NAME = "LAPTOP-4ARO0MSO\SQLEXPRESS"
DATABASE_NAME = "Casino"

connection = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;"""

conn = odbc.connect(connection)

# Проверка на подключение
# print(conn)

"""
Создадим таблицу:
USERS - 
    Login
    Password
    Cash
"""

cursor = conn.cursor()

cursor.execute(f"""
    CREATE TABLE Users (
        Login varchar(30) NOT NULL PRIMARY KEY,
        Password varchar(30) NOT NULL,
        Cash money NOT NULL
    );
""")
conn.commit()

"""
Создадим таблицу:
Operations:
    Code
    Login
    Transfer
"""
"""Code 1 - Пополнение баланса
Code 2 - Слоты
Code 3 - Рулетка"""
cursor.execute(f"""
    CREATE TABLE Operations (
        Login varchar(30) NOT NULL,
        Transfer money NOT NULL,
        Code int NOT NULL   
    );
""")

conn.commit()

"""
Создадим связь между ID (Users) и IDUser (Operations)
"""

cursor.execute(f"""
   ALTER TABLE dbo.Operations
   ADD CONSTRAINT FK_Login FOREIGN KEY (Login)
      REFERENCES dbo.Users (Login)
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
""")

conn.commit()
