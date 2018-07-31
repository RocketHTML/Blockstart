import sqlite3


conn = sqlite3.connect('grad_keys.db')

c = conn.cursor()

c.execute("""CREATE TABLE grad_keys (
user text,
passwd text,
public text,
private text
)
""")

conn.commit()

conn.close()

