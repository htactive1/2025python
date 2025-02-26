name = '小明'
student_no = 1
price = float(input("请输入价格"))
weight = float(input('请输入重量'))
money = price * weight
print('我的名字是 %s,请多多关照' % name)
print('我的学号是%06d' % student_no)
print('苹果单价%.02f元/斤，购买了%.02f斤，总共是%.02f元' % (price, weight, money))
