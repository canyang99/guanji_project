from core.scheduler import ShutdownScheduler


class ShutdownCLI:
    def __init__(self):
        self.scheduler = ShutdownScheduler()

    def run(self):
        print("=== 智能关机工具 ===")
        while True:
            print("\n1. 设置定时关机\n2. 取消关机\n3. 退出")
            choice = input("请选择: ")

            if choice == '1':
                self.set_shutdown()
            elif choice == '2':
                self.cancel_shutdown()
            elif choice == '3':
                break
            else:
                print("无效输入")

    def set_shutdown(self):
        try:
            minutes = float(input("输入关机倒计时(分钟): "))
            print("\n" + self.scheduler.set_shutdown(minutes))
            print("提示: 要取消请重新运行程序")
        except ValueError:
            print("错误: 请输入数字")
        except Exception as e:
            print("错误:", str(e))

    def cancel_shutdown(self):
        try:
            print("\n" + self.scheduler.cancel_shutdown())
        except Exception as e:
            print("错误:", str(e))