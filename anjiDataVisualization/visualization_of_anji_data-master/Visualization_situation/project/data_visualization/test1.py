from sklearn.linear_model import LinearRegression
import pandas as pd

# 假设这是你的数据
data = pd.DataFrame({
    'visitor_num': [1000, 2000, 3000, 4000, 5000],
    'ticket_price': [50, 45, 40, 35, 30],
    'hotel_num': [10, 20, 30, 40, 50],
    'hotel_price': [100, 90, 80, 70, 60],
    'rating': [4.5, 4.6, 4.7, 4.8, 4.9],
    'tourism_value': [200, 400, 600, 800, 1000]  # 这是你已知的景点旅游价值，用于训练模型
})

# 准备训练数据
X = data[['visitor_num', 'ticket_price', 'hotel_num', 'hotel_price', 'rating']]
y = data['tourism_value']

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 使用模型进行预测
# 假设这是你要预测的新数据
new_data = pd.DataFrame({
    'visitor_num': [6000],
    'ticket_price': [25],
    'hotel_num': [60],
    'hotel_price': [50],
    'rating': [5.0]
})

# 预测新数据的旅游价值
predicted_value = model.predict(new_data)

print("Predicted tourism value:", predicted_value)
