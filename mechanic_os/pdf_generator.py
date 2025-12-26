from fpdf import FPDF
from datetime import datetime
import os

def generate_quotation_pdf(quote, file_path):
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "MECHANIC SHOP QUOTATION", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
    pdf.cell(0, 8, f"Quotation No: Q-{quote['id']}", ln=True)

    pdf.ln(5)

    # Customer info
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Customer Information", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 6, f"Name: {quote['customer_name']}", ln=True)
    pdf.cell(0, 6, f"Phone: {quote['customer_phone']}", ln=True)

    pdf.ln(3)

    # Vehicle
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Vehicle Information", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 6, f"Vehicle: {quote['vehicle_make']} {quote['vehicle_model']}", ln=True)
    pdf.cell(0, 6, f"Registration: {quote['vehicle_reg']}", ln=True)

    pdf.ln(3)

    # Work description
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Work Description", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, quote["description"])

    pdf.ln(3)

    # Costs
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Cost Breakdown", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 6, f"Labour: R {quote['labour_cost']:.2f}", ln=True)
    pdf.cell(0, 6, f"Parts: R {quote['parts_cost']:.2f}", ln=True)

    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, f"TOTAL: R {quote['total_cost']:.2f}", ln=True)

    pdf.ln(8)
    pdf.set_font("Arial", size=9)
    pdf.multi_cell(0, 6, "This quotation is valid for 7 days.")

    pdf.output(file_path)

def generate_invoice_pdf(job, file_path):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "INVOICE", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, f"Invoice Date: {job['completed_at']}", ln=True)
    pdf.cell(0, 8, f"Invoice No: INV-{job['id']}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 6, f"Customer: {job['customer_name']}", ln=True)
    pdf.cell(0, 6, f"Vehicle: {job['vehicle_make']} {job['vehicle_model']} ({job['vehicle_reg']})", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Charges", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 6, f"Labour: R {job['labour_cost']:.2f}", ln=True)
    pdf.cell(0, 6, f"Parts: R {job['parts_cost']:.2f}", ln=True)

    total = job['labour_cost'] + job['parts_cost']
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, f"TOTAL: R {total:.2f}", ln=True)

    pdf.output(file_path)


def generate_completion_report_pdf(job, file_path):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "JOB COMPLETION REPORT", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 6, f"Completed On: {job['completed_at']}", ln=True)
    pdf.cell(0, 6, f"Mechanic: {job['full_name']}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Work Performed", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, job['work_done'])

    pdf.ln(3)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Parts Used", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, job['parts_used'])

    pdf.ln(3)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Future Recommendations", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, job['recommendations'])

    pdf.ln(10)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Mechanic Signature:", ln=True)

    if job.get("signature_path") and os.path.exists(job["signature_path"]):
        pdf.image(job["signature_path"], w=50)
    else:
        pdf.set_font("Arial", size=9)
        pdf.cell(0, 6, "Signature not available", ln=True)

    pdf.output(file_path)
