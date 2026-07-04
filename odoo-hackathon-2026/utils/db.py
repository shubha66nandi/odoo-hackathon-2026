# SUPABASE_URL=https://zvcacliunacyuodbapwj.supabase.co
# SUPABASE_PUBLISHABLE_KEY=sb_publishable_tG6neP9gU8bMgCtjCMyKMg_JQiiPvvY
# SUPABASE_SECRET_KEY=sb_secret_l2up3W34Hoc-gr-XVqheuQ_QxU5eKeL
# SUPABASE_JWKS_URL=https://zvcacliunacyuodbapwj.supabase.co/auth/v1/.well-known/jwks.json


# NEXT_PUBLIC_SUPABASE_URL=https://zvcacliunacyuodbapwj.supabase.co
# NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_tG6neP9gU8bMgCtjCMyKMg_JQiiPvvY


from supabase import create_client, Client

# ======================================================
# SUPABASE CONFIGURATION
# ======================================================

SUPABASE_URL = "https://zvcacliunacyuodbapwj.supabase.co"
SUPABASE_KEY = "sb_publishable_tG6neP9gU8bMgCtjCMyKMg_JQiiPvvY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ======================================================
# CREATE TABLES
# ======================================================

def create_tables():
    """
    Tables are created in the Supabase Dashboard.
    This function exists only to avoid import errors.
    """
    return True

# ======================================================
# EMPLOYEE FUNCTIONS
# ======================================================

def add_employee(name, department, email, phone):
    data = {
        "name": name,
        "department": department,
        "email": email,
        "phone": phone
    }
    return supabase.table("employees").insert(data).execute()


def get_employees():
    return supabase.table("employees").select("*").execute()


def delete_employee(emp_id):
    return supabase.table("employees").delete().eq("id", emp_id).execute()


# ======================================================
# ATTENDANCE FUNCTIONS
# ======================================================

def add_attendance(employee, department, attendance_date,
                   status, check_in, check_out):

    data = {
        "employee": employee,
        "department": department,
        "attendance_date": str(attendance_date),
        "status": status,
        "check_in": str(check_in),
        "check_out": str(check_out)
    }

    return supabase.table("attendance").insert(data).execute()


def get_attendance():
    return supabase.table("attendance").select("*").execute()


def delete_attendance(attendance_id):
    return supabase.table("attendance").delete().eq("id", attendance_id).execute()


# ======================================================
# LEAVE FUNCTIONS
# ======================================================

def apply_leave(employee,
                leave_type,
                start_date,
                end_date,
                reason):

    data = {
        "employee": employee,
        "leave_type": leave_type,
        "start_date": str(start_date),
        "end_date": str(end_date),
        "reason": reason,
        "status": "Pending"
    }

    return supabase.table("leave_requests").insert(data).execute()


def get_leave_requests():
    return supabase.table("leave_requests").select("*").execute()


def approve_leave(request_id):
    return supabase.table("leave_requests").update(
        {"status": "Approved"}
    ).eq("id", request_id).execute()


def reject_leave(request_id):
    return supabase.table("leave_requests").update(
        {"status": "Rejected"}
    ).eq("id", request_id).execute()


# ======================================================
# PAYROLL FUNCTIONS
# ======================================================

def add_payroll(employee,
                basic_salary,
                bonus,
                deduction):

    net_salary = basic_salary + bonus - deduction

    data = {
        "employee": employee,
        "basic_salary": basic_salary,
        "bonus": bonus,
        "deduction": deduction,
        "net_salary": net_salary
    }

    return supabase.table("payroll").insert(data).execute()


def get_payroll():
    return supabase.table("payroll").select("*").execute()


# ======================================================
# DASHBOARD FUNCTIONS
# ======================================================

def employee_count():
    return len(get_employees().data)


def attendance_count():
    return len(get_attendance().data)


def leave_count():
    return len(get_leave_requests().data)


def payroll_count():
    return len(get_payroll().data)
