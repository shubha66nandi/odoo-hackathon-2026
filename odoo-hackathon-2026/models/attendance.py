import sqlite3
from datetime import datetime

DB = "database/database.db"


class Attendance:

    def __init__(self):

        self.conn = sqlite3.connect(DB,check_same_thread=False)
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            date TEXT,
            check_in TEXT,
            check_out TEXT,
            status TEXT
        )
        """)

        self.conn.commit()

    def check_in(self, employee_id):

        today = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")

        self.cur.execute("""
        INSERT INTO attendance(
        employee_id,
        date,
        check_in,
        status)
        VALUES(?,?,?,?)
        """,

        (
            employee_id,
            today,
            time,
            "Present"
        ))

        self.conn.commit()

    def check_out(self, employee_id):

        today = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")

        self.cur.execute("""
        UPDATE attendance
        SET check_out=?
        WHERE employee_id=?
        AND date=?
        """,

        (
            time,
            employee_id,
            today
        ))

        self.conn.commit()

    def get_employee_attendance(self, employee_id):

        self.cur.execute("""
        SELECT *
        FROM attendance
        WHERE employee_id=?
        ORDER BY date DESC
        """,(employee_id,))

        return self.cur.fetchall()

    def get_all_attendance(self):

        self.cur.execute("""
        SELECT *
        FROM attendance
        ORDER BY date DESC
        """)

        return self.cur.fetchall()
