import tkinter as tk
from getRemoteHost import getRemoteHost
from getLocalHost import getHost, updateFile


class App:
    flag = False
    def __init__(self, master, remoteIP, localIP):
        # 设置标题
        master.title("github域名获取")
        # 创建一个框架，然后在里面添加一个Button组件
        # 框架的作用一般是在复杂的布局中起到将组件分组的作用
        frame = tk.Frame(master)
        # pack()自动调节组件自身尺寸
        frame.pack()
        tk.Label(master, text='远程IP:').place(x=50, y=150)
        tk.Label(master, text='本机hosts文件IP:').place(x=50, y=190)
        # 创建一个按钮组件，fg是foreground（前景色）
        # self.showRemote = tk.Button(frame, text="获取远程域名", fg="blue", command=getRemoteHost())
        ipAddress = tk.StringVar()
        ipAddress.set(remoteIP)
        ipLocal = tk.StringVar()
        ipLocal.set(localIP)
        remoteEntry = tk.Entry(master, textvariable=ipAddress)
        remoteEntry.place(x=160, y=150)
        localEntry = tk.Entry(master, textvariable=ipLocal)
        localEntry.place(x=160, y=190)

        if remoteIP == localIP:
            tk.Label(master, text='IP相符，请刷新重试！').place(x=100, y=230)
        else:
            tk.Label(master, text='IP更新，是否更改本地主机IP？').place(x=100, y=230)
            # command里的函数带有参数的话，会自动执行
            # tk.Button(master, text='更新本地IP', command=updateFile(localIP, remoteIP)).place(x=200, y=230)
            tk.Button(master, text='更新本地IP', command=lambda: self.updateFile(master, localIP, remoteIP)).place(x=290, y=230)

    def updateFile(self, master, old_str, new_str):
        file_data = ""
        with open('C:\Windows\System32\drivers\etc\hosts', "r") as f:
            for line in f:
                line = line.replace(old_str, new_str)
                file_data += line
        with open('C:\Windows\System32\drivers\etc\hosts', "w") as f:
            f.write(file_data)

        ipLocal = getHost('C:\Windows\System32\drivers\etc\hosts')
        print("nowipLocal:", ipLocal)
        tk.Label(master, text='现在的本地IP为：' + ipLocal).place(x=100, y=270)


ipAddress = getRemoteHost()
localIP = getHost('C:\Windows\System32\drivers\etc\hosts')
# print("localIP:", localIP)
# 创建一个toplevel的根窗口，并把它作为参数实例化app对象
root = tk.Tk()
app = App(root, ipAddress, localIP)
root.geometry('450x300')

# 开始主事件循环
root.mainloop()
