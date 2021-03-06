import tkinter

root = tkinter.Tk()
root.title('Canvas')
canvas = tkinter.Canvas(root, width=450, height=450)

canvas.create_oval(100,50,150,100, fill='gray90')

x = 125
y = 175
stick = canvas.create_line(x, y-75, x, y)

diff_x = 25
stick_leg1 = canvas.create_line(x, y, x-diff_x, y+50)
stick_leg2 = canvas.create_line(x, y, x+diff_x, y+50)

y=145
stick_arm1 = canvas.create_line(x, y, x-30, y-20)
stick_leg2 = canvas.create_line(x, y, x+30, y-10)

canvas.pack()
root.mainloop()