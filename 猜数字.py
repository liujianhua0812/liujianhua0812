import random
a = int(random.uniform(1, 10))
print(a)
e = 1
while e == 1:
    y = int(input("请猜一个10以内的整数："))
    while y != a:
        if y > a:
            print("很遗憾，您猜大了！")
            break

        if y < a:
            print("很遗憾，您猜小了！")
            break
    else:
        print('恭喜您猜对了')
        e = 2



