#函数
#内置函数
import math
math.isqrt(100) #返回整数平方根

def isprime(n):
    for i in range (2, math.sqrt(n) + 1):
        if n % i == 0:
            return False
        else:
            return True
n = int(input("Enter a number: "))
if isprime(n):
    print(n)
else:
    print(n, "is not a prime number")
#参数传递
#必须参数（如上

#关键字参数
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
#调用printme函数
printme( str = "111")
#默认参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )

#不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
# 调用printinfo 函数
printinfo( 70, 60, 50 )
#*后会以元组类型导入
#！！如果单独出现星号* 后的参数只能用强制关键字
#**则以字典
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
# 调用printinfo 函数
printinfo(1, a=2,b=3)

#匿名函数lambda
x = lambda a : a + 10
print(x(5))

sum = lambda arg1, arg2: arg1 + arg2

print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))
#可以将lambda封装在函数内
def myfunc(n):
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))

#return语句
#调用函数后会返回值，可返回多个（以元组形式返回
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
# 调用sum函数
t = sum( 10, 20 )
print ("函数外 : ", t)

#强制位置参数
#在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

#内置函数介绍
#fliter()
#输出true的元素
def isodd(n):
   return n % 2 == 1
n = list(filter(isodd, range(1, 20)))
print(n)

#zip
#打包，将元素一一匹配构造元组
a = [1, 2, 3]
b = [4, 5, 6]
t = zip(a, b)
print(list(zip(a, b)))
#若非等长，舍去超出部分
#zip(*)解包
a1, b1 = zip(*t)
print(a1, b1)

#enumerate()
#遍历并给每个元素加序号

