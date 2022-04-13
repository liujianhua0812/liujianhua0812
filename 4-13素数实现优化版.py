y = []
while 1:
    a = int(input('请输入区间起点(起点应大于1)：'))
    b = int(input('请输入区间终点（终点应大于起点）：'))
    if a >= b:
        print('请检查输入是否正确（遵循 a < b原则）')
    else:
        for i in range(a, b + 1):
            for j in range(2, i):
                k = i % j
                if k == 0:
                    break
            else:
                y.append(i)
        print('区间', a, '-', 'b', '内存在如下素数：', y)
    c = input('请选择是否继续：')
    if c == '否':
      break



