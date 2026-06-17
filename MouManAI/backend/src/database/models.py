from dataclasses import dataclass
from datetime import datetime

@dataclass

class SystemMetric:
    timestamps:datetime
    cpu_percent:float
    ram_percent: float
    disk_percent:float
    cpu_frequency:float
    process_count:int

@dataclass

class BatteryMetric:
    timestamps: datetime
    battery_percent:float
    plugged:bool
    seconds_left:int

@dataclass
class NetworkMetric:
    timestamp: datetime
    bytes_sent: int
    bytes_received: int
    packets_sent: int
    packets_received: int

@dataclass
class ActivitySession:
    app_name:str
    window_title:str
    start_time:datetime
    end_time:datetime
    duration_seconds:int

@dataclass
class DailyReport:
    repost_date:datetime
    summary:str
    created_at:datetime
