from database import get_connection

def create_quotation(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO quotations (
            mechanic_id, customer_name, customer_phone,
            vehicle_make, vehicle_model, vehicle_reg,
            description, labour_cost, parts_cost, total_cost
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["mechanic_id"],
        data["customer_name"],
        data["customer_phone"],
        data["vehicle_make"],
        data["vehicle_model"],
        data["vehicle_reg"],
        data["description"],
        data["labour_cost"],
        data["parts_cost"],
        data["total_cost"]
    ))

    conn.commit()
    conn.close()
