#Q1
'''
s1 = input()
s2 = input()
if len(s1) < len(s2):  
    s1, s2 = s2, s1
longest = "" 
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        s = s1[i:j]
        if len(s) <= len(longest):
            continue
        if s in s2:
            longest = s
print(longest)
'''
#Q2
'''
s = list(eval(input()))
n = []

for i in range(len(s)):
    if s.count(s[i]) > 1 and s[i] not in n:
        n.append(s[i])

n.sort()

for j in n:
    print(j, end = " ")
'''

#Q3
'''
n = int(input())
l = [0] * (n+1)

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        l[j] = 1 - l[j] 

for i in range(1, n + 1):
    if l[i] == 1:
        print(i, end=" ")
'''
#Q4
'''
n = int(input())
a = 0
s = [0]

for i in range(1, n+1):
    x = a - i
    if x > 0 and x not in s:
        a = x
    else:
        a = a + i
    s.append(a)
print(*s)
'''
'''
r = [0]
c = int(input())
for n in range(1, c + 1):
    t = r[n-1] - n
    if t > 0 and t not in r:
        r.append(t)
    else:
        r.append(r[n-1] + n)
print(*r)
'''

#Q5
'''
n = int(input())
s = 0
a = 1
for i in range(1, n+1):
    a *= i
    s += a
print(f"和为：{s}")
'''

#Q6
'''
m, n = map(int, input().split())
s = 0

for num in range(m, n+1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    mun = int(str(num)[::-1])
    if mun <= 1:
        continue
    is_mun_prime = True
    for i in range(2, int(mun ** 0.5) + 1):
        if mun % i == 0:
            is_mun_prime = False
            break
    if is_mun_prime:
        s += num

print(s)
overtime'''
'''
m, n = map(int, input().split())

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False

i = 2
while i * i <= n:
    if is_prime[i]:
        j = i * i
        while j <= n:
            is_prime[j] = False
            j += i
    i += 1

s = 0
num = m
while num <= n:
    if is_prime[num]:
        mun = 0
        temp = num
        while temp > 0:
            mun = mun * 10 + temp % 10
            temp //= 10
        if mun <= n:
            if is_prime[mun]:
                s += num
        else:
            if mun > 1:
                is_mun_prime = True
                j = 2
                while j * j <= mun:
                    if mun % j == 0:
                        is_mun_prime = False
                        break
                    j += 1
                if is_mun_prime:
                    s += num
    num += 1

print(s)
overtime'''

'''
#获取输入
m, n = map(int, input().split())
#埃氏筛 创建bool列表进行判断
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

prime_set = list(i for i in range(2, n+1) if is_prime[i])

s = 0
for num in range(m, n+1):
    if not is_prime[num]:
        continue
    rev = int(str(num)[::-1])
    if rev <= n:
        if rev in prime_set:
            s += num
    else:
        if rev < 2:
            continue
        is_rev_prime = True
        i = 2
        while i*i <= rev:
            if rev % i == 0:
                is_rev_prime = False
                break
            i += 1
        if is_rev_prime:
            s += num

print(s)
first test answer error?'''
'''
创建列表
筛选法
找到第一个质数,剩下倍数全部筛掉
'''
'''
maxnum = 10**6
primes = [True] * (maxnum + 1)
primes[0] = primes[1] = False
for i in range(2, int(maxnum ** 0.5) + 1):
    if primes[i]:
        primes[i*i:maxnum+1:i] = [False] * len(primes[i*i:maxnum+1:i])
s = 0
for num in range(m , n+1):
    if primes[num]:
        rev = int(str(num)[::-1])
        if primes[rev]:
            s += num
print(s)
'''
#Q7
'''
t = int(input())
for _ in range(t):
    c = int(input())
    ok = 0
    a = 0
    while a * a <= c:
        b = c - a * a
        s = int(b ** 0.5)
        if s * s == b:
            ok = 1
            break
        a += 1
    if ok == 1:
        print("YES")
    else:
        print("NO")
overtime'''

'''
t = int(input())
for i in range(t):
    c = int(input())
    a = 0
    b = int(c ** 0.5)
    ok = 0
    while a <= b:
        s = a*a + b*b
        if s == c:
            ok = 1
            break
        if s > c:
            b -= 1
        else:
            a += 1
    if ok:
        print("YES")
    else:
        print("NO")
'''
'''
math.isqrt()函数
取求得平方根的整数部分
'''


#Q8
'''
n = int(input())
a = list(map(int, input().split()))
a.sort()

b = 0

for k in range(2, n):
    i = 0
    j = k - 1
    while i < j:
        if a[i] + a[j] > a[k]:
            b += (j - i)
            j -= 1
        else:
            i += 1

print(b)
双指针'''

#Q9
'''
n = int(input())
keys = ["if","else","while","for","int","float","return","break","continue"]

for i in range(n):
    s = input()

    if s in keys:
        print("Invalid")
        continue

    if len(s) == 0:
        print("Invalid")
        continue

    c = s[0]
    if '0' <= c <= '9':
        print("Invalid")
        continue

    ok = True
    for c in s:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            continue
        if '0' <= c <= '9':
            continue
        if c == '_':
            continue

        ok = False
        break

    if ok:
        print("Valid")
    else:
        print("Invalid")
'''

#Q10
'''
A = int(input())
n = [0] * 10

for i in range(1, A + 1):
    x = i
    while x > 0:
        j = x % 10
        n[j] += 1
        x //= 10

for i in range(10):
    if i == 9:
        print(i)
    else:
        print(i, end=" ")


for i in range(10):
    if i == 9:
        print(n[i])
    else:
        print(n[i], end=" ")
'''

#Q11
'''
n = int(input())
for _ in range(n):
    a = input().split()
    if len(a) != 3:
        print("ErrorInput")
        continue

    y = int(a[0])
    m = int(a[1])
    d = int(a[2])

    if m < 1 or m > 12:
        print("ErrorInput")
        continue

    md = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        md[2] = 29

    if d < 1 or d > md[m]:
        print("ErrorInput")
        continue

    s = d
    i = 1
    while i < m:
        s += md[i]
        i += 1

    print("Totaldays= " + str(s))
 3rd answer error?'''

#Q12
'''
n = int(input())
a = 0
b = 1
print(a, b, sep=',', end='')

i = 3
while i <= n:
    c = a + b
    print(',', c, sep='', end='')
    a = b
    b = c
    i += 1
'''

#Q13
m, n = map(int, input().split())
c = 0
for x in range(m, n+1):
    d =[]
    for i in range(1, x):
        if x % i == 0:
            d.append(i)

#Q14
#test 求素数逆序数的和
m, n = map(int, input().split())
#埃氏筛 创建bool列表进行判断
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False
#到根号n即可
for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False
#ai 干的 转换成集合储存会快一点
primes = [i for i in range(m, n+1) if is_prime[i]]
prime_set = set(primes)

s = 0
for num in primes:
    #求逆序
    rev = int(str(num)[::-1])
    if rev in prime_set:
        #加到总和中
        s += num

print(s)
