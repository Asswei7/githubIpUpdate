import tkinter as tk
from getRemoteHost import getRemoteHost
from getLocalHost import getHost, updateFile


class App:
    flag = False

    def __init__(self, master):
        self.remoteIPValue = getRemoteHost("github.com")
        self.localIPValue = getHost('C:/Windows/System32/drivers/etc/hosts', 'github.com')
        self.remoteIPVar = tk.StringVar()
        self.remoteIPVar.set(self.remoteIPValue)
        self.localIPVar = tk.StringVar()
        self.localIPVar.set(self.localIPValue)
        self.url = tk.StringVar()
        self.url.set("github.com")
        # 设置标题
        master.title("域名获取以及本地更新")
        # 创建一个框架，然后在里面添加一个Button组件
        # 框架的作用一般是在复杂的布局中起到将组件分组的作用
        frame = tk.Frame(master)
        # pack()自动调节组件自身尺寸
        frame.pack()
        tk.Label(master, text='默认的更改域名是github.com').place(x=40, y=40)
        tk.Label(master, text='想要更改的域名:').place(x=50, y=110)
        tk.Button(master, text='更新要查询的域名', command=lambda: self.updateURL(master, self.urlEntry.get())).place(x=330,
                                                                                                              y=110)
        tk.Label(master, text='远程IP:').place(x=50, y=150)
        tk.Label(master, text='本机hosts文件IP:').place(x=50, y=190)
        # 创建一个按钮组件，fg是foreground（前景色）
        # self.showRemote = tk.Button(frame, text="获取远程域名", fg="blue", command=getRemoteHost())

        self.urlEntry = tk.Entry(master, textvariable=self.url)
        self.urlEntry.place(x=160, y=110)
        self.remoteEntry = tk.Entry(master, textvariable=self.remoteIPVar)
        self.remoteEntry.place(x=160, y=150)
        self.localEntry = tk.Entry(master, textvariable=self.localIPVar)
        self.localEntry.place(x=160, y=190)
        self.sameHint = tk.Label(master, text='IP相符，请刷新重试！')
        # self.localIPHint = tk.Label(master, text='现在本地host的IP为:')
        if self.remoteIPValue == self.localIPValue:
            self.sameHint.place(x=100, y=230)
        else:
            tk.Label(master, text='IP更新，是否更改本地主机IP？').place(x=100, y=230)
            # command里的函数带有参数的话，会自动执行
            # tk.Button(master, text='更新本地IP', command=updateFile(localIP, remoteIP)).place(x=200, y=230)
            tk.Button(master, text='更新本地IP',
                      command=lambda: self.updateFile(master, self.localIPValue, self.remoteIPValue, self.url)).place(
                x=290,
                y=230)

    def updateURL(self, master, url):
        self.sameHint.place_forget()
        # print(url)
        # self.sameHint['text'] = ""
        # self.localIPHint['text'] = ""
        result = getRemoteHost(url)
        if result == "该网站无法解析":
            # tk.Label(master, text='该网站无法解析,请换一个域名').place(x=100, y=270)

            self.remoteIPValue = "该网站无法解析,请换一个域名"
            self.remoteIPVar.set(self.remoteIPValue)
            self.remoteEntry.update()
            self.localEntry.delete(0, 'end')
            # self.hint.master.wm_attributes("-disabled", True)
        else:
            self.remoteIPValue = result
            self.remoteIPVar.set(result)
            self.remoteEntry.update()

            # 检测本机hosts文件是否包含该域名的解析
            localIPNewURL = getHost("C:/Windows/System32/drivers/etc/hosts", url)
            print(localIPNewURL)
            # 本地无该映射
            if localIPNewURL == "-1":
                self.localEntry.delete(0, 'end')
                self.localEntry.insert(0, "本地无该条URL映射")
                tk.Button(master, text='添加一条本地映射',
                          command=lambda: self.addURL(master, result, url)).place(x=370, y=190)
            # IP不同
            elif localIPNewURL != result:
                self.localEntry.delete(0, 'end')
                self.localEntry.insert(0, localIPNewURL)
                tk.Button(master, text='是否更新本地IP',
                          command=lambda: self.updateFile(master, localIPNewURL, result, url)).place(x=370, y=190)
            # IP相同
            else:
                self.localEntry.delete(0, 'end')
                self.localEntry.insert(0, localIPNewURL)
                self.sameHint.place(x=100, y=230)
                # tk.Label(master, text='IP相符，请刷新重试！').place(x=100, y=230)

        return

    def addURL(self, master, ip, url):
        with open("C:/Windows/System32/drivers/etc/hosts", "a") as f:
            f.write("\n" + ip + "  " + url)
        f.close()
        self.localEntry.delete(0, 'end')
        self.localEntry.insert(0, ip)

    def updateFile(self, master, old_str, new_str, url):
        file_data = ""
        with open("C:/Windows/System32/drivers/etc/hosts", "r") as f:
            for line in f:
                line = line.replace(old_str, new_str)
                file_data += line
        with open('C:/Windows/System32/drivers/etc/hosts', "w") as f:
            f.write(file_data)

        # ipLocalNew = getHost('C:/Windows/System32/drivers/etc/hosts', url)
        self.localIPVar.set(new_str)
        self.localEntry.update()
        self.localIPHint['text'] += new_str
        self.localIPHint.place(x=100, y=270)
        # tk.Label(master, text='现在的本地IP为：' + new_str).place(x=100, y=270)


# 创建一个toplevel的根窗口，并把它作为参数实例化app对象
root = tk.Tk()
app = App(root)
root.geometry('550x300')

# 开始主事件循环
root.mainloop()
