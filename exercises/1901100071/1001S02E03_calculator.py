# 计算器确定三个输入值，分别是运算符、运算符左边的数字和右边的数字

# 把内置函数 input 接收的输入字符 赋值 给 变量
operator = input("请输入运算符(+、-、*、/): ") # input 里面的字符串的作用是在等待输入的时候进行提示
first_number = input("请输入第一个数字：")
second_number = input("请输入第二个数字：")

a = int(first_number) # first_number在这里的作用是 把 str 类型 的 first_number转换成 int类型
b = int(second_number)

print("operator:",operator,type(operator))
print("first_number:",first_number,type(first_number),type(a))
print("second_number:",second_number,type(second_number),type(b))

print("测试加法 str 加法：",first_number + second_number )

if operator == "+":
    print(a, "+", b, "=", a+b)
elif operator == "-":
    print(a, "-", b, "=", a-b)
elif operator == "*":
    print(a, "*", b, "=", a*b)
elif operator == "/":
    print(a, "/", b, "=", a/b)
else:
    print("无效的运算符")
    # raise ValueError"无效的运算符"