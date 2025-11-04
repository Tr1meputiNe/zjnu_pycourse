#Q1
'''
a = int(input())
list1 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print(list1[a - 1])
'''

#Q2
'''
a = list(input().split())
print(f"count = {len(a)}")
'''

#Q3
'''
a = list(map(int, input()))
b = a[0]
n = 0
for i in a:
    if i > b:
        b = i
        n += 1
print(f"{b} {n}")
''' 
'''
s = input()
m1 = max(s)
print(m1, s.find(m1))'''
#Q4
'''
if (a[1] + m) >= 60:
    a[0] = (a[0] + h + 1) % 24
    a[1] = (a[1] + m) % 60
#add
else:
    a[0] = (a[0] + h) % 24
    a[1] = a[1] + m
print(f"{a[0]:02d}:{a[1]:02d}")

add = 
elif (a[1] + m) < 0:
    a[0] = (a[0] + h - 1) % 24
    a[1] = (a[1] + m + 60) % 60

'''
#corrected version
'''
a = list(map(int, input().split(":")))
b = int(input())
t = a[0] * 60 + a[1] + b
a[0] = t // 60
a[1] = t % 60

print(f"{a[0]:02d}:{a[1]:02d}")
'''

#Q5
'''
n = int(input())
a = list(map(int, input().split()))
m = a[0]
p = 0
for i in range(1, n):
    if a[i] > m:
        m = a[i]
        p = i
print(m, p)
'''
'''
index()函数
n = int(input())
a = list(map(int, input().split()))
i = a.index(max(a))
print(a[i], i)
'''

#Q6
'''
a = list(map(float, input().split()))
print(f"最高分:{max(a):.2f}\n最低分:{min(a):.2f}\n平均分:{sum(a)/len(a):.2f}")
'''

#Q7
'''
a = list(map(int, input().split()))
print(sum(a)//len(a), max(a), min(a))
'''

#Q8
'''
s = input().strip("[]")
a = list(map(int, s.split(",")))
print(f"length={len(a)}")
print(f"sum={sum(a)}")
'''

'''
a = eval(input())
print(f"length={len(a)}")
print(f"sum={sum(a)}")
'''

