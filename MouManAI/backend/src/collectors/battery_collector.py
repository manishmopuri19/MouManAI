from database.models import BatteryMetric
import psutil
from datetime import datetime
from collectors.base_collector import BaseCollector

class BatteryCollector(BaseCollector):
    def collect(self)->BatteryMetric:
        battery=psutil.sensors_battery()
        if battery is None:
            return BatteryMetric(
                timestamp=datetime.now(),
                battery_percent=0,
                plugged=False,
                seconds_left=-1
            )

        return BatteryMetric(
            timestamps=datetime.now(),
            battery_percent=battery.percent,
            plugged=battery.power_plugged,
            seconds_left=battery.secsleft
        )