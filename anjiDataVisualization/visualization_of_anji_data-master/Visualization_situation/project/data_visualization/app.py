import numpy as np
from flask import Flask, render_template
import csv
import codecs
import pandas as pd
import mysql.connector

web = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'anjidata'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()



#首页
@web.route('/')
def dashboard():
    # 查询数据
    query = "SELECT place, time, visit_num, hotel_num, average_score, ticket, all_average_price, three_mile_num, three_mile_num_price FROM total_data"
    cursor.execute(query)
    data = cursor.fetchall()

    # 转换数据为字典列表
    columns = ['place', 'time', 'visit_num', 'hotel_num', 'average_score', 'ticket', 'all_average_price',
               'three_mile_num', 'three_mile_num_price']
    data_dict = [dict(zip(columns, row)) for row in data]


    return render_template('bashboard.html', data_dict=data_dict)

@web.route('/index')
def index():
    # 查询数据
    query = """
        SELECT place, average_score, visit_num, three_mile_num, three_mile_num_price, ticket
        FROM total_data
    """
    cursor.execute(query)
    data = cursor.fetchall()

    # 提取各列数据
    places = [row[0] for row in data]
    R = np.array([row[1] for row in data])
    N = np.array([row[2] for row in data])
    Hq = np.array([row[3] for row in data])
    Hp = np.array([row[4] for row in data])
    T = np.array([row[5] for row in data])

    # 处理零值，避免除以零的情况


    # 计算max和min值，避免除以零的情况
    max_N = np.max(N) if np.max(N) != 0 else 1
    max_Hq = np.max(Hq) if np.max(Hq) != 0 else 1
    min_Hp = np.min(Hp) if np.min(Hp) != 0 else 1


    #  门票0得满分，其余30/当地价格 算得分
    T_scores = np.where(T == 0, 1.0, 30 / T)

    # 设置权重因子
    alpha = 30
    beta = 50
    gamma = 10
    delta = 15
    epsilon = 10

    # 计算评分
    S = alpha * R / 5 + beta * (N/max_N) + gamma * (Hq/ max_Hq ) + delta * (min_Hp/ Hp) + epsilon *T_scores;

    # 打印结果
    for place, score in zip(places, S):
        print(f"{place} 的评分为: {score:.2f}")


    return render_template('index.html')


@web.route('/movie')
def movie_list():
    movies = [{'file':'安吉宣传片.mp4','title':'安吉宣传片'}]
    return render_template('movie.html',movies=movies)


@web.route('/map')
def map():
    return render_template('map.html')


@web.route('/pie')
def pie():


    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT place, visit_num, hotel_num, time FROM total_data WHERE time = 2023")
    data_2023 = cursor.fetchall()
    conn.close()
    # 生成饼图数据
    people_pie_data_2023 = [{'name': row['place'], 'value': row['visit_num']} for row in data_2023]
    people_pie_data_2023.sort(key=lambda x: x['value'], reverse=True)
    hotel_pie_data_2023 = [{'name': row['place'], 'value': row['hotel_num']} for row in data_2023]
    hotel_pie_data_2023.sort(key=lambda x: x['value'], reverse=True)
    return render_template('pie.html', people_pie_data_2023=people_pie_data_2023,hotel_pie_data_2023=hotel_pie_data_2023 )


@web.route('/rank')
def rank():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT place, average_score FROM total_data")
    data = cursor.fetchall()


    # 根据平均评分对数据进行排序
    sorted_data = sorted(data, key=lambda x: x['average_score'], reverse=True)

    # 获取排序后的景点和平均评分
    place_name = [item['place'] for item in sorted_data]
    average_score = [item['average_score'] for item in sorted_data]

    return render_template('rank.html', place_name=place_name, average_score=average_score)






web.run(debug=True)
