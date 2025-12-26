# Authentication module for mechanic_os
import bcrypt
from database import get_connection

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

def create_user(full_name, username, password, signature_path):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO mechanics (full_name, username, password, signature_path)
        VALUES (?, ?, ?, ?)
        """,
        (full_name, username, hash_password(password), signature_path)
    )

    conn.commit()
    conn.close()

def authenticate(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, full_name, password, signature_path FROM mechanics WHERE username=?",
        (username,)
    )
    user = cur.fetchone()
    conn.close()

    if user and verify_password(password, user[2]):
        return {
            "id": user[0],
            "name": user[1],
            "signature": user[3]
        }
    return None
