import streamlit as st
from jobs import get_completed_jobs
from pdf_generator import generate_invoice_pdf, generate_completion_report_pdf

st.title("🧾 Invoices & Reports")

jobs = get_completed_jobs()

if not jobs:
    st.info("No completed jobs found.")
    st.stop()

for job in jobs:
    job_data = {
    "id": job[0],
    "customer_name": job[1],
    "vehicle_make": job[2],
    "vehicle_model": job[3],
    "vehicle_reg": job[4],
    "work_done": job[5],
    "parts_used": job[6],
    "labour_cost": job[7],
    "parts_cost": job[8],
    "recommendations": job[9],
    "completed_at": job[10],
    "full_name": job[11],
    "signature_path": job[12]}


    st.markdown(f"### Job #{job_data['id']} – {job_data['customer_name']}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"📄 Invoice #{job_data['id']}"):
            path = f"invoice_{job_data['id']}.pdf"
            generate_invoice_pdf(job_data, path)
            st.download_button("⬇️ Download Invoice", open(path, "rb"), file_name=path)

    with col2:
        if st.button(f"🛠️ Completion Report #{job_data['id']}"):
            path = f"report_{job_data['id']}.pdf"
            generate_completion_report_pdf(job_data, path)
            st.download_button("⬇️ Download Report", open(path, "rb"), file_name=path)

    st.divider()
