from datetime import datetime
from core.shutdown import SystemShutdown

class ShutdownScheduler:
    def __init__(self):
        self.scheduled_time = None

    def set_shutdown(self, minutes: float):
        confirmation = SystemShutdown.schedule(minutes)
        self.scheduled_time = datetime.now().timestamp() + minutes * 60
        return confirmation

    def cancel_shutdown(self):
        self.scheduled_time = None
        return SystemShutdown.cancel()