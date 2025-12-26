import streamlit as st
from quotations import create_quotation
from pdf_generator import generate_quotation_pdf
import os

st.title("📄 New Quotation")

if "user" not in st.session_state or st.session_state.user is None:
    st.error("Please log in.")
    st.stop()

customer_name = st.text_input("Customer Name")
customer_phone = st.text_input("Customer Phone")

vehicle_make = st.text_input("Vehicle Make")
vehicle_model = st.text_input("Vehicle Model")
vehicle_reg = st.text_input("Registration Number")

description = st.text_area("Work Description")

labour_cost = st.number_input("Labour Cost", min_value=0.0)
parts_cost = st.number_input("Parts Cost", min_value=0.0)

total_cost = labour_cost + parts_cost
st.info(f"Total Cost: R {total_cost:.2f}")

if st.button("📄 Generate Quotation"):
    if not customer_name or not description:
        st.error("Customer name and description are required.")
    else:
        quote_data = {
            "mechanic_id": st.session_state.user["id"],
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "vehicle_make": vehicle_make,
            "vehicle_model": vehicle_model,
            "vehicle_reg": vehicle_reg,
            "description": description,
            "labour_cost": labour_cost,
            "parts_cost": parts_cost,
            "total_cost": total_cost
        }

        create_quotation(quote_data)

        # Temporary ID placeholder (simple approach)
        quote_data["id"] = 1

        file_path = f"quotation_{customer_name.replace(' ', '_')}.pdf"
        generate_quotation_pdf(quote_data, file_path)

        with open(file_path, "rb") as f:
            st.download_button(
                "⬇️ Download Quotation PDF",
                f,
                file_name=file_path
            )
