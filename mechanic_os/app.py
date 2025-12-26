import streamlit as st
import os
from PIL import Image
from database import create_tables
from auth import create_user, authenticate

st.set_page_config(page_title="Mechanic OS", layout="centered")
create_tables()

SIGNATURE_DIR = "assets/signatures"
os.makedirs(SIGNATURE_DIR, exist_ok=True)

if "user" not in st.session_state:
    st.session_state.user = None

st.title("🔧 Mechanic Shop Operating System")

# ---------------- LOGIN / REGISTER ----------------
if st.session_state.user is None:
    tab1, tab2 = st.tabs(["Login", "Register"])

    # ---------- LOGIN ----------
    with tab1:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = authenticate(username, password)
            if user:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid username or password")

    # ---------- REGISTER ----------
    with tab2:
        st.subheader("Register Mechanic")

        full_name = st.text_input("Full Name")
        new_username = st.text_input("Username", key="register_username")
        new_password = st.text_input("Password", type="password", key="register_password")

        st.markdown("### ✍️ Upload Signature Image")
        signature_file = st.file_uploader(
            "Upload a clear image of your signature (PNG or JPG)",
            type=["png", "jpg", "jpeg"]
        )

        if st.button("Create Account"):
            if not full_name or not new_username or not new_password:
                st.error("All fields are required")
            elif signature_file is None:
                st.error("Signature image is required")
            else:
                image = Image.open(signature_file)
                signature_path = f"{SIGNATURE_DIR}/{new_username}.png"
                image.save(signature_path)

                create_user(
                    full_name,
                    new_username,
                    new_password,
                    signature_path
                )

                st.success("Account created successfully. You can now log in.")

# ---------------- DASHBOARD ----------------
else:
    st.success(f"Welcome, {st.session_state.user['name']}")

    st.markdown("### Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("➕ New Job"):
            st.switch_page("pages/job_page.py")

    with col2:
        if st.button("📄 Quotations"):
            st.switch_page("pages/quotation_page.py")

    with col3:
        if st.button("🧾 Invoices and Report"):
            st.switch_page("pages/invoice_report_page.py")

    st.divider()

    st.markdown("### Stored Signature")
    if st.session_state.user["signature"]:
        st.image(st.session_state.user["signature"], width=300)

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()

