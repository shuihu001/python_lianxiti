"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/19 22:06
@File : login_gui.py
@Software: PyCharm
@desc:
"""
from tkinter import *
from tkinter.ttk import *
import os
from tkinter.messagebox import *
import maingui

class LoginWindow(Tk):
    """
    创建GUI界面及登录方法
    """
    # def __init__(self):
    #     self.frame = Tk()
    #     self.frame.title("登录界面")
    #     self.frame.geometry("600x400")
    #
    # def show(self):
    #     self.frame.mainloop()
    def __init__(self):
        super().__init__()   # 先执行Tk这个类的初始化
        self.title("登录界面")
        self.geometry("560x374+500+300")
        self.resizable(0, 0)  # 不允许改变窗口大小
        self.iconbitmap("./img/student.ico")
        self['bg'] = "#EEEEE0"

        # 加载窗体
        self.setup_UI()

        # 定义变量
        self.file_path ="D:\PYTHON学习\cs231n\python练习题\学生信息管理系统\data\\User.txt"
        self.user_list = []  # 所有用户信息
        self.password_error_times = 0

        # 自动执行文件中账户的加载
        self.load_file_info()
        # showinfo(message=self.user_list)


    def setup_UI(self):
        # ttk中控件使用Style对象设定
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("微软雅黑", 11, "bold"), foreground='Navy', background="#EEEEE0")
        self.Style01.configure("TButton", font=("微软雅黑", 13, "bold"))

        # 创建一个Label标签展示图片
        self.Login_image = PhotoImage(file="./img/school.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack(padx=10, pady=10)

        #  创建Label_user+Entry ---用户名
        self.Label_user = Label(self, text="用户名:", style="user.TLabel").place(x=10, y=330)
        self.var_user = StringVar()
        self.Entry_user = Entry(self, width=10, textvariable=self.var_user, font=("微软雅黑", 10, "bold")).place(x=70, y=327)

        #  创建Label_user+Entry ---密码
        self.Label_password = Label(self, text="密码:", style="user.TLabel").place(x=230, y=330)
        self.var_password = StringVar()
        self.Entry_pasword = Entry(self, width=10, textvariable=self.var_password, show="*", font=("微软雅黑", 10, "bold")).place(x=295, y=327)

        # 创建一个按钮 --登录
        self.Button_login = Button(self, text="登录", width=6, command=self.login).place(x=450, y=327)

    def load_file_info(self):
        """
        加载文件中的用户信息（用户名、密码和状态
        :return:
        """
        if not os.path.exists(self.file_path):
            showinfo("系统消息", "文件名不存在")
        else:
            try:
                with open(file=self.file_path, mode="r",) as fd:
                    current_line = fd.readline()
                    while current_line:
                        temp_list = current_line.split(",")
                        self.user_list.append(temp_list)
                        current_line = fd.readline()
            except:
                showinfo("系题消息","文件读取异常")

    def login(self):
        # 获取输入的用户名和密码
        user = self.var_user.get()
        password = self.var_password.get()
        # showinfo(message="用户名"+user+"\n"+"密码"+password)

        # 实现身份验证
        for index in range(len(self.user_list)):
            # 校验用户名
            if user.strip().lower() == str(self.user_list[index][0]).strip().lower():
                # 判断账户是否禁用
                if "0" in str(self.user_list[index][2]):
                    showinfo("系统消息", "账户异常,已被锁定")
                    break
                else:
                    # 校验密码
                    if password != str(self.user_list[index][1]):
                        self.password_error_times +=1
                        # 判断是否到三次
                        if self.password_error_times>=3:
                            showinfo("系统消息", "密码错误已达三次，账户已锁定！")
                            # 改变状态
                            self.user_list[index][2] = "0\n"
                            # 信息写入文件
                            self.write_file_info()
                        else:
                            showinfo("系统消息", "密码错误")
                        break
                    else:  # 身份验证正确
                        self.password_error_times=0
                        # 加载主窗体
                        # showinfo("系统消息", "登录成功")
                        self.load_main()
                        break

            # 如果校验到最后没有满足匹配的，则用户名不存在
            if index == len(self.user_list) - 1:
                showinfo("系统消息", "用户名不存在")

    def write_file_info(self):
        # 1.清空文件
        try:
            with open(file=self.file_path, mode="w") as fd:
                fd.write("")
            with open(file=self.file_path, mode="a") as fd:
                for item in self.user_list:
                    fd.write(",".join(item))

        except:
            showinfo("系统消息","写入文件异常")
        # 2.写入

    def load_main(self):
        # 1.关闭当前窗体
        self.destroy()
        # 2.打开主窗体
        main_window = maingui.MainWindow()


if __name__ == '__main__':
    this_login = LoginWindow()
    this_login.mainloop()
