while 1:
    #s = 'hello world, hello python, hello,my new life'
    s = input("请输入一个字符串:")
    l = len(s)
    y = []
    a = input('请输入一个字符：')
    for i in range(l):
        if s[i] == a:
            y.append(i+1)
            if i == l-1:
                break
    if y:
        print('字母', a, '在字符串中位于第', y, '位')
    else:
        print('字母', a, '不在字符串中')
    b = input('是否继续：')
    if b == '否':
        break
