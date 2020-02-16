"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/21 16:24
@File : maingui.py
@Software: PyCharm
@desc:
"""
from tkinter import *
from tkinter.ttk import *

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("主窗体")
        self.geometry("1366x768+100+20")
        self.resizable(0, 0)  # 不允许改变窗口大小
        self.iconbitmap("./img/student.ico")
        self['bg'] = "blue"

        # 加载GUI
        self.setup_UI()
    def setup_UI(self):

        # 设定style
        self.Style01= Style()
        self.Style01.configure("left.TPanedwindow", background="navy")
        self.Style01.configure("right.TPanedwindow", background="skyBlue")
        self.Style01.configure("TButton", font=("微软雅黑", 13, "bold"))
        self.Style01.configure("TLabel", font=("微软雅黑", 13, "bold"))

        # top banner
        self.Login_image = PhotoImage(file="./img/stu_main_top.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack()

        # 左边：按钮区域
        self.Pane_left = PanedWindow(width=200, height=605, style="left.TPanedwindow")
        self.Pane_left.place(x=4, y=158)
        # 添加按钮
        self.Button_add = Button(self.Pane_left, width=12, text="增添学生", style="TButton")
        self.Button_add.place(x=36, y=30)
        self.Button_del = Button(self.Pane_left, width=12, text="删除学生", style="TButton")
        self.Button_del.place(x=36, y=70)
        self.Button_mod = Button(self.Pane_left, width=12, text="修改学生", style="TButton")
        self.Button_mod.place(x=36, y=110)
        self.Button_qur = Button(self.Pane_left, width=12, text="查询学生", style="TButton")
        self.Button_qur.place(x=36, y=150)



        # 右边：查询
        self.Pane_right = PanedWindow(width=1152, height=605, style="right.TPanedwindow")
        self.Pane_right.place(x=210, y=158)

        # LabelFrame控件
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="学生信息查询", width=1130, height=75)
        self.LabelFrame_query.place(x=10, y=10)
        # 添加控件
        self.Label_sno = Label(self.LabelFrame_query, text="学号：")
        self.Entry_sno = Entry(self.LabelFrame_query, font=("微软雅黑", 13, "bold"), width=10)
        self.Label_sno.place(x=10, y=10)
        self.Entry_sno.place(x=60, y=10)

        self.Label_sname = Label(self.LabelFrame_query, text="姓名：")
        self.Entry_sname = Entry(self.LabelFrame_query, font=("微软雅黑", 13, "bold"), width=12)
        self.Label_sname.place(x=185, y=10)
        self.Entry_sname.place(x=240, y=10)

        self.Label_mobile = Label(self.LabelFrame_query, text="电话：")
        self.Entry_mobile = Entry(self.LabelFrame_query, font=("微软雅黑", 13, "bold"), width=15)
        self.Label_mobile.place(x=380, y=10)
        self.Entry_mobile.place(x=430, y=10)

        self.Label_id = Label(self.LabelFrame_query, text="身份证号码：")
        self.Entry_id = Entry(self.LabelFrame_query, font=("微软雅黑", 13, "bold"), width=18)
        self.Label_id.place(x=600, y=10)
        self.Entry_id.place(x=700, y=10)

        self.Button_query = Button(self.LabelFrame_query, text="查询", width=8)
        self.Button_all = Button(self.LabelFrame_query, text="显示全部", width=8)

        self.Button_query.place(x=920, y=8)
        self.Button_all.place(x=1020, y=8)


        # 添加Treeview控件
        self.Tree = Treeview(self.Pane_right, columns=("sno", "name", "gender", "birth", "phone", "e-mail", "address"),
                             show="headings", height=24)
        # 设置每个列的宽度和对齐方式
        self.Tree.column("sno", width=100, anchor="center")
        self.Tree.column("name", width=120, anchor="center")
        self.Tree.column("gender", width=60, anchor="center")
        self.Tree.column("birth", width=120, anchor="center")
        self.Tree.column("phone", width=200, anchor="center")
        self.Tree.column("e-mail", width=300, anchor="center")
        self.Tree.column("address", width=300, anchor="center")
        # 设置表头
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("name", text="姓名")
        self.Tree.heading("gender", text="性别")
        self.Tree.heading("birth", text="出生日期")
        self.Tree.heading("phone", text="手机号")
        self.Tree.heading("e-mail", text="电子邮箱")
        self.Tree.heading("address", text="家庭地址")

        self.Tree.place(x=10, y=95)


if __name__ == '__main__':
    this_main = MainWindow()
    this_main.mainloop()