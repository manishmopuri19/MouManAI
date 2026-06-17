from typing import Optional

from database.connection import get_connection
from database.models import SystemMetric

from .base_repository import BaseRepository


class SystemMetricRepository(BaseRepository):

    def save(
        self,
        metric: SystemMetric
    ) -> None:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO system_metrics
            (
                timestamp,
                cpu_percent,
                ram_percent,
                disk_percent,
                cpu_frequency,
                process_count
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                metric.timestamp.isoformat(),
                metric.cpu_percent,
                metric.ram_percent,
                metric.disk_percent,
                metric.cpu_frequency,
                metric.process_count,
            )
        )

        conn.commit()
        conn.close()

    def get_by_id(
        self,
        item_id: int
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM system_metrics
            WHERE id = ?
            """,
            (item_id,)
        )

        row = cursor.fetchone()

        conn.close()

        return row

    def get_latest(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM system_metrics
            ORDER BY id DESC
            LIMIT 1
            """
        )

        row = cursor.fetchone()

        conn.close()

        return row