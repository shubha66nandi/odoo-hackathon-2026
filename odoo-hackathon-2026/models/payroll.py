import sqlite3

DB = "database/database.db"


class Payroll:

    def __init__(self):

        self.conn = sqlite3.connect(DB, check_same_thread=False)
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS payroll(
            payroll_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            month TEXT,
            basic_salary REAL,
            hra REAL,
            da REAL,
            bonus REAL,
            deductions REAL,
            net_salary REAL,
            status TEXT
        )
        """)

        self.conn.commit()

    # ----------------------------
    # Calculate Net Salary
    # ----------------------------
    def calculate_salary(self,
                         basic_salary,
                         hra,
                         da,
                         bonus,
                         deductions):

        return (basic_salary + hra + da + bonus) - deductions


    # ----------------------------
    # Add Payroll
    # ----------------------------
    def add_payroll(self,
                    employee_id,
                    month,
                    basic_salary,
                    hra,
                    da,
                    bonus,
                    deductions):

        net_salary = self.calculate_salary(
            basic_salary,
            hra,
            da,
            bonus,
            deductions
        )

        self.cur.execute("""
        INSERT INTO payroll(
            employee_id,
            month,
            basic_salary,
            hra,
            da,
            bonus,
            deductions,
            net_salary,
            status
        )
        VALUES(?,?,?,?,?,?,?,?,?)
        """,(
            employee_id,
            month,
            basic_salary,
            hra,
            da,
            bonus,
            deductions,
            net_salary,
            "Generated"
        ))

        self.conn.commit()


    # ----------------------------
    # Employee Payroll
    # ----------------------------
    def get_employee_payroll(self, employee_id):

        self.cur.execute("""
        SELECT *
        FROM payroll
        WHERE employee_id=?
        ORDER BY payroll_id DESC
        """,(employee_id,))

        return self.cur.fetchall()


    # ----------------------------
    # All Payroll
    # ----------------------------
    def get_all_payroll(self):

        self.cur.execute("""
        SELECT *
        FROM payroll
        ORDER BY payroll_id DESC
        """)

        return self.cur.fetchall()


    # ----------------------------
    # Update Payroll
    # ----------------------------
    def update_payroll(self,
                       payroll_id,
                       basic_salary,
                       hra,
                       da,
                       bonus,
                       deductions):

        net_salary = self.calculate_salary(
            basic_salary,
            hra,
            da,
            bonus,
            deductions
        )

        self.cur.execute("""
        UPDATE payroll
        SET
        basic_salary=?,
        hra=?,
        da=?,
        bonus=?,
        deductions=?,
        net_salary=?
        WHERE payroll_id=?
        """,(
            basic_salary,
            hra,
            da,
            bonus,
            deductions,
            net_salary,
            payroll_id
        ))

        self.conn.commit()


    # ----------------------------
    # Delete Payroll
    # ----------------------------
    def delete_payroll(self, payroll_id):

        self.cur.execute("""
        DELETE FROM payroll
        WHERE payroll_id=?
        """,(payroll_id,))

        self.conn.commit()


    # ----------------------------
    # Search Payroll
    # ----------------------------
    def search_payroll(self, employee_id):

        self.cur.execute("""
        SELECT *
        FROM payroll
        WHERE employee_id=?
        """,(employee_id,))

        return self.cur.fetchall()
