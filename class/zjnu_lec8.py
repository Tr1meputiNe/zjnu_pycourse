#矩阵
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
#对称差集
s6 = s ^ s2
print(s6)
#集合间关系
#>= #超集
#<= #子集
#== #相等
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

#遍历字典
for key in d:
    print(key, d[key])
for i in d.values:
    print(i)
for i in d.items:
    print(i)
#解包
for key, value in d.items():
    print(key, value)

#字典推导式
d = {x: x ** 2 for x in range(1, 6)}
print(d)    
#生成器表达式
g = (x ** 2 for x in range(1, 6))
for val in g:    
    print(val)