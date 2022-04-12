import random
a = int(random.uniform(1, 3))
if a == 1:
    x = "石头"
elif a == 2:
    x = "剪刀"
elif a == 3:
    x = "布"
xx = ['石头', '剪刀', '布']
while 1:
    b = input("请任意输入'石头'、'剪刀'、'布'，开始游戏，退出请输入end：")
    if (b not in xx) and (b != 'end'):
        print('请正确输入：')
    elif (b not in xx) and (b == 'end'):
        print('退出游戏')
        break
    elif (x == "剪刀" and b == "石头") or (x == "石头" and b == "布") or (x == "布" and b == "剪刀"):
        print('电脑出:', x,  '您出:', b, '恭喜您获胜')
    elif (x == "剪刀" and b == "布") or (x == "石头" and b == "剪刀") or (x == "布" and b == "石头"):
        print('电脑出:', x,  '您出:', b, '请再接再厉')
    elif x == b:
        print('电脑出:', x,  '您出:', b, '平手~')
