import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="HRMS Login",
    page_icon="🔐",
    layout="centered"
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
# ---------------- SESSION ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if "username" not in st.session_state:
    st.session_state.username=""

# ---------------- LOGIN PAGE ---------------- #

st.markdown(
"""
<div class='login-box'>
""",
unsafe_allow_html=True
)

st.image(
"https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
width=120
)

st.title("HRMS Login")

st.write("Welcome to Human Resource Management System")

username=st.text_input("Username")

password=st.text_input(
"Password",
type="password"
)

remember=st.checkbox("Remember Me")

login=st.button("Login")

# ---------------- LOGIN ---------------- #

ADMIN_USER="admin"
ADMIN_PASS="admin123"

if login:

    if username==ADMIN_USER and password==ADMIN_PASS:

        st.session_state.logged_in=True
        st.session_state.username=username

        st.success("Login Successful ✅")

        st.balloons()

    else:

        st.error("Invalid Username or Password")

st.markdown("</div>",unsafe_allow_html=True)

# ---------------- AFTER LOGIN ---------------- #

if st.session_state.logged_in:

    st.divider()

    st.success(
        f"Welcome {st.session_state.username}"
    )

    st.info("You can now access Dashboard, Attendance, Leave and Payroll.")

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.page_link(
            "pages/dashboard.py",
            label="Dashboard",
            icon="🏠"
        )

    with c2:
        st.page_link(
            "pages/attendance.py",
            label="Attendance",
            icon="📅"
        )

    with c3:
        st.page_link(
            "pages/leave.py",
            label="Leave",
            icon="🌴"
        )

    with c4:
        st.page_link(
            "pages/payroll.py",
            label="Payroll",
            icon="💰"
        )

    st.divider()

    if st.button("Logout"):

        st.session_state.logged_in=False
        st.session_state.username=""

        st.rerun()

# ---------------- FOOTER ---------------- #

st.markdown(
"""
<div class="footer">
© 2026 Odoo Hackathon | Human Resource Management System
</div>
""",
unsafe_allow_html=True
)
