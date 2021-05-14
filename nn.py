# -*- coding = utf-8 -*-
# @Time : 2021/5/9 14:31
# @Author : 韩岳霖
# @File : nn.py
# @software ：PyCharm

# import tkinter
#
# win = tkinter.Tk()
# win.title("python_1")
# win.geometry("500x500+1+1")
#
#
# label = tkinter.Label(win, text="请输入：", font=("宋体", 19))
# label.pack()
#
# e1 = tkinter.Variable()
# entry = tkinter.Entry(win, textvariable=e1)
# entry.pack()
#
#
# label = tkinter.Label(win, text="输出结果:", font=("宋体", 19))
# label.pack()
#
# text = tkinter.Text(win, width=50, height=15)
# text.pack()
#
#
# def func1():
#     with open("usr.txt", "a+") as f:
#         f.write(str(e1.get()))
#         f.flush()
#
#
# def func2():
#     with open("usr.txt", "a+") as f:
#         f.seek(0, 0)
#         content = f.read()
#         text.insert(tkinter.INSERT, content)
#
#
# button1 = tkinter.Button(win, text="保存", command=func1)
# button2 = tkinter.Button(win, text="读取", command=func2)
# button1.pack()
# button2.pack()
#
#
# win.mainloop()
