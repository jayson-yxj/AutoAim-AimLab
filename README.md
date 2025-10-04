# AutoAim-AimLab-
基于传统视觉的适用于aimlab中的Gridshot(Ultimate)项目自动瞄准设计程序
## 成绩展示
![88de58fcaac83a254a53af7d51839a14](https://github.com/user-attachments/assets/f1a8cd51-04c6-4ffe-b73d-d1b9b92e2f72)

[English](README.md) | 简体中文

一个专为 Aim Lab 中 **Gridshot Ultimate** 模式设计的自动瞄准辅助程序。

## 功能特性

*   **高精度识别**: 利用计算机视觉技术（如 OpenCV）实时捕捉屏幕中的目标。
*   **快速瞄准**: 优化算法实现低延迟的鼠标移动，精准锁定目标。
*   **Gridshot Ultimate 特化**: 专门针对 Aim Lab 的 Gridshot Ultimate 模式进行调优。
*   **可配置性**: 允许用户调整灵敏度、反应时间等参数。

## 安装与使用

###  prerequisites (前置依赖)

确保您的系统已安装以下软件和库：

*   Python 3.8+
*   pip
*   OpenCV
*   NumPy
*   PyAutoGUI / pynput

### 安装步骤

1.  **克隆本仓库**:
```
    git clone https://github.com/jayson-yxj/AutoAim-AimLab-.git
    cd AutoAim-AimLab-
```

2.  **安装Python依赖**:
```
    pip install opencv-python numpy pyautogui win32api win32con
```

3.  **运行程序**:
    先设置窗口名称(main.py)
```
    monitor = WindowInputMonitor("aimlab_tb") # 指定监听窗口
    # 指定你的aimlab的真实窗口名
```
```
    python main.py
```
    *请确保先进入 Aim Lab 并打开 Gridshot Ultimate 模式。*

3.  **快捷按键**:
    *   **o** : 启动自瞄（但不自动射击）。
    *   **p** : 关闭自瞄和自动射击。
    *   **k** : 启动自动射击。
    *   **l** : 关闭自动射击。

### 配置说明

## 配置参数(AutoAim.py)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pyautogui.size() # 屏幕分辨率
        self.CENTER_X, self.CENTER_Y = self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 # 屏幕中心点
        self.TARGET_COLOR_LOWER = np.array([0, 70, 50]) # 目标颜色范围(HSV)
        self.TARGET_COLOR_UPPER = np.array([179, 255, 255])
        self.SMOOTHING_FACTOR = 2  # 鼠标移动平滑系数 2是测试过最好的参数，数字越大步长越大
        self.MIN_TARGET_AREA = 100  # 最小目标面积



## 免责声明

本项目是开源的学习案例，旨在探讨计算机视觉和自动化技术。开发者不对任何滥用此项目的行为负责。使用者请务必遵守游戏规则和用户协议。用于线上游戏的风险需自行承担。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 致谢

*   感谢 Aim Lab 提供了优秀的训练平台。
*   感谢 OpenCV 等开源库提供的强大功能。
