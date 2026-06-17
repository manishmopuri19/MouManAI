from database.models import NetworkMetric
import psutil
from collectors.base_collector import BaseCollector
from datetime import datetime

class NetworkCollector(BaseCollector):
    def collect(self)->NetworkMetric:
        network=psutil.net_io_counters()
        
        return NetworkMetric(
            timestamp=datetime.now(),
            bytes_sent=network.bytes_sent,
            bytes_received=network.bytes_received,
            packets_sent=network.packets_sent,
            packets_received=network.packets_received
        )