import tkinter as tk
from tkinter import ttk
import win32api, win32con
import os
from win32com.shell import shell

if shell.IsUserAnAdmin():
    class PyWinDesign:
        def __init__(self, startwin):
            PyWinDesign.xcv = 250

            def addreg():
                if PyWinDesign.xcv == 250:
                    win32api.MessageBox(0, "请进行图像设置!", "提示", win32con.MB_ICONWARNING)
                    return '0'
                print(PyWinDesign.xcv)
                yesorno = '255'
                bj844get = self.bj844.get()
                bj84get = self.bj84.get()
                bj3get = self.bj3.get()
                if bj3get == '':
                    if PyWinDesign.xcv == 'xsd':
                        win32api.MessageBox(0, "输入框不能为空!", "提示", win32con.MB_ICONWARNING)
                        return bj3get
                    else:
                        pass
                else:
                    pass
                if bj844get == '':
                    win32api.MessageBox(0, "输入框不能为空!", "提示", win32con.MB_ICONWARNING)
                    return bj844get
                if bj84get == '':
                    win32api.MessageBox(0, "输入框不能为空!", "提示", win32con.MB_ICONWARNING)
                    return bj84get

                os.popen("reg delete HKEY_CLASSES_ROOT\Directory\Background\shell\\" + bj844get + " /f")
                os.popen("reg add HKEY_CLASSES_ROOT\Directory\Background\shell\\" + bj844get)
                os.popen("reg add HKEY_CLASSES_ROOT\Directory\Background\shell\\" + bj844get + "\command")
                os.popen(
                    "reg add HKEY_CLASSES_ROOT\Directory\Background\shell\\" + bj844get + "\command /t REG_SZ /d " + bj84get)
                print(bj84get)
                if PyWinDesign.xcv == 'xxs':
                    os.popen(
                        "reg add HKEY_CLASSES_ROOT\Directory\Background\shell\\" + bj844get + " /v Icon /t REG_SZ /d " + bj84get)
                elif PyWinDesign.xcv == 'xsd':
                    os.popen(
                        "reg add HKEY_CLASSES_ROOT\Directory\Background\shell\\" + bj844get + " /v Icon /t REG_SZ /d " + bj3get)
                elif PyWinDesign.xcv == 'cv':
                    pass
                else:
                    pass
                win32api.MessageBox(0, "添加完成", "提示", win32con.MB_ICONQUESTION)
            def no():
                PyWinDesign.xcv = 'xxs'
                self.bj3.config(state='disabled')

            def de():
                PyWinDesign.xcv = 'xsd'
                self.bj3.config(state='normal')

            def nox():
                PyWinDesign.xcv = 'cv'
                self.bj3.config(state='disabled')

            self.startwin = startwin
            self.startwin.title('右键菜单添加')
            self.startwin.resizable(width=False, height=False)
            screenwidth = self.startwin.winfo_screenwidth()
            screenheight = self.startwin.winfo_screenheight()
            size = '%dx%d+%d+%d' % (333, 210, (screenwidth - 333) / 2, (screenheight - 210) / 2)
            self.startwin.geometry(size)

            self.bq1bt = tk.StringVar()
            self.bq1bt.set('项目名:')
            self.bq1 = tk.Label(self.startwin, textvariable=self.bq1bt, anchor=tk.W)
            self.bq1.place(x=5, y=11, width=44, height=19)

            self.bj44nr = tk.StringVar()
            self.bj44nr.set('')
            self.bj844 = tk.Entry(self.startwin, textvariable=self.bj44nr, justify=tk.LEFT)
            self.bj844.place(x=54, y=11, width=155, height=20)

            self.bj8nr = tk.StringVar()
            self.bj8nr.set('')
            self.bj84 = tk.Entry(self.startwin, textvariable=self.bj8nr, justify=tk.LEFT)
            self.bj84.place(x=63, y=41, width=198, height=20)

            self.bj3bt = tk.StringVar()
            self.bj3bt.set('使用程序自带图标')
            self.bq3 = tk.Label(self.startwin, textvariable=self.bj3bt, anchor=tk.W)
            self.bq3.place(x=20, y=85, width=99, height=17)

            self.bq4bt = tk.StringVar()
            self.bq4bt.set('指定图标路径:')
            self.bq4 = tk.Label(self.startwin, textvariable=self.bq4bt, anchor=tk.W)
            self.bq4.place(x=20, y=114, width=78, height=21)

            self.bj3nr = tk.StringVar()
            self.bj3nr.set('')
            self.bj3 = tk.Entry(self.startwin, textvariable=self.bj3nr, justify=tk.LEFT, state='disabled')
            self.bj3.place(x=106, y=115, width=179, height=20)

            self.bq5bt = tk.StringVar()
            self.bq5bt.set('不使用图标')
            self.bq5 = tk.Label(self.startwin, textvariable=self.bq5bt, anchor=tk.W)
            self.bq5.place(x=20, y=147, width=64, height=20)

            self.an1bt = tk.StringVar()
            self.an1bt.set('添加')
            self.an1 = tk.Button(self.startwin, textvariable=self.an1bt, command=addreg)
            self.an1.place(x=244, y=177, width=80, height=32)

            self.dxxz = tk.IntVar()
            self.dx3bt = tk.StringVar()
            self.dx3bt.set('')
            self.dx3 = tk.Radiobutton(self.startwin, textvariable=self.dx3bt, variable=self.dxxz, value=15, command=no)
            self.dx3.place(x=2, y=82, width=19, height=24)

            self.dx4bt = tk.StringVar()
            self.dx4bt.set('')
            self.dx4 = tk.Radiobutton(self.startwin, textvariable=self.dx4bt, variable=self.dxxz, value=16, command=de)
            self.dx4.place(x=2, y=114, width=19, height=24)

            self.dx5bt = tk.StringVar()
            self.dx5bt.set('')
            self.dx5 = tk.Radiobutton(self.startwin, textvariable=self.dx5bt, variable=self.dxxz, value=17, command=nox)
            self.dx5.place(x=2, y=144, width=19, height=24)

            self.bq2bt = tk.StringVar()
            self.bq2bt.set('项目路径:')
            self.bq2 = tk.Label(self.startwin, textvariable=self.bq2bt, anchor=tk.W)
            self.bq2.place(x=5, y=41, width=57, height=19)


    if __name__ == '__main__':
        root = tk.Tk()
        app = PyWinDesign(root)
        root.mainloop()
else:
    win32api.MessageBox(0, "请右键->以管理员身份运行该程序!", "提示", win32con.MB_ICONWARNING)
