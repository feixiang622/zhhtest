# 实现拷贝文件


oldfile = open(r"D:\PyCharm\LearnPython\zhhtest.txt", 'rb')

oldname = oldfile.name

name_list = oldname.split("\\")  # 将待路径的文件名分隔成列表

#print(name)
name = name_list[-1]

nameflag_index = name.rfind(".") # 获取后缀名头字符的索引

if nameflag_index > 0:
    newfile = name[:nameflag_index] + "[复制]" + name[nameflag_index:]  # 生成新的文件名称

with open(newfile,'wb') as ff:         # 打开新文件
    for line in oldfile.readlines():   #  旧文件内容写入新闻界
        ff.write(line)

oldfile.close() # 关闭旧文件