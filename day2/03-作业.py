# 实现1-100的奇数求和
def use_sum():
    total = 0
    for i in range(1, 101, 2):
        total += i
    print(total)
    # 实现1-100的奇数求和
    num = 0
    i = 1
    while i <= 100:
        num += i
        i += 2
    print(num)


# 打印九九乘法表

def print_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{i}*{j}={i * j}", end="\t")
        print()


def use_count1():
    # 统计一个整数的二进制中1的个数
    num = int(input("请输入一个整数："))
    original_num = num
    count = 0
    while num > 0:
        if num % 2 == 1:
            count += 1
        num //= 2
    print(f"整数{original_num}的二进制中1的个数为{count}")


def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def use_zifuchuanhuanhang():
    str1='abc,def,ghij'
    print(str1.split(','))
    str2='abc\ndef\nghij'
    print(str2.split('\n'))
    str_list=['a','b','c']
    str3=(','.join(str_list))
    print(str3)

def use_tuple():
    t = (1, 2, 3)
    print(id(t))
    t = t + (4, 5)
    print(id(t))
    print(t)

def str_slice():
    """
    字符串切片
    :return:
    """
    num_str='1234567890'
    print(num_str)
    print(num_str[0:3])
    print(num_str[3:])
    print(num_str[:3])
    print(num_str[:])
if __name__ == '__main__':
    # use_tuple()
    use_zifuchuanhuanhang()