import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()
# print(connection)
# print(cur)

# === CREATE ===
# cur.execute("CREATE TABLE users (login TEXT);")
# connection.commit()

# ==== INSERT ====
name = input("Login : ")
cur.execute(f"INSERT INTO users (login) VALUES ('{name}');")
connection.commit()
print("Login added!")

# ===== SELECT =====
cur.execute(f"SELECT rowid, login FROM users;")
res = cur.fetchall()
print(res)

connection.close()