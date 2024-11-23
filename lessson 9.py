import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()
# print(connection)
# print(cur)

# == DROP ==
cur.execute("DROP TABLE Animal;")
connection.commit()

# === CREATE ===
cur.execute("CREATE TABLE IF NOT EXISTS Animal (id INT, name TEXT, type TEXT);")
connection.commit()

# ==== INSERT ====
# name = input("Login : ")
# cur.execute(f"INSERT INTO users (login) VALUES ('{name}');")
# connection.commit()
# print("Login added!")

# ===== SELECT =====
# cur.execute(f"SELECT rowid, login FROM users;")
# res = cur.fetchall()
# print(res)

# ====== UPDATE ======
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (1, 'Tiger', 'Walking');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (2, 'Bear', 'Walking');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (3, 'Dog', 'Walking');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (4, 'Eagle', 'Flying');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (5, 'Crow', 'Flying');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (6, 'Salmon', 'Swimming');")
connection.commit()

connection.close()