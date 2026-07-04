import sqlite3

DB="database/database.db"


class Leave:

    def __init__(self):

        self.conn=sqlite3.connect(DB,check_same_thread=False)
        self.cur=self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS leave_requests(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            leave_type TEXT,
            from_date TEXT,
            to_date TEXT,
            remarks TEXT,
            status TEXT,
            admin_comment TEXT
        )
        """)

        self.conn.commit()

    def apply_leave(
            self,
            employee_id,
            leave_type,
            from_date,
            to_date,
            remarks):

        self.cur.execute("""
        INSERT INTO leave_requests(
        employee_id,
        leave_type,
        from_date,
        to_date,
        remarks,
        status,
        admin_comment)
        VALUES(?,?,?,?,?,?,?)
        """,

        (
            employee_id,
            leave_type,
            from_date,
            to_date,
            remarks,
            "Pending",
            ""
        ))

        self.conn.commit()

    def get_employee_leaves(self,employee_id):

        self.cur.execute("""
        SELECT *
        FROM leave_requests
        WHERE employee_id=?
        ORDER BY id DESC
        """,(employee_id,))

        return self.cur.fetchall()

    def get_all_leaves(self):

        self.cur.execute("""
        SELECT *
        FROM leave_requests
        ORDER BY id DESC
        """)

        return self.cur.fetchall()

    def approve_leave(self,id,comment="Approved"):

        self.cur.execute("""
        UPDATE leave_requests
        SET
        status='Approved',
        admin_comment=?
        WHERE id=?
        """,(comment,id))

        self.conn.commit()

    def reject_leave(self,id,comment):

        self.cur.execute("""
        UPDATE leave_requests
        SET
        status='Rejected',
        admin_comment=?
        WHERE id=?
        """,(comment,id))

        self.conn.commit()
