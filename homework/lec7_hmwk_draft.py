#Q1
'''
n = int(input())
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = 0

for i in range(n, 0, -1):
    for j in range(i):
        print(s[p], end=" ")
        p += 1
    print()
'''

'''
n = int(input())
s = ord("A")
for i in range(n, 0, -1):
    for j in range(i)
        print(chr(s), end = " ")
        s += 1
    print()
'''
#Q2
'''
n = int(input())
for i in range(n):
    f = int(input())
    if f % 2 == 1:
        print("0 0")
        continue
    max = f // 2
    max_rabbit = f // 4
    rest_chic = (f - max_rabbit * 4) // 2

    print(rest_chic + max_rabbit, max)
'''

#Q3
'''
n = input()
rev = n[::-1]
while True:
    n = 1
    s = int(n) + int(rev)
    rev = str(s)[::-1]
    if str(s) == rev:
        print(s)
        break
    else:
        n = str(s)
    n += 1
    if n > 8:
        print(0)
        break
'''

#Q4
'''
n = int(input())
for i in range(n):
    z = i + 1
    for j in range(n - i):
        print(z, end=" ")
        z += n - j
    print()

n = int(input())
for i in range(n):
    x = i + 1
    for j in range(n - i):
        print(x, end="")
        if x < 10:
            for _ in range(2):
                print(" ", end="")
        else:
            print(" ", end="")
        x += n - j
    print()
格式错误'''
'''
n = int(input())
for i in range(n):
    x = i + 1
    for j in range(n - i):
        print(x, end="")
        
        if j != (n - i - 1):
            if x < 10:
                for _ in range(2):
                    print(" ", end="")
            else:
                print(" ", end="")
                
        x += n - j
    print()
correct'''

#Q5
n = int(input())
for i in range(n):
    for k in range(n - i):
        nxy = (n - 2*i)**2 - 2*(n - 2*i) + 2
        print(nxy, end="  ")
        for l in range(n - i - 1):
            if l == n - 1:
                break
            if nxy - (l+1) <= 0:
                print(nxy + n,end="  " if l < n-1 else "" )
                
            else:
                print(nxy - (l+1), end="  " if l < n-1 else "" )
    print()
    print(nxy + 1, end="  ")

