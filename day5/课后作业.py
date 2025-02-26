#求两个有序数字列表的公共元素
def common_elements(list1, list2):
    common_elements_list = []
    for element in list1:
        if element in list2:
            common_elements_list.append(element)
    print(common_elements_list)



# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
  common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
