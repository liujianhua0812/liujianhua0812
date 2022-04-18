class Acount1:
    kc = {'金渐层': 20, '银渐层': 50, '布偶': 25}
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def query(self):
        if self.name in Acount1.kc:
            i = Acount1.kc[self.name]
            print(self.name, '当前剩余', i, 'zhi')
            return
        else:
            print('查无信息，', self.name, '信息', '请核对输入')
            return

    def sold(self):
        if self.name in Acount1.kc and Acount1.kc[self.name] > 0:
            Acount1.kc[self.name] -= self.quantity
            print('交易成功，当前宠物剩余：\n', Acount1.kc)
            return
        elif self.name in Acount1.kc and Acount1.kc[self.name] < 0:
            print('该宠物已卖完，请及时补充数量：\n', Acount1.kc)
            return

    def buy(self):
        Acount1.kc[self.name] += self.quantity
        print('宠物库存更新成功：\n', Acount1.kc)
        return

    def delete(self):
        del Acount1.kc[self.name]
        print('宠物库存更新成功：\n', Acount1.kc)
        return








