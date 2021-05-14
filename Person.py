# -*- codeing = utf-8 -*-
# @Time : 2021/5/14 18:26
# @Author : 韩岳霖
# @File : Person.py
# @software ：PyCharm
class Card:
    def __init__(self, card_num, password, count):
        self.card_num = card_num
        self.password = password
        self.count = count
        self.locked_or_not = False     #self.locked_or_not = unclocked错
