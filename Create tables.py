import pypyodbc as odbc

"""
Список констант
"""

DRIVER_NAME = "SQL Server"
SERVER_NAME = "WIN\SQLEXPRESS"
DATABASE_NAME = "Casino"

connection = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE=Casino};
    Trust_Connection=yes;
"""
connection = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE=Table2;
    Trust_Connection=yes;
"""

conn1 = odbc.connect(connection1)

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
    IDOper
    IDUser
    Transfer
"""

cursor.execute(f"""
    CREATE TABLE Operations (
        IDOper int NOT NULL,
        Login varchar(30) NOT NULL,
        Transfer money NOT NULL   
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
