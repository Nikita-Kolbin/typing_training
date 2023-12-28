import sqlite3
import os
from pathlib import Path


class Storage:
    def __init__(self):
        self.con = sqlite3.connect(rf'{Path.cwd().absolute()}\storage\statistics.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS statistics (ID integer primary key AUTOINCREMENT, "
                         "Date VARCHAR(20), Language VARCHAR(20), Speed VARCHAR(20), Accuracy VARCHAR(20))")

    def add_train(self, date, lang, speed, accuracy):
        self.cur.execute(f"INSERT INTO statistics (Date, Language, Speed, Accuracy) "
                         f"VALUES ('{date}', '{lang}', '{speed}', '{accuracy}')")
        self.con.commit()

    def del_train(self, id):
        self.cur.execute(f"DELETE FROM statistics WHERE ID={id}")
        self.con.commit()

    def get_trains(self) -> [(int, str, str, str, str)]:
        res = self.cur.execute("SELECT * FROM statistics")
        return res.fetchall()
