import streamlit as st
from jobs import create_job
from datetime import datetime

st.title("🛠️ New Job / Work Order")

if "user" not in st.session_state or st.session_state.user is None:
    st.error("Please log in first.")
    st.stop()

st.markdown("### Customer Information")
customer_name = st.text_input("Customer Name")
customer_phone = st.text_input("Customer Phone")

st.markdown("### Vehicle Information")
vehicle_make = st.text_input("Vehicle Make")
vehicle_model = st.text_input("Vehicle Model")
vehicle_reg = st.text_input("Registration Number")

st.markdown("### Work Details")
work_done = st.text_area("Work Performed")
parts_used = st.text_area("Parts Used")

labour_cost = st.number_input("Labour Cost", min_value=0.0)
parts_cost = st.number_input("Parts Cost", min_value=0.0)

st.markdown("### Future Recommendations")
recommendations = st.text_area("Recommendations for Customer")

st.markdown("### Mechanic Confirmation")
st.image(st.session_state.user["signature"], width=250)
st.caption("By submitting, you confirm this work was completed by you.")

if st.button("✅ Complete Job"):
    if not customer_name or not work_done:
        st.error("Customer name and work performed are required.")
    else:
        create_job({
            "mechanic_id": st.session_state.user["id"],
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "vehicle_make": vehicle_make,
            "vehicle_model": vehicle_model,
            "vehicle_reg": vehicle_reg,
            "work_done": work_done,
            "parts_used": parts_used,
            "labour_cost": labour_cost,
            "parts_cost": parts_cost,
            "recommendations": recommendations
        })

        st.success("Job completed and recorded successfully.")
