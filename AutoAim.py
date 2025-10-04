import cv2
import numpy as np
import pyautogui
import win32api
import win32con
from pynput.mouse import Controller

# 自瞄器
class AutoAim:
    def __init__(self):
        # 配置参数
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pyautogui.size() # 屏幕分辨率
        self.CENTER_X, self.CENTER_Y = self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 # 屏幕中心点
        self.TARGET_COLOR_LOWER = np.array([0, 70, 50])
        self.TARGET_COLOR_UPPER = np.array([179, 255, 255])
        self.SMOOTHING_FACTOR = 2  # 鼠标移动平滑系数 2是测试过最好的参数，数字越大步长越大
        self.MIN_TARGET_AREA = 100  # 最小目标面积
        self.mouse = Controller()

    def capture_screen(self):
        screenshot = pyautogui.screenshot()
        return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    def find_targets(self,frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.TARGET_COLOR_LOWER, self.TARGET_COLOR_UPPER)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        targets = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > self.MIN_TARGET_AREA:
                (x, y), radius = cv2.minEnclosingCircle(contour)
                targets.append((int(x), int(y), int(radius)))
        
        return targets, mask

    def move_mouse_smoothly(self,target_x, target_y):
        current_x, current_y = pyautogui.position()

        dx = (target_x - current_x) * self.SMOOTHING_FACTOR
        dy = (target_y - current_y) * self.SMOOTHING_FACTOR
        
        # 移动鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy), 0, 0)