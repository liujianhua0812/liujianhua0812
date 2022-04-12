
while 1:
    x = input('请输入任意整数：')
    y = int(x)
    i = 1
    while i <= y:
        i += 1
        num = y % i
        if num == 0:
            if i != y:
                print(y, "不是素数")
                break
            else:
                print(y, "是素数")
