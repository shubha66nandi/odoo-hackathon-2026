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

st.markdown("""
<style>

.stApp{
    background-color:#f5f7fa;
}

h1{
    color:#1565C0;
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
