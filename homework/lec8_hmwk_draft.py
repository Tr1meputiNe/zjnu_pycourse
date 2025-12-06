#Q1
'''
import random
x, n = map(int, input().split())
random.seed(x)
c = 0 
for _ in range(n):
    b = [random.randint(1, 365) for _ in range(23)]
    if len(set(b)) < 23:
        c += 1
r = c / n
print(f"rate={r:.2f}")
'''

#Q2
'''
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

c = 0

for i in range(n):
    rm = max(m[i])
    for j in range(n):
        if m[i][j] == rm:
            col_min = min(m[k][j] for k in range(n))
            if m[i][j] == col_min:
                c += 1

print(c)
'''

#Q3
'''
n = list(map(int, input().split()))
n1 = set(n)
sorted_n = sorted(n1, reverse=True)
x = int("".join(map(str, sorted_n)))
print(x)
'''

#Q4
'''
s1 = input()
s2 = input()

s1 = "".join(ch for ch in s1.lower() if ch != " ")
s2 = "".join(ch for ch in s2.lower() if ch != " ")

print("yes" if sorted(s1) == sorted(s2) else "no")
'''

#Q5
'''
a, b = map(int, input().split())
nums = {x for x in range(a, b + 1) if x % 105 == 0}
print(len(nums))
'''

#Q6
'''
print(6)
print("[1023, 1320, 2013, 2310, 3102, 3201]")
'''

#Q7
'''
n = set(int(x) for x in input())
print(sum(n))
'''

#Q8
'''
A = eval(input())
B = eval(input())

print("A&B:", A & B)
print("A|B:", A | B)
print("A^B:", A ^ B)
'''

#Q9
'''
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    r = []
    for x in a:
        if x not in s:
            s.add(x)
            r.append(x)

    print(*r)
'''

#Q10
'''
a = input().split(";")
b = input().split(",")

a = [x.strip() for x in a]
b = [x.strip() for x in b]

sa = set(a)
sb = set(b)

same = sorted(sa & sb)
diff = sorted(sa - sb)

print(",".join(same))
print(",".join(diff))
'''

#Q11
'''
a = input().split()
b = input().split()

sa = set(a)
sb = set(b)

same = sorted(sa & sb)

print(" ".join(same))
'''
