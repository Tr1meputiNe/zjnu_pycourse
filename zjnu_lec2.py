#input()函数
#e.g. 1
a = input("input your name: ")
print(a)
#接收的是字符串类型
age = input("input your age : ")
print(type(age))
print(int(age) + 5)
#数据输入（input，map)
#map()函数
#e.g. 2

'''
b = input("input a number: ")
c = input("input another number: ")
int(b)
int(c)
print(b + c)
'''

b, c = map(int, input("input two numbers: ").split())
print(b + c)


#print()函数 以,将参数进行分割
#e.g. 3
print("hello world", "hello zjnu", 2025, sep = " --- ", end = "\n***\n")
#sep参数指定分隔符，end参数指定结尾符


#格式化输出
#e.g. 4
name, age = map(str, input("input your name and age: ").split())
#占位符方式
print("My name is %s, I am %s years old." % (name, age))
#%s字符串，%d整数，%f浮点数，%x十六进制数
#百分号后加数字表示占位宽度，如%.2f表示保留两位小数，%2d表示至少两位宽度,%-2d表示至少两位宽度，左对齐,不足补空格
pi = 3.141592653589793
print("pi = %.2f" % pi) #保留两位小数
number = 7
print("number = %2d" % number) #至少两位宽度，右对齐
print("number = %-2d" % number) #至少两位宽度，左对齐
#format()函数
age = int(age)  #ag
print("My name is {0:5s}, I am {1:3d} years old. {0} is a student.".format(name, age))
#f字符串
print(f"My name is {name}, I am {age} years old. {name} is a student.")


#list 列表
#e.g. 5
lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))
#访问列表元素
print(lst[0]) #第一个元素
print(lst[-1]) #最后一个元素
#修改列表元素
lst[0] = 10
print(lst)
#添加元素
lst.append(6)
print(lst)
#插入元素
lst.insert(2, 20) #在第三个位置插入20
print(lst)
#删除元素
lst.pop(2) #删除第三个元素
print(lst)
#切片
print(lst[1:4]) #第二个到第四个元素
print(lst[:3]) #前三个元素 
print(lst[2:]) #从第三个元素到最后
print(lst[-1::-1]) #反转列表
#遍历列表
for i in lst:
    print(i)
#列表推导式
squares = [x**2 for x in range(1, 6)]
print(squares)
#列表初始化
zeros = ["",0,""] * 5
print(zeros)
