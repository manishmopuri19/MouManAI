from connection import get_connection


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT NOT NULL,

        cpu_percent REAL,

        ram_percent REAL,

        disk_percent REAL,

        cpu_frequency REAL,

        process_count INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS battery_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT NOT NULL,

        battery_percent REAL,

        plugged INTEGER,

        seconds_left INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        app_name TEXT,

        window_title TEXT,

        start_time TEXT,

        end_time TEXT,

        duration_seconds INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        report_date TEXT,

        summary TEXT,

        created_at TEXT
    )
    """)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    initialize_database()