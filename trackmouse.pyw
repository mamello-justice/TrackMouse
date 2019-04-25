import pyautogui
from tkinter import *

class TrackMouse:
    def __init__(self, master):
        self.master = master
        self.master.overrideredirect(1)

        self.label = Label(master, font=("Helvetica", 16))
        self.label.bind("<Button-1>", self.leave)
        self.label.pack()

    def update(self):
        x, y = pyautogui.position()
        self.label['text'] = "X:{}  Y:{} ".format(x,y)
        self.master.after(1, lambda: self.update())

    def leave(self, event):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    root.wm_attributes('-alpha', 0.7, '-topmost', 1)
    trackmouse = TrackMouse(root)
    root.after(1, lambda: trackmouse.update())
    root.mainloop()

