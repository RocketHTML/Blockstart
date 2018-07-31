def register_user(user, passwd, public, private):
        import sqlite3

        conn = sqlite3.connect('grad_keys.db')

        c = conn.cursor()

        c.execute("INSERT INTO grad_keys VALUES (?, ?, ?, ?)",
                  (user, passwd, public, private))

        conn.commit()

        conn.close()

def delete_user(user):
        import sqlite3

        conn = sqlite3.connect('grad_keys.db')

        c = conn.cursor()

        c.execute("DELETE from grad_keys WHERE user=(?)", (user,))

        conn.commit()

        conn.close()

def delete_key(user, public):
        import sqlite3

        conn = sqlite3.connect('grad_keys.db')

        c = conn.cursor()

        c.execute("DELETE from grad_keys WHERE user=(?) and public=(?)", (user, public))

        conn.commit()

        conn.close()

def fetch_user(user):
        import sqlite3

        conn = sqlite3.connect('grad_keys.db')

        c = conn.cursor()

        c.execute("SELECT * from grad_keys WHERE user=(?)", (user,))

        return c.fetchall()

        conn.commit()

        conn.close()


def fetch_all():
        import sqlite3

        conn = sqlite3.connect('grad_keys.db')

        c = conn.cursor()

        c.execute("SELECT * from grad_keys")

        return c.fetchall()

        conn.commit()

        conn.close()

