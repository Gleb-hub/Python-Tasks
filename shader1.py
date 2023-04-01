from math import sqrt
import tkinter as tk

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)

    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0) for c in func(x / w, y / h)]

    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii')  + scr

def func(x, y):
    r1 = 1 - (2 * x - 1.1) ** 2 - (2 * y - 1.1) ** 2
    return r1, 0, 0
    


if __name__ == '__main__':
    label = tk.Label()
    img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()

