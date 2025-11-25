#输出九九乘法表
#字符形状输出
#百钱买百鸡
#迭代法解决猴子吃桃问题
#二分迭代法求一元一次方程的根
#牛顿迭代法求一元方程的根
#矩形面积法求积分
#猜数字游戏
#字符串的加密和解密
#蒙特卡洛法求圆周律
import random
n = 1000000
c = 0
for i in range(n):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        c += 1
print(c/n*4)
