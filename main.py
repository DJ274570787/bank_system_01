# -*- codeing = utf-8 -*-
# @Time : 2021/5/14 18:26
# @Author : 韩岳霖
# @File : main.py
# @software ：PyCharm
from view import View
from operation import Operation

v = View()
o = Operation()


def main():
    v.login()
    while True:
        but = int(input("请输入数字："))#but = input("请输入数字：")输出的是字符串
        if but == 1:
            print("11111")
            o.register()
        elif but == 2:
            pass
        elif but == 3:
            pass
        elif but == 4:
            pass
        elif but == 5:
            pass
        elif but == 6:
            pass
        elif but == 7:
            pass
        elif but == 8:
            pass
        elif but == 9:
            o.show_list()
        elif but == 0:
            o.save()
            break


if __name__ == "__main__":  # if __name__ == __main__:忘记冒号
    main()
