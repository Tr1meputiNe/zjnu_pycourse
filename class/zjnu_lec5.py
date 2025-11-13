#何意味？
#while循环介绍
#猜数字游戏
#习题课
i = 1
while i <= 100:
    i += 1
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)
#continue用法：结束本次循环
#while else语句 ----若循环未被break()终止 则会运行else内代码
#for else 同理
n = int(input("Input a number: "))
for i in range(2, n):
    if n % i == 0 :
        print("Not Prime")
        break
else:
    print("Primes")