sd = {'商品名称：中华烟': '商品价格：100', '商品名称：朗姆酒': '商品价格：200', '商品名称：杜康酒': '商品价格：366'}
k = 1
t = 0
while k == 1:
    print('欢迎进行商店价格管理：')
    print('新增商品信息请输入z')
    print('删除商品信息请输入s')
    print('修改商品信息请输入g')
    print('查询商品信息请输入c')
    a = input('请输入您的选择（输入end退出）：')
    if a == 'z' or a == 'Z':  t = 1
    if a == 's' or a == 'S':  t = 2
    if a == 'g' or a == 'G':  t = 3
    if a == 'c' or a == 'C':  t = 4
    if a == 'end' or a == 'END':
        break

    while t == 1:
        x1 = input('请输入商品名称：')
        x2 = input('请输入商品价格：')
        y1 = '商品名称：' + x1
        y2 = '商品价格：' + x2
        sd[y1] = y2
        a1 = input('请选择是否继续新增：')
        if a1 == '否':
            print('当前系统已保存信息如下：', sd)
            break
        elif a1 == '是':
            continue
        if a1 != '否' and a1 != '是':
            print("请确认输入是否正确！")
        a2 = input('请重新输入您的选择(再次输入错误将返回主菜单)：')
        if a2 != '否' and a2 != '是':
            break
        elif a2 == '是':
            continue
        elif a2 == '否':
            print('当前系统已保存信息如下：', sd)
            break
    while t == 2:
        print(sd)
        x1 = input('请输入需删除的商品名称(返回上一步请输入“返回”)：')
        if x1 == '返回':
            break
        elif x1 != '返回':
            y1 = '商品名称：' + x1
            if y1 in sd:
                del sd[y1]
                print('商品', x1, '已经成功删除！')
                #print(sd)
            else:
                print("请确认输入是否正确！")
                continue
    while t == 3:
        print(sd)
        x1 = input('请输入需修改信息的商品名称(返回上一步请输入“返回”)：')
        if x1 == '返回':
            break
        elif x1 != '返回':
            y1 = '商品名称：' + x1
            if y1 in sd:
                x2 = input('请输入您需要修改的内容（输入’名称‘或’价格‘）：')
                if x2 == '名称':
                    x3 = input('请输入修改后的商品名：')
                    y2 = '商品名称：' + x3
                    #if y2 in sd:
                    sd[y2] = sd[y1]
                    del sd[y1]
                    print('操作成功：', sd)
                    break
                elif x2 == '价格':
                       x3 = input('请输入修改后的价格：')
                       sd[y1] = x3
                       print('操作成功：', sd)
                       break
                else:
                     print('输入有误返回上一级')
                     continue
            else:
                #print(sd)
                print('请确认您的输入是否正确')
                continue
    while t == 4:
        print(sd)
        x1 = input('请输入需查询的商品名称(返回上一步请输入“返回”)：')
        if x1 == '返回':
            break
        elif x1 != '返回':
            y1 = '商品名称：' + x1
            if y1 in sd:
                print(y1, sd[y1])
                # print(sd)
            else:
                print("请确认输入是否正确或无该商品信息！")
                continue








