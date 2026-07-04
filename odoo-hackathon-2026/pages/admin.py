import streamlit as st

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="HRMS Admin",
    page_icon="💼",
    layout="wide"
)

# ----------------------------
st.markdown("""
<style>

/* Hide Streamlit UI */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* ---------------- App Background ---------------- */

.stApp{
    background:#0f172a;
    color:white;
}

/* ---------------- Main Container ---------------- */

.main .block-container{
    background:#0f172a;
    padding:2rem;
}

/* ---------------- Titles ---------------- */

h1,h2,h3{
    color:white !important;
}

/* ---------------- Text ---------------- */

p,
label,
span{
    color:#cbd5e1 !important;
}

/* ---------------- Sidebar ---------------- */

section[data-testid="stSidebar"]{
    background:#1e293b;
    border-right:1px solid #334155;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* ---------------- Metric Cards ---------------- */

div[data-testid="metric-container"]{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:18px;
    padding:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,.35);
}

/* ---------------- Forms ---------------- */

div[data-testid="stForm"]{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:18px;
    padding:25px;
    box-shadow:0px 8px 20px rgba(0,0,0,.35);
}

/* ---------------- DataFrame ---------------- */

div[data-testid="stDataFrame"]{
    background:#1e293b;
    border-radius:18px;
    border:1px solid #334155;
    padding:10px;
}

/* ---------------- Input Fields ---------------- */

.stTextInput input,
.stDateInput input,
.stTimeInput input{
    background:#334155 !important;
    color:white !important;
    border:1px solid #475569 !important;
    border-radius:8px !important;
}

/* ---------------- Select Box ---------------- */

div[data-baseweb="select"] > div{
    background:#334155 !important;
    color:white !important;
    border:1px solid #475569 !important;
    border-radius:8px !important;
}

/* Dropdown */

ul[role="listbox"]{
    background:#334155 !important;
}

ul[role="listbox"] li{
    color:white !important;
}

ul[role="listbox"] li:hover{
    background:#3b82f6 !important;
}

/* ---------------- Buttons ---------------- */

.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button{

    background:#2563EB !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    font-weight:600 !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover{

    background:#1D4ED8 !important;
}

/* ---------------- Progress ---------------- */

.stProgress > div > div{
    background:#2563EB;
}

/* ---------------- Divider ---------------- */

hr{
    border:1px solid #334155;
}

/* ---------------- Caption ---------------- */

.stCaption{
    color:#94a3b8 !important;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)



# ----------------------------
# HEADER
# ----------------------------

left,right = st.columns([8,1])

with left:
    st.title("🏢 Human Resource Management System")
    st.caption("Admin Dashboard")

with right:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(
        "https://ui-avatars.com/api/?name=Admin&background=2563eb&color=fff",
        width=70
    )

st.divider()

# ----------------------------
# WELCOME
# ----------------------------

st.success("👋 Welcome Admin")

st.write(
    "Manage employees, attendance, leave approvals and payroll from one place."
)

st.write("")

# ----------------------------
# DASHBOARD STATS
# ----------------------------

st.subheader("📊 Dashboard Overview")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        label="Employees",
        value="156",
        delta="+12"
    )

with c2:
    st.metric(
        label="Attendance",
        value="142",
        delta="+5%"
    )

with c3:
    st.metric(
        label="Pending Leave",
        value="8",
        delta="-2"
    )

with c4:
    st.metric(
        label="Payroll",
        value="₹24.5L",
        delta="+15%"
    )

st.write("")
st.subheader("🚀 Quick Actions")
st.caption("Open any module from here.")

# ======================================================
# RECENT EMPLOYEES
# ======================================================

st.write("")
st.subheader("👥 Employees")

employees = [
    {
        "ID": "EMP001",
        "Name": "Rahul Sharma",
        "Department": "IT",
        "Designation": "Software Engineer",
        "Status": "🟢 Active"
    },
    {
        "ID": "EMP002",
        "Name": "Priya Das",
        "Department": "HR",
        "Designation": "HR Executive",
        "Status": "🟢 Active"
    },
    {
        "ID": "EMP003",
        "Name": "Amit Roy",
        "Department": "Finance",
        "Designation": "Accountant",
        "Status": "🟡 On Leave"
    },
    {
        "ID": "EMP004",
        "Name": "Sneha Paul",
        "Department": "Sales",
        "Designation": "Sales Manager",
        "Status": "🟢 Active"
    }
]

# -----------------------------
# SEARCH BOX
# -----------------------------

search = st.text_input(
    "🔍 Search Employee",
    placeholder="Search by Employee Name or ID..."
)

# -----------------------------
# FILTER
# -----------------------------

if search == "":
    filtered_employees = employees
else:
    filtered_employees = []

    for employee in employees:

        if (

            search.lower() in employee["ID"].lower()

            or

            search.lower() in employee["Name"].lower()

            or

            search.lower() in employee["Department"].lower()

            or

            search.lower() in employee["Designation"].lower()

            or

            search.lower() in employee["Status"].lower()

):

            filtered_employees.append(employee)

# -----------------------------
# TABLE
# -----------------------------

# Show number of matching employees
st.info(f"🔍 {len(filtered_employees)} employee(s) found.")

# Show employee table
st.dataframe(
    filtered_employees,
    use_container_width=True,
    hide_index=True
)



st.write("")

# Action Buttons
col1, col2, col3 = st.columns(3)

with col1:
    add_employee = st.button(
        "➕ Add Employee",
        use_container_width=True
    )

# ======================================================
# ADD EMPLOYEE FORM
# ======================================================

if add_employee:

    st.write("")
    st.subheader("➕ Add New Employee")

    c1, c2 = st.columns(2)

    with c1:

        emp_id = st.text_input("Employee ID")

        emp_name = st.text_input("Employee Name")

        department = st.selectbox(
            "Department",
            [
                "IT",
                "HR",
                "Finance",
                "Sales",
                "Marketing"
            ]
        )

        designation = st.text_input("Designation")

    with c2:

        email = st.text_input("Email")

        phone = st.text_input("Phone Number")

        joining_date = st.date_input("Joining Date")

        salary = st.number_input(
            "Basic Salary",
            min_value=0,
            step=1000
        )

    st.write("")

    if st.button(
        "💾 Save Employee",
        use_container_width=True
    ):

        st.success("Employee Added Successfully ✅")



with col2:
    edit_employee = st.button(
        "✏️ Edit Employee",
        use_container_width=True
    )

    # ======================================================
# EDIT EMPLOYEE
# ======================================================

if edit_employee:

    st.write("")
    st.subheader("✏️ Edit Employee")

    selected_employee = st.selectbox(
        "Select Employee",
        [
            "Rahul Sharma",
            "Priya Das",
            "Amit Roy",
            "Sneha Paul"
        ]
    )

    c1, c2 = st.columns(2)

    with c1:

        edit_name = st.text_input(
            "Employee Name",
            value=selected_employee
        )

        edit_department = st.selectbox(
            "Department",
            [
                "IT",
                "HR",
                "Finance",
                "Sales"
            ]
        )

        edit_designation = st.text_input(
            "Designation",
            value="Software Engineer"
        )

    with c2:

        edit_email = st.text_input(
            "Email",
            value="employee@gmail.com"
        )

        edit_phone = st.text_input(
            "Phone",
            value="9876543210"
        )

        edit_salary = st.number_input(
            "Salary",
            value=40000,
            step=1000
        )

    st.write("")

    if st.button(
        "✅ Update Employee",
        use_container_width=True
    ):

        st.success("Employee Updated Successfully ✅")



with col3:
    delete_employee = st.button(
        "🗑️ Delete Employee",
        use_container_width=True
    )

    # ======================================================
# DELETE EMPLOYEE
# ======================================================

if delete_employee:

    st.write("")
    st.subheader("🗑️ Delete Employee")

    employee_to_delete = st.selectbox(
        "Select Employee",
        [
            "Rahul Sharma",
            "Priya Das",
            "Amit Roy",
            "Sneha Paul"
        ],
        key="delete_employee_select"
    )

    st.warning(
        f"You are about to delete **{employee_to_delete}**.\n\n"
        "This action cannot be undone."
    )

    confirm_delete = st.checkbox(
        "I understand this action cannot be undone."
    )

    if confirm_delete:

        if st.button(
            "❌ Confirm Delete",
            use_container_width=True
        ):

            st.success(
                f"{employee_to_delete} deleted successfully."
            )



            

        # ======================================================
# EMPLOYEE PROFILE
# ======================================================

st.write("")
st.subheader("👤 Employee Profile")

left, right = st.columns([1, 3])

# ----------------------------
# PROFILE PHOTO
# ----------------------------

with left:

    st.image(
        "https://ui-avatars.com/api/?name=Rahul+Sharma&background=2563eb&color=ffffff&size=256",
        width=180
    )

    st.markdown("### Rahul Sharma")
    st.caption("Software Engineer")

# ----------------------------
# PROFILE DETAILS
# ----------------------------

with right:

    c1, c2 = st.columns(2)

    with c1:
        st.text_input("Employee ID", "EMP001", disabled=True)
        st.text_input("Department", "IT", disabled=True)
        st.text_input("Email", "rahul@gmail.com", disabled=True)
        st.text_input("Phone", "+91 9876543210", disabled=True)

    with c2:
        st.text_input("Joining Date", "15-Jan-2024", disabled=True)
        st.text_input("Manager", "Mr. Arindam Roy", disabled=True)
        st.text_input("Location", "Kolkata", disabled=True)
        st.text_input("Status", "Active", disabled=True)


        st.write("")

st.subheader("💼 Job Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("Designation\n\nSoftware Engineer")

with col2:
    st.info("Employment Type\n\nFull Time")

with col3:
    st.info("Experience\n\n2 Years")



    st.write("")

st.subheader("📞 Contact Information")

st.text_area(
    "Address",
    "Salt Lake Sector V, Kolkata, West Bengal",
    height=90,
    disabled=True
)




st.write("")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("📥 Download Payslip", use_container_width=True):

        st.success("Payslip Download Started")

with col2:

    if st.button("🖨 Print Payslip", use_container_width=True):

        st.success("Preparing Payslip")

with col3:

    if st.button("📧 Email Payslip", use_container_width=True):

        st.success("Payslip Sent Successfully")





st.write("")

st.subheader("📈 Payroll Analytics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Salary Paid", "₹12.4L")

with c2:
    st.metric("Pending Payroll", "₹1.3L")

with c3:
    st.metric("Employees Paid", "148")

with c4:
    st.metric("Pending Employees", "8")





col1,col2 = st.columns(2)

with col1:

    st.markdown("""

<div class="action-box">

<div class="action-title">
👥 Employee Management
</div>

<div class="action-desc">
Add, edit, delete and manage employee records.
</div>

</div>

""", unsafe_allow_html=True)

    st.button("Open Employee Management", use_container_width=True)

with col2:

    st.markdown("""

<div class="action-box">

<div class="action-title">
📅 Attendance
</div>

<div class="action-desc">
Monitor daily attendance and working hours.
</div>

</div>

""", unsafe_allow_html=True)

    st.button("Open Attendance", use_container_width=True)

col3,col4 = st.columns(2)

with col3:

    st.markdown("""

<div class="action-box">

<div class="action-title">
📝 Leave Approval
</div>

<div class="action-desc">
Approve or reject employee leave requests.
</div>

</div>

""", unsafe_allow_html=True)

    st.button("Open Leave Approval", use_container_width=True)

with col4:

    st.markdown("""

<div class="action-box">

<div class="action-title">
💰 Payroll
</div>

<div class="action-desc">
Manage salaries, allowances and deductions.
</div>

</div>

""", unsafe_allow_html=True)

    st.button("Open Payroll", use_container_width=True)
