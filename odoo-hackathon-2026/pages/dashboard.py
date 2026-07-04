import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------ PAGE CONFIG ------------------

st.set_page_config(
    page_title="HRMS Dashboard",
    page_icon="🏢",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------

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

# ------------------ SIDEBAR ------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=120
)

st.sidebar.title("HRMS")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Employees",
        "Attendance",
        "Leave",
        "Payroll",
        "Reports"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("Admin Logged In")

# ------------------ HEADER ------------------

st.title("🏢 Human Resource Management System")

st.write("Welcome back, **Admin** 👋")

st.markdown("---")

# ------------------ KPI CARDS ------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="👨 Employees",
        value="120",
        delta="+5"
    )

with c2:
    st.metric(
        label="✅ Present",
        value="108",
        delta="+3"
    )

with c3:
    st.metric(
        label="🏖 Leave",
        value="8",
        delta="-2"
    )

with c4:
    st.metric(
        label="💰 Payroll",
        value="₹4.8 Lakh",
        delta="+12%"
    )

st.markdown("---")

# ------------------ SAMPLE DATA ------------------

attendance = pd.DataFrame({
    "Month":[
        "Jan","Feb","Mar","Apr",
        "May","Jun"
    ],
    "Attendance":[
        92,
        95,
        90,
        97,
        94,
        98
    ]
})

department = pd.DataFrame({
    "Department":[
        "IT",
        "HR",
        "Finance",
        "Sales"
    ],
    "Employees":[
        45,
        18,
        20,
        37
    ]
})

# ------------------ CHARTS ------------------

left,right = st.columns(2)

with left:

    fig = px.bar(
        attendance,
        x="Month",
        y="Attendance",
        title="Monthly Attendance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    pie = px.pie(
        department,
        values="Employees",
        names="Department",
        title="Department Distribution"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.markdown("---")

# ------------------ EMPLOYEE TABLE ------------------

st.subheader("👨 Employee List")

employee = pd.DataFrame({

    "ID":[101,102,103,104,105],

    "Name":[
        "Rahul",
        "Priya",
        "Amit",
        "Sneha",
        "Rohit"
    ],

    "Department":[
        "IT",
        "HR",
        "Finance",
        "Sales",
        "IT"
    ],

    "Status":[
        "Present",
        "Leave",
        "Present",
        "Present",
        "Absent"
    ]

})

st.dataframe(
    employee,
    use_container_width=True
)

st.markdown("---")

# ------------------ LEAVE REQUESTS ------------------

st.subheader("📄 Pending Leave Requests")

leave = pd.DataFrame({

    "Employee":[
        "Priya",
        "Amit",
        "Rahul"
    ],

    "Type":[
        "Casual",
        "Sick",
        "Emergency"
    ],

    "Status":[
        "Pending",
        "Approved",
        "Pending"
    ]

})

st.table(leave)

st.markdown("---")

# ------------------ FOOTER ------------------

st.info("HRMS Dashboard | Odoo Hackathon 2026")
