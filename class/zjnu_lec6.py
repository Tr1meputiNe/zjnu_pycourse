#水仙花数
n1 = int(input())
for x in range (10**(n1 - 1), 10**n1):
    l = map(int, str(x))
    s = 0                           
#for i in l:     s += i**n
    s = sum(i**n1 for i in l)
    if s == x: 
        print(x)
#判断素数
for n2 in range(2, 10000):
    for i in range(2, int(n2**0.5) + 1):
        if n2 % i == 0:
            is_prime = False
            break
    else:
        print(n2)

#哥德巴赫猜想
n = int(input())
for n in range(4, 10001, 2):
    for a in range(2, n // 2 + 1):
        b = n - a 
        #判断a和b是否都为素数
        for i in range(2, int(a)**0.5 + 1):
            if a % i ==0:
                break
        else:
            for i in range(2, int(b)**0.5 + 1):
                if b % i == 0:
                    break
            else:
                print(n, a, b)


#百钱买百鸡
for x in range(1, 21):
    for y in range(1, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5*x + 3*y + z == 100:
            print(x, y, z)

#牛顿迭代法


    


    

