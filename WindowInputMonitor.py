import win32gui
from pynput import keyboard, mouse

class WindowInputMonitor:
    def __init__(self, window_title="aimlab_tb"):
        self.window_title = window_title
        self.hwnd = None
        self.keyboard_listener = None
        self.mouse_listener = None
        self.running = False

        self.key_press = None
    def get_window_handle(self):
        """获取窗口句柄"""
        self.hwnd = win32gui.FindWindow(None, self.window_title)
        if self.hwnd == 0:
            print(f"未找到标题为 '{self.window_title}' 的窗口")
            return False
        return True
    def on_key_press(self, key):
        """键盘按下事件"""
        try:
            if win32gui.GetForegroundWindow() == self.hwnd:
                print(f'键盘按下: {key.char}')
                self.key_press = key.char
        except AttributeError:
            if win32gui.GetForegroundWindow() == self.hwnd:
                print(f'特殊键按下: {key}')
                self.key_press = key
            self.key_press = None
    def get_key_press(self):
        """获取键盘按下的键"""
        return self.key_press
    def on_key_release(self, key):
        """键盘释放事件"""
        if win32gui.GetForegroundWindow() == self.hwnd:
            print(f'键盘释放: {key}')
    def on_move(self, x, y):
        """鼠标移动事件"""
        if win32gui.GetForegroundWindow() == self.hwnd:
            print(f'鼠标移动到: ({x}, {y})')
    def on_click(self, x, y, button, pressed):
        """鼠标点击事件"""
        if win32gui.GetForegroundWindow() == self.hwnd:
            action = "按下" if pressed else "释放"
            print(f'鼠标{action}: {button} 在 ({x}, {y})')
    def start(self):
        """启动监控"""
        if not self.get_window_handle():
            return False

        self.running = True
        
        # 启动键盘监听
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release)
        self.keyboard_listener.start()
        
        # 启动鼠标监听
        self.mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click)
        # self.mouse_listener.start()
        
        print(f"开始监控窗口 '{self.window_title}' 的输入...")
        return True
    def stop(self):
        """停止监控"""
        if self.running:
            self.running = False
            if self.keyboard_listener:
                self.keyboard_listener.stop()
            if self.mouse_listener:
                self.mouse_listener.stop()
            print("监控已停止")