def meun():
    meun_info = '''
    ＋－－－－－－－水果管理系统－－－－－－－＋
    ｜ 1）添加水果信息 
    ｜ 2）显示所有水果的信息 
    ｜ 3）删除水果信息 
    ｜ 4）修改水果信息 
    ｜ 5）按含水量高－低显示水果信息 
    ｜ 6）按含水量低－高显示水果信息 
    ｜ 7）按VC含量高－低显示水果信息 
    ｜ 8）按VC含量低－高显示水果信息 
    ｜ 9）保存水果信息到文件（fruit.txt) 
    ｜ 10）从文件中读取水果数据（fruit.txt) 
    ｜ 退出：其他任意按键＜回车＞ 
＋－－－－－－－－－－－－－－－－－－－－－－＋
    '''
    print(meun_info)
# 1）增加水果信息
def addfruit():
    fruits = []
    while True:
        n = input("请输入水果的名称：")
        if not n:
            break
        try:
            w = int(input("请输入含水量："))
            v = int(input("请输入含VC量："))
        except:
            print("输入错误，请输入整数！请重新输入：")
            continue
        fruit = {'name':n,'water':w,'victer':v}
        fruits.append(fruit)
#    print(fruits)
    print("信息录入完毕!")
    return fruits

# 2）显示水果信息
def show_fruits(fruits_info):
    if not fruits_info:
        print("无信息展示")
        return
    print('Name'.center(8), 'Water'.center(12), 'Victer'.center(4))
    for info in fruits_info:
        print(info.get('name').center(8) + str(info.get('water')).center(12) + str(info.get('victer')).center(4))

# 3) 删除水果信息
def del_fruits(fruits_info,del_fruit=''):
    if not del_fruit:
        del_name = input('请输入要删除的水果的名字：')
        for info in fruits_info:
            if del_name == info.get('name'):
                return  info
        raise IndexError('水果名称不匹配，没有找到 %s' % del_name)
    else:
        for info in fruits_info:
            if del_fruit == info.get('name'):
                print("返回将要删除的信息")
                print(info)
                return  info

# 4) 修改水果信息
def edit_fruits(fruits_info):
    edit_name = input('请输入要修改的水果的名字：')
    for info in fruits_info:
        if edit_name == info.get('name'):
            w = int(input('请输入含水量：'))
            v = int(input('请输入VC含量：'))
            edit_info = {'name': edit_name,'water': w,'victer': v}
    return edit_info

# 排序
def sortbywater(*l):
    for x in l:
        return x.get('water')

# 排序
def sortbyvc(*l):
    for x in l:
        return x.get('victer')

# 5）按含水量高 - 低排序
def sort_water_reduce(fruits_info):
    print("按含水量高 - 低排序")
    mit = sorted(fruits_info, key=sortbywater, reverse=True)
    show_fruits(mit)

# 6) 按含水量低 - 高排序
def sort_water_rise(fruits_info):
    print("按含水量低 - 高排序")
    mit = sorted(fruits_info, key=sortbywater)
    show_fruits(mit)

# 7）按VC含量高 - 低排序
def sort_vc_reduce(fruits_info):
    print("按VC含量高 - 低排序")
    mit = sorted(fruits_info, key=sortbyvc, reverse=True)
    show_fruits(mit)

# 8) 按VC含量低 - 高排序
def sort_vc_rise(fruits_info):
    print("按VC含量低 - 高排序")
    mit = sorted(fruits_info, key=sortbyvc)
    show_fruits(mit)


# 9） 保存到文件
def save_info(fruits_info):
    try:
        savefile = open("fruits.txt", 'w')
    except Exception as e:
        savefile = open("fruits.txt", 'x')
    for info in fruits_info:
        savefile.write(str(info) + '\n')
    savefile.close()

# 10) 从文件中读取
def read_info():
    with open("fruits.txt", 'r') as readfile:
        lines = readfile.readlines()
        for line in lines:
            linenew = line[1:-2]
            print(linenew)

def main():
    fruit_info = []
    while True:
        meun()
        num = int(input('请输入：'))
        if not num:
            break
        elif num == 1:
            fruit_info = addfruit()
        elif num == 2:
            show_fruits(fruit_info)
        elif num == 3:
            del_fruit_info = del_fruits(fruit_info)
            fruit_info.remove(del_fruit_info)
        elif num == 4:
            edit_info = edit_fruits(fruit_info)
            print(edit_info)
            fruit_info.remove(del_fruits(fruit_info,del_fruit = edit_info.get('name')))
            fruit_info.append(edit_info)
        elif num == 5:
            sort_water_reduce(fruit_info)
        elif num == 6:
            sort_water_rise(fruit_info)
        elif num == 7:
            sort_vc_reduce(fruit_info)
        elif num == 8:
            sort_vc_rise(fruit_info)
        elif num == 9:
            save_info(fruit_info)
        elif num == 10:
            read_info()
        else:
            break
        input("回车显示菜单")

main()

#L = addfruit()
#show_fruits(L)
#edit_fruits(L)
