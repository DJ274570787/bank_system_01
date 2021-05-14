# -*- codeing = utf-8 -*-
# @Time : 2021/5/3 10:04
# @Author : 韩岳霖
# @File : a.py
# @software ：PyCharm
# import tkinter
#
# win = tkinter.Tk()
# win.title("python")
# win.geometry("500x500+1+1")
#
# label = tkinter.Label(win,
#                       text="测试程序",
#                       fg="purple",
#                       anchor="center",
#                       font=("宋体", 19)
#                       )
# label.pack()
#
#
# e1 = tkinter.Variable()
# entry1 = tkinter.Entry(win, textvariable=e1,show="#")
# entry1.pack()
#
#
# def func():
#     print(e1.get())
#
#
# button1 = tkinter.Button(win,
#                          text="保存",
#                          command=func
#                          )
#
# button1.pack()
#
# text = tkinter.Text(win, width=100, height=15)
# text.pack()
#
# """显示按钮"""
#
#
# def func2():
#     text.insert(tkinter.INSERT, e1.get())
#
#
# button2 = tkinter.Button(win, text="显示", command=func2,)
# button2.pack()

# win.mainloop()

# class Bullet:
#     def __init__(self, bullet_count):
#         self.bullet_count = bullet_count
#
#
# class Gun(Bullet):
#     def __init__(self, bullet_count):
#         super().__init__(bullet_count)
#
#     def show_bullet(self):
#         print(self.bullet_count)
#
#     def shoot(self, count):
#         self.bullet_count -= count
#         if self.bullet_count > 0:
#             print("还剩下%s子弹！" % self.bullet_count)
#         else:
#             print("没有子弹了！")
#
#
# class Person(Gun):
#     def __init__(self, bullet_count):
#         super().__init__(bullet_count)
#
#     def fire(self, count):
#         super().shoot(count)
#
#     def change_neil(self):
#         self.bullet_count = 10
#
#     def watch_neil(self):
#         super().show_bullet()
#
#
# p = Person(10)
# p.fire(10)
# p.change_neil()
# p.fire(5)
