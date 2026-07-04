import sqlite3

DB = "database/database.db"


class Employee:

    def __init__(self):
        self.conn = sqlite3.connect(DB, check_same_thread=False)
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            employee_id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            department TEXT,
            designation TEXT,
            salary REAL,
            address TEXT,
            profile_picture TEXT
        )
        """)
        self.conn.commit()

    def add_employee(self, employee):
        self.cur.execute("""
        INSERT INTO employees
        VALUES(?,?,?,?,?,?,?,?,?)
        """, employee)

        self.conn.commit()

    def get_employee(self, employee_id):

        self.cur.execute("""
        SELECT * FROM employees
        WHERE employee_id=?
        """,(employee_id,))

        return self.cur.fetchone()

    def get_all_employees(self):

        self.cur.execute("""
        SELECT * FROM employees
        """)

        return self.cur.fetchall()

    def update_employee(self, employee):

        self.cur.execute("""
        UPDATE employees
        SET
        name=?,
        email=?,
        phone=?,
        department=?,
        designation=?,
        salary=?,
        address=?,
        profile_picture=?
        WHERE employee_id=?
        """,

        (
        employee[1],
        employee[2],
        employee[3],
        employee[4],
        employee[5],
        employee[6],
        employee[7],
        employee[8],
        employee[0]
        ))

        self.conn.commit()

    def delete_employee(self, employee_id):

        self.cur.execute("""
        DELETE FROM employees
        WHERE employee_id=?
        """,(employee_id,))

        self.conn.commit()
