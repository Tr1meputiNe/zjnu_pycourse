#sort()函数 对列表进行排序，默认升序排列
lst = [3, 1, 4, 2, 5]
lst.sort()
print(lst)
#reverse参数 设置为True时，降序排列
lst.sort(reverse = True) 
print(lst)
#sort()函数 也可以接收一个key参数，指定根据哪个元素进行排序
lst = [('apple', 3), ('banana', 1), ('orange', 4), ('grape', 2), ('pear', 5)]
lst.sort(key = lambda x: x[1]) #根据元组的第二个元素排序
print(lst)
#sorted()函数 返回一个新的排序后的列表，原列表不变（异地排序
lst = [3, 1, 4, 2, 5]
new_lst = sorted(lst)
print(new_lst)
new_lst = sorted(lst, reverse = True) #降序排列
print(new_lst)
new_lst = sorted(lst, key = lambda x: x % 2) #根据元素的奇偶性进行排序
print(new_lst)
#revered()函数 返回一个新的列表，元素顺序颠倒
lst = [3, 1, 4, 2, 5]
new_lst = list(reversed(lst))
print(new_lst)
#reversed()方法 用于字符串或列表，返回一个反转的字符串
s = "hello world"
new_s = (reversed(s))
print(new_s)
#if_else_elif条件表达式
#略
#eval()函数 将字符串str当成有效的表达式来求值并返回计算结果
print(eval("max(1,2,3,4,5)"))#输出5
print(eval("2 + 3 * 4"))#输出14

