import cv2
from pynput.mouse import Controller, Button
from WindowInputMonitor import WindowInputMonitor
from AutoAim import AutoAim
def main():
    # 自动瞄准开启标志
    AUTOAIM = False
    AUTOSHOOT = False

    monitor = WindowInputMonitor("aimlab_tb") # 指定监听窗口
    monitor.start() # 开启监听
    autoaim = AutoAim() # 自瞄器
    mouse = Controller() # 鼠标控制

    while True:
        frame = autoaim.capture_screen()
        targets, mask = autoaim.find_targets(frame)
        # 获取键盘按下
        key_press = monitor.get_key_press()
        print("type: ",type(key_press))
        print("key: ",(key_press))

        if str(key_press) == 'o' or str(key_press) == 'O':
            print("自动瞄准已开启")
            AUTOAIM = True
        elif str(key_press) == 'p' or str(key_press) == 'p':
            print("自动瞄准已关闭")
            AUTOAIM = False
            AUTOSHOOT = False

        if str(key_press) == 'k' or str(key_press) == 'K':
            print("自动瞄准已开启")
            AUTOSHOOT = True
        elif str(key_press) == 'l' or str(key_press) == 'L':
            print("自动瞄准已关闭")
            AUTOSHOOT = False

        if AUTOAIM :
            # 获取最接近屏幕中心的目标
            if targets:
                closest_target = min(targets, key=lambda t: (t[0]-autoaim.CENTER_X)**2 + (t[1]-autoaim.CENTER_Y)**2)
                target_x, target_y, radius = closest_target
                # 移动鼠标
                autoaim.move_mouse_smoothly(target_x, target_y)
                if AUTOSHOOT:
                    mouse.click(Button.left)
        
        cv2.imshow("frame", frame)
        # cv2.imshow("mask", mask)

        if cv2.waitKey(1) == 27:
            monitor.stop()
            break
    
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()