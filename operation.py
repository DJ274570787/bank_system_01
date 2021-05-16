import os
import pickle
import random

from Card import Card
from Person import Person


class Operation:
    def __init__(self):
        self.load()
        self.usr_dict = {}

    def load(self):
        if os.path.exists("usr.txt"):
            with open("usr.txt", "r")as f:
                self.usr_dict = f.read()
                # self.usr_dict = pickle.load(f)
        else:
            self.usr_dict = {}

    def save(self):
        with open("usr.txt", "w") as f:
            f.write(str(self.usr_dict))
            # pickle.dump(self.usr_dict, f)        #这里要将usr_dict改为self.usr_dict, 不然这里没法调用

    def register(self):
        name = input("请输入姓名：")
        phone_num = input("请输入电话：")
        pwd = self.get_pwd()
        usr_id = self.get_id()
        card = Card(usr_id, pwd, 10)
        person = Person(name, usr_id, phone_num, card)
        self.usr_dict[usr_id] = person               #注意可以等于一个类!!!!!!!!
        print("恭喜您开卡成功！姓名：%s，卡号：%s, 余额%s" % (name, usr_id, card.count))


    def get_pwd(self):
        while True:
            password1 = input("请输入密码：")
            password2 = input("请再次输入密码：")
            if password1 == password2:
                return password1
            else:
                print("输入错误，请重新输入！")

    def get_id(self):
        usr_id1 = random.randint(620000, 629999)#usr_id = random.random(62000, 62999)错
        if usr_id1 not in self.usr_dict:
            return usr_id1

    def show_list(self):
        with open("usr.txt", "rb")as f:
            content = pickle.load(f)
        print(content)


