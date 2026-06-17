import win32gui
import win32process

import psutil


class WindowTracker:

    def get_active_window(self):

        hwnd = win32gui.GetForegroundWindow()

        window_title = win32gui.GetWindowText(hwnd)

        _, pid = (
            win32process
            .GetWindowThreadProcessId(hwnd)
        )

        try:

            process = psutil.Process(pid)

            app_name = process.name()

        except Exception:

            app_name = "Unknown"

        return {
            "app_name": app_name,
            "window_title": window_title,
            "pid": pid
        }