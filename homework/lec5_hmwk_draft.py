#Q1
'''
while True:
    score = int(input())  # 输入成绩
    if score < 0:
        print("end")
        break
    elif score > 100:
        print("data error!")
    elif score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")
'''

#Q2
'''
n = int(input())

while n >= 10:
    s = 0
    for i in str(n):
        s += int(i)
    n = s

print(n)
'''

#Q3
'''
n = input()
if n[0] == '-':
    n = n[1:]
count = [0] * 10

for c in n:
    count[int(c)] += 1

for i in range(10):
    print(i, ':', count[i])
'''

#Q4
'''
n = 0
s = []

while n != -1:
    n = int(input())
    if n != -1:
        s.append(n)
a = 0  
for i in s:
    if i >= 60:
        a += 1

if len(s) > 0:
    print(f"班级平均成绩为： {sum(s)//len(s)}")
    print(f"及格人数： {a}")
    print(f"不及格人数： {len(s) - a}")
else:
    print(f"班级平均成绩为： 0")
    print(f"及格人数： 0")
    print(f"不及格人数： 0")
'''

#Q5
'''
a, b = map(int, input().split())

c = 1
if a < b:
    d = a
else:
    d = b
    
for i in range(1, d + 1):
    if a % i == 0:
        if b % i == 0:
            c = i


if a > b:
    e = a
else:
    e = b

while True:
    if e % a == 0:
        if e % b == 0:
            break
    e = e + 1

print(c, e)
'''

#Q6
'''
a = int(input())
d = 1

while a > 1:
    a = a // 2
    d = d + 1

print(d)
'''

#Q7
'''
a = int(input())

b = 1               
for i in range(1, a + 1):
    b = b * i

c = []           
d = []              

x = b
y = 2               
while y <= x:
    if x % y == 0:
        yon = 0      
        p = 0
        while x % y == 0:
            x = x // y
            p +=1
        c.append(y)
        d.append(p)
    else:
        y += 1

e = 1
for i in d:
    e = e * (i + 1)
print(e)
'''

#Q8
'''
a = int(input())
s = 0
n = 0

while s <= a:
    n = n + 1
    s = s + n

print(f"{s}=1+2+...+{n}")
'''

#Q9
'''
a = int(input())
b = []

while a != 1:
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1
    b.append(a)

s = str(b)[1:-1]
s = s.replace(" ", "")
print(s)
'''

#Q10
'''
a = int(input())

b = bin(a)
s = 0

for i in b:
    if i == '1':
        s += 1

print(s)
'''