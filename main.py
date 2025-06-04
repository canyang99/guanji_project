import sys
import os
import tkinter as tk

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.gui import ShutdownGUI
from ui.cli import ShutdownCLI

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        ShutdownCLI().run()
    else:
        try:
            root = tk.Tk()
            app = ShutdownGUI(root)
            root.mainloop()
        except tk.TclError:
            print("自动切换到命令行模式")
            ShutdownCLI().run()

if __name__ == "__main__":
    main()