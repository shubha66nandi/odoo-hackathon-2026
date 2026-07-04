import streamlit as st
import pandas as pd
from datetime import date

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Attendance Management",
    page_icon="📅",
    layout="wide"
)

# ---------------- CSS ---------------- #

# ---------------- CSS ---------------- #

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
# ---------------- HEADER ---------------- #

st.title("📅 Attendance Management System")

st.write("Manage employee attendance efficiently.")

st.divider()

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("Attendance Panel")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Mark Attendance",
        "Attendance History",
        "Attendance Summary"
    ]
)

st.sidebar.success("HR Attendance Module")

# ---------------- DASHBOARD CARDS ---------------- #

c1, c2, c3, c4 = st.columns(4)

c1.metric("👨 Employees", "120")
c2.metric("✅ Present", "108")
c3.metric("❌ Absent", "8")
c4.metric("⏰ Late", "4")

st.divider()

# MARK ATTENDANCE

if menu == "Mark Attendance":

    st.subheader("Mark Today's Attendance")

    with st.form("attendance_form"):

        employee = st.text_input("Employee Name")

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

        attendance_date = st.date_input(
            "Date",
            date.today()
        )

        status = st.selectbox(
            "Attendance Status",
            [
                "Present",
                "Absent",
                "Late",
                "Half Day"
            ]
        )

        check_in = st.time_input("Check In Time")

        check_out = st.time_input("Check Out Time")

        submit = st.form_submit_button("Submit Attendance")

    if submit:

        st.success("Attendance Marked Successfully ✅")
        st.balloons()

# ATTENDANCE HISTORY

elif menu == "Attendance History":

    st.subheader("Attendance Records")

    df = pd.DataFrame({

        "Employee":[
            "Rahul",
            "Priya",
            "Amit",
            "Sneha",
            "Rohit",
            "Ankit",
            "Neha"
        ],

        "Department":[
            "IT",
            "HR",
            "Finance",
            "Sales",
            "IT",
            "Marketing",
            "HR"
        ],

        "Date":[
            "04-07-2026",
            "04-07-2026",
            "04-07-2026",
            "04-07-2026",
            "04-07-2026",
            "04-07-2026",
            "04-07-2026"
        ],

        "Status":[
            "Present",
            "Late",
            "Present",
            "Absent",
            "Present",
            "Half Day",
            "Present"
        ]

    })

    search = st.text_input("🔍 Search Employee")

    if search:
        df = df[df["Employee"].str.contains(search, case=False)]

    department_filter = st.selectbox(
        "Department Filter",
        ["All", "IT", "HR", "Finance", "Sales", "Marketing"]
    )

    if department_filter != "All":
        df = df[df["Department"] == department_filter]

    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download Attendance Report",
        csv,
        "attendance_report.csv",
        "text/csv"
    )

# ATTENDANCE SUMMARY

else:

    st.subheader("Attendance Summary")

    summary = pd.DataFrame({

        "Status":[
            "Present",
            "Absent",
            "Late",
            "Half Day"
        ],

        "Employees":[
            108,
            8,
            4,
            3
        ]

    })

    st.dataframe(summary, use_container_width=True)

    st.info("Today's Attendance Percentage : 90%")

    st.progress(90)

st.divider()

st.caption("© Odoo Hackathon 2026 | Attendance Management")
