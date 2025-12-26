# Database module for mechanic_os
import sqlite3

def get_connection():
    return sqlite3.connect("database.db", check_same_thread=False)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Mechanics
    cur.execute("""
    CREATE TABLE IF NOT EXISTS mechanics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        username TEXT UNIQUE,
        password BLOB,
        signature_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Jobs / Work Orders
    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mechanic_id INTEGER,
        customer_name TEXT,
        customer_phone TEXT,
        vehicle_make TEXT,
        vehicle_model TEXT,
        vehicle_reg TEXT,
        work_done TEXT,
        parts_used TEXT,
        labour_cost REAL,
        parts_cost REAL,
        recommendations TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP,
        FOREIGN KEY (mechanic_id) REFERENCES mechanics(id)
    )
    """)
    
    # Quotations
    cur.execute("""
    CREATE TABLE IF NOT EXISTS quotations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mechanic_id INTEGER,
        customer_name TEXT,
        customer_phone TEXT,
        vehicle_make TEXT,
        vehicle_model TEXT,
        vehicle_reg TEXT,
        description TEXT,
        labour_cost REAL,
        parts_cost REAL,
        total_cost REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (mechanic_id) REFERENCES mechanics(id)
    )
    """)

        # Invoices
    cur.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER,
        invoice_number TEXT,
        total_amount REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (job_id) REFERENCES jobs(id)
    )
    """)



    conn.commit()
    conn.close()

