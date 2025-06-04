import tkinter as tk
from tkinter import ttk, messagebox
from core.scheduler import ShutdownScheduler


class ShutdownGUI:
    def __init__(self, master):
        self.master = master
        self.scheduler = ShutdownScheduler()
        self.setup_ui()

    def setup_ui(self):
        self.master.title("智能关机工具 v1.0")
        self.master.geometry("300x180")

        frame = ttk.Frame(self.master, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="关机倒计时(分钟):").pack(pady=5)
        self.entry = ttk.Entry(frame, width=15)
        self.entry.pack(pady=5)

        ttk.Button(frame, text="设置关机", command=self.set_shutdown).pack(pady=10)
        ttk.Button(frame, text="取消关机", command=self.cancel_shutdown).pack(pady=5)

    def set_shutdown(self):
        try:
            minutes = float(self.entry.get())
            messagebox.showinfo("成功", self.scheduler.set_shutdown(minutes))
        except ValueError:
            messagebox.showerror("错误", "请输入有效数字")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def cancel_shutdown(self):
        try:
            messagebox.showinfo("成功", self.scheduler.cancel_shutdown())
        except Exception as e:
            messagebox.showerror("错误", str(e))