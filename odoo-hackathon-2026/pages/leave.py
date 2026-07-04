import streamlit as st
import pandas as pd
from datetime import date

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="Leave Management",
    page_icon="🌴",
    layout="wide"
)

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
# ---------------- Header ---------------- #

st.title("🌴 Leave Management System")

st.write("Apply, approve and manage employee leaves.")

st.divider()

# ---------------- Sidebar ---------------- #

st.sidebar.title("Leave Panel")

option=st.sidebar.selectbox(
    "Select",
    [
        "Apply Leave",
        "Leave History",
        "HR Approval"
    ]
)

st.sidebar.success("HR Module")

# ---------------- Dashboard Cards ---------------- #

c1,c2,c3,c4=st.columns(4)

c1.metric("Total Leave","24")
c2.metric("Used","9")
c3.metric("Remaining","15")
c4.metric("Pending","2")

st.divider()

# APPLY LEAVE

if option=="Apply Leave":

    st.subheader("Apply Leave")

    with st.form("leave_form"):

        emp=st.text_input("Employee Name")

        leave_type=st.selectbox(
            "Leave Type",
            [
                "Casual Leave",
                "Sick Leave",
                "Earned Leave",
                "Emergency Leave",
                "Maternity Leave"
            ]
        )

        start=st.date_input(
            "Start Date",
            date.today()
        )

        end=st.date_input(
            "End Date",
            date.today()
        )

        reason=st.text_area("Reason")

        emergency=st.checkbox("Emergency Leave")

        submit=st.form_submit_button("Apply")

    if submit:

        st.success("Leave Applied Successfully ✅")

        st.balloons()

# LEAVE HISTORY

elif option=="Leave History":

    st.subheader("Leave History")

    df=pd.DataFrame({

        "Employee":[
            "Rahul",
            "Priya",
            "Amit",
            "Sneha",
            "Rohit"
        ],

        "Type":[
            "Casual",
            "Sick",
            "Emergency",
            "Earned",
            "Casual"
        ],

        "Days":[
            2,
            3,
            1,
            5,
            4
        ],

        "Status":[
            "Approved",
            "Pending",
            "Rejected",
            "Approved",
            "Approved"
        ]

    })

    search=st.text_input("Search Employee")

    if search:

        df=df[
            df["Employee"].str.contains(
                search,
                case=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

    csv=df.to_csv(index=False)

    st.download_button(

        "Download Report",

        csv,

        "leave_report.csv",

        "text/csv"

    )

# HR APPROVAL

else:

    st.subheader("Pending Leave Requests")

    approval=pd.DataFrame({

        "Employee":[
            "Priya",
            "Rahul",
            "Ankit",
            "Riya"
        ],

        "Leave Type":[
            "Sick",
            "Casual",
            "Emergency",
            "Earned"
        ],

        "Days":[
            2,
            4,
            1,
            3
        ],

        "Status":[
            "Pending",
            "Pending",
            "Pending",
            "Pending"
        ]

    })

    st.dataframe(
        approval,
        use_container_width=True
    )

    employee=st.selectbox(

        "Select Employee",

        approval["Employee"]

    )

    col1,col2=st.columns(2)

    with col1:

        if st.button("Approve"):

            st.success(f"{employee} Leave Approved ✅")

    with col2:

        if st.button("Reject"):

            st.error(f"{employee} Leave Rejected ❌")

st.divider()

st.caption("© Odoo Hackathon 2026 | HR Leave Management")
