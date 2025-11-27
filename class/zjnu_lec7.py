#列表推导式
#l = [表达式 for 变量 in 可迭代对象 if 条件表达式] #生成列表
l =[1 / n if n > 0 else 0 for n in range(1, 11)]#生成1到10的倒数列表
print(l)
#异常处理
#预计到的错误用代码解决
#不可预计的错误用异常处理
try:
    num = int(input("请输入一个整数："))
    result = 10 / num
except ValueError:
    print("输入的不是整数！")
except ZeroDivisionError:
    print("除数不能为零！")
except Exception as e:
    print("发生了其他错误：", e)
else:
    print(result)
finally:
    print("程序结束。")
#
