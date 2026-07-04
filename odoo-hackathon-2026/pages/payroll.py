import streamlit as st

# ======================================================
# PAYROLL MANAGEMENT
# ======================================================

st.title("💰 Payroll Management")
st.caption("Manage employee salaries, deductions and payroll history")

st.write("")

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

# ======================================================
# PAYROLL COMPLETION
# ======================================================

st.subheader("📌 Payroll Completion")

st.progress(85)

st.caption("85% of employee salaries have been processed for this month.")

st.write("")

# ======================================================
# PAYROLL STATUS
# ======================================================

st.subheader("📊 Payroll Status")

status_data = {
    "Paid": 148,
    "Pending": 8
}

st.bar_chart(status_data)

st.write("")

# ======================================================
# PAYROLL DASHBOARD
# ======================================================

st.subheader("📊 Payroll Dashboard")

card1, card2, card3, card4 = st.columns(4)

with card1:
    st.metric(
        "💰 Gross Salary",
        "₹51,000",
        "+5%"
    )

with card2:
    st.metric(
        "📉 Deductions",
        "₹3,500",
        "-2%"
    )

with card3:
    st.metric(
        "💵 Net Salary",
        "₹47,500",
        "+4%"
    )

with card4:
    st.metric(
        "👥 Employees",
        "156",
        "+12"
    )

st.divider()

# ======================================================
# EMPLOYEE PAYROLL
# ======================================================

st.subheader("👤 Employee Payroll")

# ======================================================
# EMPLOYEE DATA
# ======================================================

employee_data = {

    "Rahul Sharma": {
        "Department": "IT",
        "Designation": "Software Engineer",
        "Salary": 40000
    },

    "Priya Das": {
        "Department": "HR",
        "Designation": "HR Executive",
        "Salary": 35000
    },

    "Amit Roy": {
        "Department": "Finance",
        "Designation": "Accountant",
        "Salary": 45000
    },

    "Sneha Paul": {
        "Department": "Sales",
        "Designation": "Sales Manager",
        "Salary": 38000
    }

}

employee = st.selectbox(
    "Select Employee",
    [
        "Rahul Sharma",
        "Priya Das",
        "Amit Roy",
        "Sneha Paul"
    ]
)
month = st.selectbox(
    "Payroll Month",
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
)

selected = employee_data[employee]

# ======================================================
# EMPLOYEE DETAILS
# ======================================================

col1, col2 = st.columns(2)

with col1:
    st.text_input(
        "Department",
        selected["Department"],
        disabled=True
    )

with col2:
    st.text_input(
        "Designation",
        selected["Designation"],
        disabled=True
    )

st.info(
    f"""
### Payroll Status

**Employee :** {employee}

**Month :** {month}

**Status :** Pending
"""
)

# ======================================================
# SALARY INPUT
# ======================================================

col1, col2 = st.columns(2)

with col1:

    basic_salary = st.number_input(
        "Basic Salary (₹)",
        value=selected["Salary"],
        step=1000
    )

    hra = st.number_input(
        "House Rent Allowance (HRA)",
        value=8000,
        step=500
    )

    bonus = st.number_input(
        "Bonus",
        value=3000,
        step=500
    )

with col2:

    pf = st.number_input(
        "Provident Fund (PF)",
        value=1800,
        step=100
    )

    tax = st.number_input(
        "Professional Tax",
        value=1200,
        step=100
    )

    other = st.number_input(
        "Other Deductions",
        value=500,
        step=100
    )

# ======================================================
# SALARY CALCULATION
# ======================================================

gross_salary = basic_salary + hra + bonus

total_deduction = pf + tax + other

net_salary = gross_salary - total_deduction

st.write("")

# ======================================================
# PAYROLL SUMMARY
# ======================================================

st.subheader("📄 Payroll Summary")
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Gross Salary",
        f"₹ {gross_salary:,.0f}"
    )

with c2:
    st.metric(
        "Total Deduction",
        f"₹ {total_deduction:,.0f}"
    )

with c3:
    st.metric(
        "Net Salary",
        f"₹ {net_salary:,.0f}"
    )

st.write("")

# ======================================================
# SAVE PAYROLL
# ======================================================

if st.button("💾 Save Payroll", use_container_width=True):
    st.success("Payroll Saved Successfully ✅")

# ======================================================
# PAYROLL HISTORY
# ======================================================

st.write("")
st.subheader("📜 Payroll History")

history = [

    {
        "Employee": "Rahul Sharma",
        "Month": "January",
        "Department": "IT",
        "Net Salary": "₹39,500",
        "Status": "Paid"
    },

    {
        "Employee": "Priya Das",
        "Month": "February",
        "Department": "HR",
        "Net Salary": "₹35,200",
        "Status": "Paid"
    },

    {
        "Employee": "Amit Roy",
        "Month": "March",
        "Department": "Finance",
        "Net Salary": "₹43,000",
        "Status": "Pending"
    },

    {
        "Employee": "Sneha Paul",
        "Month": "April",
        "Department": "Sales",
        "Net Salary": "₹37,500",
        "Status": "Paid"
    }

]

# ======================================================
# SEARCH & FILTER
# ======================================================

st.write("")

col1, col2 = st.columns(2)

with col1:

    payroll_search = st.text_input(
        "🔍 Search Employee"
    )

with col2:

    payroll_month = st.selectbox(
        "📅 Filter Month",
        [
            "All",
            "January",
            "February",
            "March",
            "April"
        ]
    )

# ======================================================
# FILTER LOGIC
# ======================================================

filtered_history = []

for row in history:

    employee_match = (
        payroll_search.lower() in row["Employee"].lower()
    )

    month_match = (
        payroll_month == "All"
        or row["Month"] == payroll_month
    )

    if employee_match and month_match:
        filtered_history.append(row)

# ======================================================
# DISPLAY RESULT
# ======================================================

if len(filtered_history) > 0:
    st.success(f"✅ {len(filtered_history)} payroll record(s) found.")
else:
    st.warning("⚠️ No payroll records found.")

st.dataframe(
    filtered_history,
    use_container_width=True,
    hide_index=True
)
