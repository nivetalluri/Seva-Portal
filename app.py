import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/auth"

st.set_page_config(page_title="Seva Portal", layout="wide")

def signup_page():
    st.title("Seva Portal - Sign Up")
    name = st.text_input("Name", key="signup_name")
    phone = st.text_input("Phone Number", key="signup_phone")
    email = st.text_input("Email ID", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_pass")
    if st.button("Sign Up"):
        if not all([name, phone, email, password]):
            st.error("All fields are required")
        else:
            res = requests.post(f"{API_URL}/signup", json={
                "name": name,
                "phone": phone,
                "email": email,
                "password": password
            })
            if res.status_code == 200:
                st.success("Signup successful! Please login.")
                st.session_state.page = "login"
            else:
                st.error(res.json()["detail"])

def login_page():
    st.title("Seva Portal - Login")
    user = st.text_input("Phone/Email", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        if not all([user, password]):
            st.error("All fields are required")
        else:
            res = requests.post(f"{API_URL}/login", json={
                "phone_or_email": user,
                "password": password
            })
            if res.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.page = "dashboard"
            else:
                st.error("Invalid credentials")

def dashboard():
    st.title("Seva Portal - Dashboard")
    menu = ["Home", "About", "Updates", "Evaluate", "Profile"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write(f"Welcome {st.session_state.user}! Seva Portal helps you discover government schemes you are eligible for.")
    elif choice == "About":
        st.write("Seva Portal evaluates suitable government schemes based on your personal information using Qdrant vector store.")
    elif choice == "Updates":
        st.write("Latest updates and news about government schemes will appear here.")
    elif choice == "Evaluate":
        st.subheader("Evaluate Suitable Schemes")
        id_type = st.selectbox("Select Government ID", ["Aadhaar", "PAN", "Voter ID"])
        age = st.number_input("Age", min_value=1, max_value=120)
        income = st.number_input("Monthly Income", min_value=0)
        if st.button("Evaluate"):
            user_payload = {"email": st.session_state.user, "id_type": id_type, "age": age, "income": income}
            res = requests.post("http://127.0.0.1:8000/evaluate", json=user_payload)
            if res.status_code == 200:
                st.success("Suitable Schemes:")
                for scheme in res.json()["schemes"]:
                    st.write(f"- {scheme}")
    elif choice == "Profile":
        st.write(f"User: {st.session_state.user}")
        if st.button("Logout"):
            st.session_state.clear()

# Session state to manage navigation
if "page" not in st.session_state:
    st.session_state.page = "signup"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.page == "signup":
    signup_page()
elif st.session_state.page == "login":
    login_page()
elif st.session_state.page == "dashboard":
    if st.session_state.logged_in:
        dashboard()
    else:
        st.session_state.page = "login"
        login_page()
