import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS information (id INTEGER PRIMARY KEY, nane, surname)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM information")
        rows = self.cur.fetchall()
        return rows

    # def insert(self, nane, surname):
    #     self.cur.execute(
    #         "INSERT INTO information VALUES (NULL, ?, ?)", (nane, surname))
    #     self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('ww.db')
# db.insert("Jon", "Bert")
# db.insert("Yer", "Mit")
# db.insert("Li", "Nio")
# db.insert("Vok", "Curt")
# db.insert("Pew", "Zid")
# db.insert("Erli", "Hipp")
# db.insert("Bern", "Setul")
# db.insert("Jenna", "Nusew")
