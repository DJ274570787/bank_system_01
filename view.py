# -*- codeing = utf-8 -*-
# @Time : 2021/5/14 18:27
# @Author : 韩岳霖
# @File : view.py
# @software ：PyCharm
class View:
    def login(self):  # 忘记self     def login()
        name = input("请输入id：")
        if name == "admin":
            pwd = input("请输入密码：")
            if pwd == "123456":
                self.login_view()
                self.view2()
            else:
                print("密码错误！")
        else:
            print("输入错误！")

    def login_view(self):
        print("--------------------------------------------")
        print("                                            ")
        print("                                            ")
        print("                                            ")
        print("         Welcome to the python bank         ")
        print("                                            ")
        print("                                            ")
        print("                                            ")
        print("--------------------------------------------")

    def view2(self):
        print("--------------------------------------------")
        print("        开户(1)           查询(2)            ")
        print("        存钱(3)           取钱(4)            ")
        print("        转账(5)           改密(6)            ")
        print("        锁卡(7)           查询(8)            ")
        print("        补卡(9)           退出(10)            ")
        print("--------------------------------------------")
        print("sdfsdfdsfsdfdas")
