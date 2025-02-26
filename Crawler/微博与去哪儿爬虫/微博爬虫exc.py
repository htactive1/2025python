import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

headers = {
    'cookie': 'SINAGLOBAL=7915990098787.061.1709792434709; UOR=www.baidu.com,weibo.com,login.sina.com.cn; SUB=_2A25LG9RADeRhGeFM6FYQ9y7JyDyIHXVoWWmIrDV8PUNbmtB-LRTjkW9NQML6OCMdW7QIVpQumjpI10Mk9Zn-qyQp; ALF=02_1715941648; PC_TOKEN=1c870f4ce2; _s_tentry=weibo.com; Apache=281351348221.448.1713683136136; ULV=1713683136178:5:4:1:281351348221.448.1713683136136:1713589950343',
    'referer': 'https://s.weibo.com/weibo?q=%E5%AE%89%E5%90%89%E7%AB%B9%E5%8D%9A%E5%9B%AD',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}


def extract_weibo_content(soup):
    # 创建空列表用于存储提取的数据
    data = []

    # 找到所有微博的容器
    weibo_containers = soup.find_all('div', class_='content')

    for container in weibo_containers:
        # 提取用户昵称
        username = container.find('a', class_='name')
        username = username.text.strip() if username else "未知"

        # 提取发布时间
        time_container = container.find('div', class_='from')
        publish_time = time_container.find('a').get_text(strip=True) if time_container else "未知"

        # 提取文本内容
        text = container.find('p', class_='txt')
        text = text.text.strip() if text else "未知"

        # 将提取的数据添加到列表中
        data.append([username, publish_time, text])

    return data


def save_to_excel(data, filename):
    wb = Workbook()
    ws = wb.active

    # 写入表头
    ws.append(['用户名', '发布时间', '文本内容'])

    # 写入数据
    for row in data:
        ws.append(row)

    # 保存Excel文件
    wb.save(filename)


def scrape_weibo_pages(url, headers, num_pages):
    all_data = []

    for page in range(num_pages):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = extract_weibo_content(soup)
        all_data.extend(data)

        # 模拟点击下一页按钮
        next_page_link = soup.find('a', class_='next').get('href')
        if next_page_link:
            url = 'https://s.weibo.com' + next_page_link
        else:
            print("已经到达最后一页。")
            break

    # 调用保存到Excel文件的函数
    filename = '中南百草原data.xlsx'
    save_to_excel(all_data, filename)


if __name__ == "__main__":
    url = 'https://s.weibo.com/weibo?q=%E5%AE%89%E5%90%89%E7%AB%B9%E5%8D%9A%E5%9B%AD&nodup=1'
    scrape_weibo_pages(url, headers, num_pages=50)
