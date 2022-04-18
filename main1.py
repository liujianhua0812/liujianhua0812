while 1:
    login = {'customer1': 123456, 'customer2': 123456, 'customer3': 123456, 'wo': 'liujianhua'}
    innerlogin = {'admin1': 111111, 'admin2': 111111, 'l': 1}
    a = input('请输入您的用户名（注意区分大小写）：')
    if a in login:
        b = input('用户名验证通过，请输入您的密码：')
        b1 = login[a]
        x1 = str(b)
        x2 = str(b1)
        if x1 == x2:
            print('登陆成功，欢迎进入管理系统：')
            from am import *
            sss = sale.sales('/')
        else:
            print('验证失败，密码错误')
            continue
    elif a in innerlogin:
        b = input('管理名验证通过，请输入您的密码：')
        b1 = innerlogin[a]
        x1 = str(b)
        x2 = str(b1)
        if x1 == x2:
            while 1:
                print('登陆成功，欢迎进入管理系统：')
                print('输入1进行宠物数量查询：')
                print('输入2进行宠物卖出操作：')
                print('输入3进行宠物买入操作：')
                print('输入4进行宠物删除操作：')
                c1 = input('请输入您的选择（esc退出）')
                pd = ['1', '2', '3', '4']
                from Acount import *
                if c1 in pd:
                    while c1 == '1':
                        lb = []
                        lb = str(Acount1.kc.keys())
                        print('当前店内有如下品种猫咪：\n', lb)
                        c2 = input('请输入查询的宠物名称（esc返回上级）：')
                        if c2 in Acount1.kc:
                            Acount1(c2, 0).query()
                        elif c2 != 'esc':
                            print('请正确输入猫咪品种名称')
                            continue
                        else:
                            c1 = '200'
                    while c1 == '2':
                        print(Acount1.kc)
                        c2 = input('\n请输入售出猫咪名称（esc返回上级）：')
                        if c2 in Acount1.kc:
                            c3 = input('请输入售出数量：')
                            Acount1(c2, int(c3)).sold()
                        elif c2 != 'esc':
                            print('请正确输入猫咪品种名称')
                            continue
                        else:
                            c1 = '200'
                    while c1 == '3':
                        print(Acount1.kc)
                        c2 = input('\n请输入买入猫咪名称（esc返回上级）：')
                        if c2 != 'esc':
                            c3 = input('请输入买入数量：')
                            Acount1(c2, int(c3)).buy()
                        else:
                            c1 = '200'
                    while c1 == '4':
                        print(Acount1.kc)
                        c2 = input('\n请输入需删除的猫咪名称（esc返回上级）：')
                        if c2 != 'esc' and c2 in Acount1.kc:
                            while 1:
                                c3 = input('请确认是否进行删除该猫咪相关的所有信息（确认后无法撤回操作）：')
                                if c3 == '是':
                                    Acount1(c2, 0).delete()
                                elif c3 == '否':
                                    break
                                else:
                                    print('请输入’是‘或者’否‘')
                                    continue
                        elif c2 != 'esc' and c2 not in Acount1.kc:
                            print('请检查输入是否正确')
                            continue
                        else:
                            c1 = '200'
                elif c1 == 'esc':
                    break
                else:
                    print('请确认您的输入是否有效')
                    continue


        else:
            print('验证失败，密码错误')
            continue


    else:
        print('非法用户，登入失败！')
        continue
