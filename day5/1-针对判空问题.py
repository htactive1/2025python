# 容器是空的话，就是假但不是false，比如下面if是进不去的
if []:  # 空列表进不去的  所以为去下面else打印
    print("空列表")
else:
    print("非空列表")

if {}:  # 空字典进不去的  所以为去下面else打印
    print("空字典")
else:
    print("非空字典")

if "":  # 空字符串进不去的  所以为去下面else打印
    print("空字符串")
else:
    print("非空字符串")
# 空的容器 和 None 是不同的
