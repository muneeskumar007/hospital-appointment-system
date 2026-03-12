from app.config import get_db_connection

def create_user(name, email, password, role):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO users (name,email,password,role) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,(name,email,password,role))

    conn.commit()
    cursor.close()
    conn.close()


def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM users WHERE email=%s"
    cursor.execute(sql,(email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user