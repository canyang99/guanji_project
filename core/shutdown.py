import subprocess
import platform

class SystemShutdown:
    @staticmethod
    def schedule(minutes: float):
        if minutes <= 0:
            raise ValueError("关机时间必须大于0")

        if platform.system() == 'Windows':
            seconds = int(minutes * 60)
            subprocess.run(["shutdown", "/s", "/t", str(seconds)], check=True)
            return f"系统将在 {minutes} 分钟后关机"
        else:
            raise OSError("目前仅支持Windows系统")

    @staticmethod
    def cancel():
        if platform.system() == 'Windows':
            subprocess.run(["shutdown", "/a"], check=True)
            return "关机计划已取消"
        else:
            raise OSError("目前仅支持Windows系统")