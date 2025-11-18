#水仙花数
n1 = int(input())
for x in range (10**(n1 - 1), 10**n):
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
    

