#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import shutil
from tkinter import *
import tkinter.messagebox as messagebox


#初始化容器
root = Tk()
root.title("Android多渠道打包工具")
root.geometry('550x450')


#初始化变量
#渠道文件路径
channle = StringVar()
#打包apk路径
apkSrcFile = StringVar()
#生成apk路径
apkOutputFile = StringVar()
#定制名称打包
singleApkFile = StringVar()
#包名序列号初始值
fromSize = StringVar()
#包名序列号结束值
toSize = StringVar()
#container
frm = Frame(root)
Label(frm, text='根据配置文件多渠道打包').pack(side=TOP)
Label(frm, text='输出apk路径可以为空').pack(side=TOP)
Label(frm, text='默认输出路径为当前文件路径)').pack(side=TOP)
#1
frm_L = Frame(frm)
Label(frm_L, text='渠道路径').pack(side=LEFT)
e = Entry(frm_L, textvariable = channle)
e.pack(side=RIGHT)
frm_L.pack()
#2
frm_R = Frame(frm)
Label(frm_R, text='打包apk路径').pack(side=LEFT)
e2 = Entry(frm_R, textvariable = apkSrcFile)
e2.pack(side=RIGHT)
frm_R.pack()
#3
frm_3 = Frame(frm)
Label(frm_3, text='输出apk路径').pack(side=LEFT)
e3 = Entry(frm_3, textvariable = apkOutputFile)
e3.pack(side=RIGHT)
frm_3.pack()

#输出apk
def outPut():
    channle_content =channle.get()
    apkSrcFile_content=apkSrcFile.get()
    apkOutputFile_content=apkOutputFile.get()
    if channle_content=='':
        messagebox.showinfo('提示','亲，渠道路径不能为空')
        return
    else:
        print('渠道路径'+channle_content)
    if apkSrcFile_content=='':
        messagebox.showinfo('提示','亲，打包apk路径不能为空')
        return
    else:
        print('apk源路径'+apkSrcFile_content)

    if apkOutputFile_content=='':
        # 默认路径为当前文件夹下
        # apkOutputFile_content = os.getcwd()
        print('apk生成路径'+apkOutputFile_content)
    else:
        print('apk生成路径'+apkOutputFile_content)

    command = 'java -jar walle-cli-all.jar batch -f %s %s %s'% (channle_content, apkSrcFile_content,apkOutputFile_content)
    print('打包命令'+command)
    os.system(command)
    print('打包完成')


#4
frm_4 = Frame(frm)
Button(frm_4, text="多渠道打包", command =outPut).pack(side=LEFT)
frm_4.pack()

Label(frm, text='自定义渠道名称打包，可以选填序列值').pack(side=TOP)
Label(frm, text='输入From追加渠道号名称').pack(side=TOP)
Label(frm, text='输入From和To值依次打出此范围内的包（限数字)').pack(side=TOP)

#自定义打包
def outSinglePut():
    apkSrcFile_content = apkSrcFile.get()
    singleApkFile_content = singleApkFile.get()
    apkOutputFile_content = apkOutputFile.get()
    fromSize_content = fromSize.get()
    toSize_content = toSize.get()

    if apkSrcFile_content == '':
        messagebox.showinfo('提示', '亲，打包apk路径不能为空')
        return
    else:
        print('apk源路径' + apkSrcFile_content)

    if singleApkFile_content == '':
        messagebox.showinfo('提示', '亲，渠道名不能为空')
        return
    else:
        print('apk源路径' + apkSrcFile_content)

    if apkOutputFile_content == '':
        # 默认路径为当前文件夹下
        apkOutputFile_content = os.getcwd()+'/'+singleApkFile_content+'.apk'
        print('apk生成路径' + apkOutputFile_content)
    else:
        print('apk生成路径' + apkOutputFile_content)

    if fromSize_content=='' and toSize_content=='':
        commandSingle = 'java -jar walle-cli-all.jar put -c %s %s %s' % (singleApkFile_content, apkSrcFile_content, apkOutputFile_content)
    elif fromSize_content!=''and toSize_content=='':
        commandSingle = 'java -jar walle-cli-all.jar put -c %s %s %s' % (singleApkFile_content+fromSize_content, apkSrcFile_content, apkOutputFile_content)
    elif fromSize_content==''and toSize_content!='':
        commandSingle = 'java -jar walle-cli-all.jar put -c %s %s %s' % (singleApkFile_content+toSize_content, apkSrcFile_content, apkOutputFile_content)
    else:
        order=singleApkFile_content
        sum=''
        apkOutputFile_content = os.getcwd()
        for i in range(int(fromSize_content),(int(toSize_content))):
            if i==(int(toSize_content)-1):
                sum = sum + order + str(i)
            else:
                sum = sum + order + str(i)+','
        print('渠道名'+sum)
        commandSingle = 'java -jar walle-cli-all.jar batch -c %s %s %s' % (sum, apkSrcFile_content,apkOutputFile_content)
    print('自定义打包命令' + commandSingle)
    os.system(commandSingle)
    print('打包完成')
    return

#自定义名称
frm_5 = Frame(frm)
Label(frm_5, text='自定义名称').pack(side=LEFT)
e4 = Entry(frm_5, textvariable = singleApkFile)
e4.pack(side=RIGHT)
frm_5.pack()
#渠道from值
frm_6 = Frame(frm)
Label(frm_6, text='From').pack(side=LEFT)
e5 = Entry(frm_6, textvariable = fromSize)
e5.pack(side=RIGHT)
frm_6.pack()
#渠道to值
frm_7 = Frame(frm)
Label(frm_7, text='To').pack(side=LEFT)
e6 = Entry(frm_7, textvariable = toSize)
e6.pack(side=RIGHT)
frm_7.pack()

Button(frm, text="自定义打包", command =outSinglePut).pack()
frm.pack()
root.mainloop()
