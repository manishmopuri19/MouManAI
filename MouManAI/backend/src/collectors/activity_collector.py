from datetime import datetime

from collectors.window_tracker import WindowTracker
from database.models import ActivitySession
from database.repositories.activity_repository import (
    ActivityRepository
)


class ActivityCollector:

    def __init__(self):

        self.tracker = WindowTracker()
        self.repository = ActivityRepository()

        self.current_app = None
        self.current_title = None
        self.session_start = None

    def collect(self):

        active = self.tracker.get_active_window()

        app_name = active["app_name"]
        window_title = active["window_title"]

        if self.current_app is None:

            self.current_app = app_name
            self.current_title = window_title
            self.session_start = datetime.now()

            return

        if app_name != self.current_app:

            now = datetime.now()

            duration = int(
                (now - self.session_start)
                .total_seconds()
            )

            session = ActivitySession(
                app_name=self.current_app,
                window_title=self.current_title,
                start_time=self.session_start,
                end_time=now,
                duration_seconds=duration
            )

            self.repository.save(session)

            self.current_app = app_name
            self.current_title = window_title
            self.session_start = now