#Q1
'''
a = input()
b = input()
c = input()

print(a, b, c)
print(a, b, c, sep = "-")
'''

#Q2
'''
a = input()
b = input()
c = input()
d = input()

print("今天是{}年{}月{}日，天气{}。".format(a, b, c, d))
'''

#Q3
'''
a = input()
b = input()
c = input()
d = input()
print(f"今天是{a}年{b}月{c}日，天气{d}。")
'''

#Q4
'''
n = int(input())
X = n * 50
Y = n * 2
Z = n * 100

print(f" 为了准备{n}人份的面条，你需要{X:.1f}毫升水，{Y:.1f}克盐，{Z:.1f}克面粉。")
'''

#Q5
'''
f = float(input())
c = 5 * (f - 32) / 9

print(f"{c:.2f}")
'''

#Q6
'''
a = int(input())
b = int(input())
c = int(input())
s = a + b + c
avg = s / 3

print("和:",s)
print("平均:",f"{avg:.4f}")
'''

#Q7
'''
print("轻轻松松通过考试！")
'''

#Q8
'''
s = input()
A = s[::2]
B = s[1::2]
print(A + B)
'''

#Q9
'''
length, width = map(float, input().split(","))
c = ((length ** 2) + (width ** 2)) ** 0.5 
print(f"{c:.3f}")
'''

#Q10
'''
lst = list(input())
while len(lst) < 3 or len(lst) % 2 == 0:
    lst = list(input())

first = lst[0]
mid = len(lst) // 2
middle = lst[mid]
last = lst[-1]
print(f"{first}{middle}{last}")

'''

#Q11
'''
a = input()
b = a.split()
c = input()
d = input()
for i in range(len(b)):
    if b[i].lower() == c.lower():
        b[i] = d
print(" ".join(b))
'''

#Q12
'''
a = input()
b = a[:6]
c = a[14:16]

print(f"当天出生于{b}地区的第{c}个人")
'''

#Q13
'''
a = input()
b = list(a)

while b[0] == "0":
    b.pop(0)

c = input()
n = 0

for i in range(len(b)):
    if b[i].lower() == c.lower():
        n += 1

print(n)

'''

#Q14
'''a = input()
b = a.split()
m = b[0]
for i in b:
    if i > m:
        m = i

print(m)
'''

#Q15
'''
a = input()

print(a[0], end="")
for i in range(len(a) - 3):
    print(a[1], end="")
print(a[0])

print(a[2], end="")
print(a[3:], end="")
print(a[2])

print(a[0], end="")
for i in range(len(a) - 3):
    print(a[1], end="")
print(a[0])


'''
