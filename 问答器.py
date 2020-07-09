#-*- coding: UTF-8 -*-
import os.path #引入os.path库
from time import * #引入time库
import linecache #引入lincache库
print("正在初始化！")
"""
打开文件
"""
one = open("temu.txt", "w+", encoding='UTF-8') #创建或读取一个索引文件
two = open("daan.txt", "w+", encoding='UTF-8')#创建或读取一个索引文件
"""
打开文件
"""

"""
判断文件是否为空
"""
wenjankong = os.path.getsize("temu.txt")
if wenjankong == 0:
    one.write("以下是题目：")
    one.flush()#缓冲，把改动写入文件
"""
判断文件是否为空
"""

"""
while循环
"""
while True:
    timuinput = input("请输入你的问题>>>") #输入问题
    if timuinput == "退出":#定义退出语句
        one.close()#关闭文件防止占内存
        two.close()#关闭文件防止占内存
        break#退出循环
    """
    定义区
    """
    onelist = []#第一个循环的空列表
    twolist = []#第二个循环的空列表
    number = 1
    """
    定义区
    """
    
    """
    第一个for循环
    """
    for readone in one.readlines():#读取temu.txt的一行内容
        onelist.append(readone)#把内容加入列表
    """
    第一个for循环
    """
	
    """
    第二个for循环
    """
    two.seek(0)
    for readtwo in two.readlines():#读取daan.txt的一行内容
        twolist.append(readtwo)
    """
    第二个for循环
    """
    
    """
    核心区
	"""
    for temu in onelist:
        if timuinput == temu: #判断是否和题目相同
            break
        number += 1
    if number != 1:
        number -= 1
        daanshi = linecache.getline("daan.txt", number)
        print("答案是：", daanshi)
    else:
        buzhidao = input("我不知道，请你告诉我答案（必须正确）：")
        one.writelines(timuinput)
        #one.write("\n\r")
        two.writelines(buzhidao)
        #two.write("\r\n")
        one.flush()#缓冲，把改动写入文件
        two.flush()#缓冲，把改动写入文件
        two.seek(0)
        print(two.read())
"""
核心区
"""

"""
while循环
"""
