import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox

# 全局变量，用于控制连点状态
clicking = False

# 点击间隔，默认为 0.1 秒
click_interval = 0.1

# 开启和停止鼠标连点功能
def start_clicking():
    global clicking
    if clicking:
        messagebox.showinfo("提示", "连点器已经在运行")
        return
    clicking = True
    threading.Thread(target=click_mouse).start()

def stop_clicking():
    global clicking
    clicking = False

# 负责执行鼠标点击的函数
def click_mouse():
    while clicking:
        pyautogui.click()
        time.sleep(click_interval)

# 更新点击间隔
def update_interval():
    global click_interval
    try:
        interval = float(interval_entry.get())
        if interval <= 0:
            raise ValueError
        click_interval = interval
    except ValueError:
        messagebox.showerror("错误", "请输入一个有效的时间间隔（大于 0）")

# GUI 界面
root = tk.Tk()
root.title("鼠标连点器")

# 时间间隔输入框和标签
tk.Label(root, text="点击间隔 (秒):").pack(pady=5)
interval_entry = tk.Entry(root)
interval_entry.pack(pady=5)
interval_entry.insert(0, "0.1")  # 默认间隔时间为 0.1 秒

# 更新间隔按钮
update_btn = tk.Button(root, text="更新间隔", command=update_interval)
update_btn.pack(pady=5)

# 开始和停止按钮
start_btn = tk.Button(root, text="开始连点", command=start_clicking, bg="green", fg="white")
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="停止连点", command=stop_clicking, bg="red", fg="white")
stop_btn.pack(pady=5)

# 运行 GUI
root.mainloop()
