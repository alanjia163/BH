#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
本代码主要改path目录下的文件名称，如原来为  a.txt，b.txt 改为 1a.txt,2b.txt
'''

import sys
import os


def cur_file_dir():
    # 获取当前文件路径
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def rename(path):
    '''
    文件命名函数
    :param path: 需要改名字的文件夹路径
    :return: None
    '''
    # print("当前目录:",path)
    file_list = os.listdir(path)
    # print(file_list)
    for file, i in zip(file_list, range(1000)):
        # print(file)
        old_dir = os.path.join(path, file)
        filename = os.path.splitext(file)[0]
        # print(filename)
        filetype = os.path.splitext(file)[1]
        # print(filetype)
        old_name = filename + filetype
        print("old name is:", old_name)

        # new_filename = filename.replace('','')  # 这里替换的是重点
        # new_name = new_filename.replace("",'')  # 如果无法一次替换成功，可以进行多次替换

        # *****************************重命名****************************************#
        # 其中i为for i in range(1000)
        new_name = str(i) + old_name
        print("new name is:", new_name)
        new_dir = os.path.join(path, new_name + filetype)  # 新的文件路径
        os.rename(old_dir, new_dir)  # 重命名
        # *****************************重命名****************************************#

        # print("DONE")
        if os.path.isdir(new_dir):
            rename(new_dir)  # 注意这里是重点，这里使用了递归


if __name__ == "__main__":
    # path =cur_file_dir()#获取当前文件夹目录
    path = '.\pg'
    rename(path)
    print("ALL DONE!!!")
