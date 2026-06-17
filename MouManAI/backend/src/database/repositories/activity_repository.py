from database.connection import get_connection

from database.models.activity_session import ActivitySession


class ActivityRepository:

    def save(
        self,
        session: ActivitySession
    ) -> None:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO activity_sessions
            (
                app_name,
                window_title,
                start_time,
                end_time,
                duration_seconds
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                session.app_name,
                session.window_title,
                session.start_time.isoformat(),
                session.end_time.isoformat(),
                session.duration_seconds
            )
        )

        conn.commit()

        conn.close()