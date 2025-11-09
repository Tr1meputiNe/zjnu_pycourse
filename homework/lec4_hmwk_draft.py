#Q1
'''
a = list(map(int,input().split(":")))
b = list(map(int,input().split(":")))
t = (b[0] * 60 + b[1] - a[0] * 60 - a[1]) // 30
c = t * 1.5
if t % 30 != 0 or t == 0:
    c += 1.5
print(f"{c:.2f}")
'''

#Q2
'''
a = list(map(float, input().split()))
if a[0] == 0:
    print(f"{(a[1] * 0.923 + a[2]) / 2:.3f}")
elif a[0] == 1:
    print(f"{((a[1] + a[2]) / 2) * 1.08:.3f}")
'''

#Q3
'''
a = int(input())
if a <= 100:
    print(f"{a * 0.1:.2f}")
else:
    print(f"{10 + (a - 100) * 0.08:.2f}")
'''

#Q4
'''
n = int(input())
if n <= 1:
    print(f"{n} indian boy.")
else:
    print(f"{n} indian boys.")
'''

#Q5
'''
y, m = map(int, input().split())

if m < 1 or m > 12:
    print("Error")
else:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print(31)
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print(30)
    elif m == 2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            print(29)
        else:
            print(28)
'''

#Q6
'''
score = int(input())

if score < 0 or score > 100:
    print("输入错误")
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

#Q7
'''
x = int(input())
if x < 1000:
    y = x
elif x < 2000:
    y = x * 0.9
elif x < 3000:
    y = x * 0.8
else:
    y = x * 0.7

print(f"y={y:.2f}")
'''

#Q8
'''
x, y = map(int, input().split(","))
if x == 0 and y == 0:
    print("位于原点")
elif x == 0:
    print("位于y轴")
elif y == 0:
    print("位于x轴")
elif x > 0 and y > 0:
    print("位于第一象限")
elif x < 0 and y > 0:
    print("位于第二象限")
elif x < 0 and y < 0:
    print("位于第三象限")
else:
    print("位于第四象限")
'''

#Q9
'''
a = list(input())
b = 0
n = 0
while a[n] == "0":
    b += 1
    if a[n + 1] == "0":
        n += 1
    else:
        break
print(b)
'''

#Q10
'''
w = float(input())
h = float(input())
value = w / (h ** 2)
print(f"BMI: {value:.2f}")

if value < 18:
    print("超轻")
elif value < 25:
    print("标准")
elif value < 27:
    print("超重")
else:
    print("肥胖")
'''

#Q11
'''
a = input()
b = int(a[4:6])

if b == 12 or b == 1 or b == 2:
    print("winter")
elif b >= 3 and b <= 5:
    print("spring")
elif b >= 6 and b <= 8:
    print("summer")
else:
    print("autumn")
'''

#Q12
'''
h, m = map(int, input().split(":"))
if h == 0:
    print(f"00:{m:02d} AM")
elif h < 12:
    print(f"{h:02d}:{m:02d} AM")
elif h == 12:
    print(f"12:{m:02d} PM")
else:
    print(f"{(h - 12):02d}:{m:02d} PM")
''' 

#Q13
'''
s = input().lower() 
t = []
i = 0

while i < len(s):
    if ('a' <= s[i] <= 'z') or ('0' <= s[i] <= '9'):
        t.append(s[i])
    i += 1
if t == t[::-1]:
    print("yes")
else:
    print("no")
'''

#Q14
'''
a, b = map(int, input().split())
c = 0
d = 1
while d <= a:
    h = a // (d * 10)
    m = (a // d) % 10
    l = a % d
    if m > b:
        c += (h + 1) * d
    elif m == b:
        c += h * d + l + 1
    else:
        c += h * d
    if b == 0:
        c -= d
    d *= 10
print(c)
'''

#Q15
'''
a,b = map(int, input().split())
c = 0
for i in range(a,b+1):
    s = sum(int(d) for d in str(i))
    if s % 7 == 0:
        c += 1
print(c)
'''

#Q16
'''
n = int(input())
a = 2
s = 0
for i in range(n):
    s += a
    a = a ** 0.5 + 1
print(f"{s:.2f}")
'''
