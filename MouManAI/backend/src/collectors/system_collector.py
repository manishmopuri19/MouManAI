from datetime import datetime
import psutil
from database.models import SystemMetric
from collectors.base_collector import BaseCollector

class SystemCollector(BaseCollector):
    def collect(self)-> SystemMetric:
        cpu_percent=psutil.cpu_percent()
        memory=psutil.virtual_memory()
        disk=psutil.disk_usage("/")
        cpu_frequency=(psutil.cpu_freq().current if psutil.cpu_freq() else 0)
        process_count=len(
            psutil.pids()
        )

        return SystemMetric(
            timestamp=datetime.now(),
            cpu_percent=cpu_percent,
            ram_percent=memory.percent,
            disk_percent=disk.percent,
            cpu_frequency=cpu_frequency,
            process_count=process_count
        )