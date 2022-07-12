import os


def updateFile(old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open("C:/Windows/System3/drivers/etc/hosts", "r") as f:
        for line in f:
            line = line.replace(old_str, new_str)
            file_data += line
    with open("C:/Windows/System32/drivers/etc/hosts", "w") as f:
        f.write(file_data)


def getHost(file, url):
    res = "-1"
    url = str(url)
    with open(file, "r") as f:
        for line in f:
            if line[0] != '#':
                index = line.find(url)
                if index != -1:
                    if line[index - 1] == " ":
                        res = line[:index].strip()
                        # print(line[:index].strip())
    return res

