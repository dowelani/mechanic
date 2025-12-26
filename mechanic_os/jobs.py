from database import get_connection
from datetime import datetime

def create_job(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO jobs (
            mechanic_id, customer_name, customer_phone,
            vehicle_make, vehicle_model, vehicle_reg,
            work_done, parts_used,
            labour_cost, parts_cost,
            recommendations, status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["mechanic_id"],
        data["customer_name"],
        data["customer_phone"],
        data["vehicle_make"],
        data["vehicle_model"],
        data["vehicle_reg"],
        data["work_done"],
        data["parts_used"],
        data["labour_cost"],
        data["parts_cost"],
        data["recommendations"],
        "COMPLETED"
    ))

    conn.commit()
    conn.close()

def get_completed_jobs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            j.id,
            j.customer_name,
            j.vehicle_make,
            j.vehicle_model,
            j.vehicle_reg,
            j.work_done,
            j.parts_used,
            j.labour_cost,
            j.parts_cost,
            j.recommendations,
            j.completed_at,
            m.full_name,
            m.signature_path
        FROM jobs j
        JOIN mechanics m ON j.mechanic_id = m.id
        WHERE j.status = 'COMPLETED'
        ORDER BY j.completed_at DESC
    """)

    rows = cur.fetchall()
    conn.close()
    return rows
