# база данных
# sql -язык для базы данных
# судб - система управления базами данных
# python - random match django

# mySQL,posgreSQL,Oracle,sqlite3
# тестовая база данных - sqlite3
# релеационные и не реляционные

import sqlite3

# sql - execute()-она выполняет команды sql
# cursor()
# база данных - таблица - поля
# CRUD-create reed update delete
db = sqlite3.connect('op37_3.db')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user(
lastname TEXT,
view INTEGER,
nickname TEXT,
age INTEGER
) ''')
# insert into
# c.execute('INSERT INTO user VALUES("beka",57,"hentoya_ogil",20)')
# c.execute('INSERT INTO user VALUES("janna",5,"JAN",22)')

#update -update
c.execute("UPDATE user SET age=100 WHERE lastname='beka' ")
c.execute("UPDATE user SET lastname='genius' WHERE view>50 ")

# delete -delete
c.execute("DELETE FROM user WHERE nickname='0gil' ")

# SELECT
# fachall
c.execute("SELECT rowid,* FROM user")
item = c.fetchall()

for i in item:
    print(i)
db.commit()
db.close()
