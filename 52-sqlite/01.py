import sqlite3

DB_NAME = 'sqlite_db.db'

# with sqlite3.connect(DB_NAME) as conn:
#     print(conn)
#     print(sqlite3.sqlite_version)

COURSES_TABLE_NAME = 'courses'

# Create table
# with sqlite3.connect(DB_NAME) as conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         students_qty INTEGER DEFAULT 0,
#         reviews_qty INTEGER DEFAULT 0
#     );"""
#     conn.execute(sql_request)
#
# courses = [
#     ('Computer vision', 50, 2),
#     ('Mathematics', 50, 10),
# ]
#
# # Add records to DB
# with sqlite3.connect(DB_NAME) as conn:
#     sql_request = f"INSERT INTO {COURSES_TABLE_NAME} (title, students_qty, reviews_qty) VALUES (?, ?, ?)"
#     for course in courses:
#         conn.execute(sql_request, course)
#     conn.commit()

with sqlite3.connect(DB_NAME) as conn:
    sql_request = f"SELECT * FROM {COURSES_TABLE_NAME}"
    cursor = conn.execute(sql_request)
    print(cursor.fetchall())
    # for row in cursor:
    #     print(row)
