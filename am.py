import Acount
from Acount import*
class Animalmanage:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def jianjie(self):
        print(self.name, "是一种......（此处省略一万字吹嘘），是您居家必备的好伴侣，快带我回家吧")
    def youhhui(self):
        newprice = (self.price)*(0.75)
        print('该品种猫咪最低价格为：', newprice)

# if __name__ == '__main__':
class sale(Animalmanage):
    def sales(self):
        salelist = {'金渐层': 2000, '银渐层': 500, '布偶': 2500}
        kk = 1
        while kk == 1:
            print("欢迎进入宠物店~\n当前店内有如下宠儿供您选择呢~（esc退出）\n", salelist)
            choice = input('请输入您的查询对象：')
            if choice == 'esc' or choice == 'ESC':
                break
            elif choice in salelist:
                c1 = choice
                c2 = salelist[choice]
                sale1 = Animalmanage(c1, c2)
                sale1.jianjie()
                sale1.youhhui()
                a1 = input('您是否购买我呢~：')

                if a1 == '是':
                    a2 = input('您想买几只呢~：')
                    if a2.isdigit() == True:
                        aa2 = int(a2)
                        if aa2 >= 0 and aa2 <= Acount1.kc[choice]:
                            Acount1(choice, aa2).sold()
                            print('好开心，我们回家吧\n')
                        else:
                            print('当前交易无法达成，抱歉')
                            continue
                    else:
                        print('数量格式输入不正确')
                        continue
                elif a1 == '否':
                    print('好难过不能和你生活~')
                    continue
                else:
                    print('请确认您的输入是否正确')
                    continue
            else:
                print('您的输入有误，请重新输入您的选择：')
                continue

















