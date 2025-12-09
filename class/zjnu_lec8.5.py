#矩阵
from optparse import Values


n = int(input())
matrix = ([0] * n for _ in range(n))
#集合  无重复元素  无序  不可索引
#创建集合
s = {1, 2, 3, 4, 5}
print(s)
#创建空集合
s = set()
#可自动去重
s = {1, 2, 2, 3, 4, 4, 5}
print(s)
#添加，删除,更新元素
s.add(6)
s.remove(3)
print(s)
s2 = {4, 5, 6, 7, 8}
s.update(s2) #并集
#若不存在，删除报错
s.discard(10) #若不存在，不报错
#交集
s3 = s & s2
print(s3)
#并集   
s4 = s | s2
print(s4)
#差集
s5 = s - s2
print(s5)
#补集（对称差集）
s6 = s ^ s2
print(s6)
#集合间关系
#>= #超集
#<= #子集
#== #相等----键和值都相等
#!= #不等


#字典 无顺序 可变
#创建字典 键可哈希 不重复（int，str，float， tuple（内部也必须是不可变对象））
d = {1: 'a', 2: 'b', 3: 'c'}
print(d)
#哈希#
d[4] = 'd' #添加元素
print(d)
del d[2] #删除元素
print(d)
#字典间关系

#in #键是否存在
print(3 in d)
print(5 not in d)
#len #键值对数量
print(len(d))
#get #获取值
print(d.get(1))
print(d.get(5, 'not found')) #键不存在时返回默认值
#keys() #获取所有键
print(d.keys())
#values() #获取所有值
print(d.values())
#items() #获取所有键值对
print(d.items())
#clear() #清空字典
d.clear()
print(d)
d = {1: 'a', 2: 'b', 3: 'c'}
#update() #合并字典
d2 = {4: 'd', 5: 'e'}
d.update(d2)
print(d)
#copy() #复制字典
d3 = d.copy()
print(d3)
#setdefault() #设置默认值
d.setdefault(6, 'not found')
print(d)

#遍历字典
for key in d:
    print(key, d[key])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(key)

#字典推导式
d = {x: x ** 2 for x in range(1, 6)}
print(d)    
#dict.fromkeys() #创建新字典，指定键和值
keys = ['a', 'b', 'c']
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)
#查找
d = {1: 'a', 2: 'b', 3: 'c'}
d.get(2) #返回'b'
n =int(input())
d.get(n, 'not found') #返回'not found'
#删除
d = {1: 'a', 2: 'b', 3: 'c'}
d.pop(2) #删除键2及其对应的值,并返回该值
print(d)
d.popitem() #删除最后一个键值对
print(d)
#遍历
d = {1: 'a', 2: 'b', 3: 'c'}
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")    
#生成器  节省内存
#生成器表达式
g = (x ** 2 for x in range(1, 6))
for val in g:    
    print(val)
#练习题
#Q1 输入1-7输出对应的星期几，输入其他输出“Invalid day
days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
num = int(input())
print(days.get(num, 'Invalid day'))
#Q2 输入一个字符串，统计每个字符出现的次数
s = input()
char_count = {}
for char in s:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

print(r)
#Q3四则运算
result = {"+": "x + y", "-": "x - y", "*": "x * y", "/": "x / y if y != 0 else 'undefined'"}
x, y = map(int, input().split())
op = input().strip()
r = eval(result.get(op, 'invalid operator'))
print(r)
#Q4输入一串字符，求“a""b""c”在该串中出现的次数
s = input()
diccount = {chr(ord("a") + i):0 for i in range(26)}
lst = [char for char in s if char in "abc"]
for char in lst:
    diccount[char] += 1
print(diccount)
#Q5 字典二维表格
#Q6 图和字典
d = {"s": {1: 1, 2: 2, 3: 4}, 1: {3: 5}, 2: {"t": 8, 3: 78}, 3: {2: 4, "t": 8},"t":{}}
v = set()
e = set()
s = 0
#顶点，边的集合
for key, value in d.items():
    v.add(key)
    if type(value) == dict:
        for k1, v1 in value.items():
            v.add(k1)
            e.add((key, k1))
            s += v1
print(len(v), v)
print(len(e), e)
print(s)

