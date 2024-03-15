import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() + 1000)) #ชื่อไฟล์เป็นจำนวนวินาที + 1000
    name = 'png/{}.png'.format(name) # {} เป็นชื่อไฟล์ มีฟอร์แมตตามใน()
    img = pyautogui.screenshot(name)
    print(f"Screenshot saved as {name}")

def create_gui():
    # สร้างหน้าต่าง GUI
    root = tk.Tk()
    root.title("Screenshot Tool")

    # สร้างปุ่มถ่ายภาพจอ
    button = tk.Button(root, text="Take Screenshot", command=screenshot)
    button.pack()

    # รัน GUI
    root.mainloop()

if __name__ == "__main__":
    create_gui()