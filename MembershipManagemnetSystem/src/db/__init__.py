import sqlite3


class DbConnect():

    def connect(self):
        cur = sqlite3.connect("ManageSystem.db")

        return cur