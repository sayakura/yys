# coding=utf-8 
import tkinter as tk
import noname

from PIL import Image, ImageTk 

window = tk.Tk()
window.title('Kura的螺旋蛇皮自动肝阴阳师软件')

window.geometry('1000x1000')

render= ImageTk.PhotoImage(file='img.jpg')  

img = tk.Label(window,image=render,width=360, height=240)  
img.image = render  
img.pack() 


label1 = tk.Label(window, 
    text=u'点击下侧按钮选择阴阳师',    # 标签的文字
    font=('Arial', 12),     # 字体和字体大小
    width=30, height=2  # 标签长宽
    )
label1.pack()


var = tk.StringVar()
var.set('点击')
on_hit = False  # 默认初始状态为 False
def hit_me():
	global on_hit 
	if on_hit == False:
		on_hit = True
		var.set('取消运行')
		noname.capture()
		i = ImageTk.PhotoImage(file='test.png')
		img2.configure(image= i)
		img2.image = i
		print("test")

	else:
		on_hit = False
		var.set('点击') # 设置 文字为空
b = tk.Button(window, 
    textvariable=var,      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置


def print_selection():
	print(radio_var.get())


radio_var = tk.StringVar()
radio_var.set('none')


label_radio = tk.Label(window, 
    text=u'你要干哈？',    # 标签的文字
        # 字体和字体大小
    width=30, height=2  # 标签长宽
    )
label_radio.pack()

r1 = tk.Radiobutton(window, text='探索',
                    variable=radio_var, value='A',
                    command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='御魂',
                    variable=radio_var, value='b',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='结界',
                    variable=radio_var, value='c',
                    command=print_selection)
r3.pack()

img2 = tk.Label(window,image='')  
img2.pack(side="bottom", fill="both", expand="yes")
window.mainloop()