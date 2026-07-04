import streamlit as st
from utils.db import create_tables

# ---------------- Database ---------------- #

create_tables()

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="HRMS",
    page_icon="🏢",
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

st.markdown('<div class="title">🏢 Human Resource Management System</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Manage Employees, Attendance, Payroll and Leave from one place.</div>',
    unsafe_allow_html=True
)

st.write("")

st.success("✅ Database Connected Successfully")

# ---------------- Metrics ---------------- #

c1, c2, c3, c4 = st.columns(4)

c1.metric("👨 Employees", "120")
c2.metric("✅ Present", "108")
c3.metric("📝 Leaves", "12")
c4.metric("💰 Payroll", "₹12.5L")

st.write("")

# ---------------- Quick Actions ---------------- #

st.subheader("🚀 HR Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h2>📅 Attendance</h2>
        <p>Track employee attendance and working hours.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>🏖 Leave Management</h2>
        <p>Approve and manage employee leave requests.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h2>💰 Payroll</h2>
        <p>Generate salary slips and payroll reports.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <h2>📊 Dashboard</h2>
        <p>View HR analytics and company reports.</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <h2>👥 Employee</h2>
        <p>Manage employee information and profiles.</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <h2>⚙ Admin</h2>
        <p>Configure system settings and user roles.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">© 2026 Odoo Hackathon | Human Resource Management System</div>',
    unsafe_allow_html=True
)
