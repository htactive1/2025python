import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 设置请求头
headers = {
    'referer': 'https://hotel.qunar.com/',
    'cookie': 'QN1=0001070030685f861d78b93e; QN300=s%3Dbing; QN99=5000; QN269=F13A14700C7F11EF90B13AEA6221AE50; _i=ueHd8D8omo-XZzvA-g2AtFlLVzRX; QN601=88dbfa5d2521265a3a286f31a277d63b; QN48=000139002f105f861d80042b; quinn=990020fd61f9f6da08a25bbec64a083059e615cd04301082bd7081de15ff39a956880e71c686650ab9332807582ffdb6; fid=f518f68e-8878-462c-be3b-d2d8fae40596; HN1=v1afaa012078ea600a06d2b6b055980b0b; HN2=qkzrucugkcqkq; SECKEY_ABVK=/QANlHkj5D8bn5DluZ0+mellcwI4IW8AU/50Jw8uECk%3D; BMAP_SECKEY=b1PemlbCTlaUnbOyWZWfXp_hvEZm3LYop6JoXuTAPGBzd-yqQ2FCvjmzucaqRk2NnyVdksiiNqtj5o9WpgFxHEdaVxchu8XQVSWVK5A55sNEps1yMe-3l1jK6deChqA707sY6qhXMvT6uwaLFTFBQLiXY1kXSOGSaA0phkfVd7M715txCgMxln7aNRs00KF2; ctt_june=1683616182042##iK3wVRDOahPwawPwasDsasvOWSamE2jOWPkTWSvsaSjmaKg%2BE2POa2D%2BWsPNiK3siK3saKgnWKvNaS2sWK2NWhPwaUvt; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; _q=U.laarcwc4331; _t=28694322; csrfToken=UOeKDwdFvaU8joxno62ZgtmXAfhLz1Gy; _s=s_W5NSNIQRKAG73ZDI2X6ZFNMIAU; _v=7rJkMTy4oHXGVvOtd1Ru9utXl0ujD6tn20O8tZbTLXdhE3XZHgifcGRZbue10G2znuum9qVuVvEdP2DImfaFgWlKs3d9BBj64WaD73lqBjzwBBMovUlW225BigZ8WQySbT5_5-gItudnM507wcXzyexEn9EHmynREqlj1125By-g; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN44=laarcwc4331; QN205=s%3Dbing; QN277=s%3Dbing; _vi=FDCW5CyIWjXiRvIB3arE710XwTd-Cd9v8br9ZltBjTicrDLelUFdlcoykxDmAlU3EgDQyJt0cxvBYo7tckTEaVu1NMLV-8XL8Tl1dKyREicP0dSai9RxeIkeVPB97HN-RHvVAtw5TlclsyGPRvlJxQ6MUkj-L1MRUu0jPNMCHTST; RT=s=1716545450740&r=https%3A%2F%2Fflight.qunar.com%2F; tabIndex=0; cityUrl=anji; cityName=%25E5%25AE%2589%25E5%2590%2589%25E5%258E%25BF; checkInDate=2024-05-24; checkOutDate=2024-05-25; ariaDefaultTheme=null; QN271=31c9da70-8797-4a4c-8e64-7076bef1a23b; QN267=01907736813c269d7b8; ctf_june=1683616182042##iK3wVKvNWuPwawPwasj%2BX%3DawVRGRESfhasfhEDX%3DaRHIWstsaSaOEPPOa%3DkIiK3siK3saKgnWSP%3DWKPmWK2%3DauPwaUvt; cs_june=bf8999a10943685b35546b104009d22908662388ed71d0fa6a13f6439a38017c4eddeb0637d430734c1093bf6b057f5836ab571bbd5f36654d10ede0101b1d5db17c80df7eee7c02a9c1a6a5b97c1179f3b866399541ff3fb1e0c2086e6802ad5a737ae180251ef5be23400b098dd8ca; __qt=v1%7CVTJGc2RHVmtYMSsyTE9WODFCeHRid0VQUHhlMXNKZElNb2RCYU8yNUsyZjRYd01HNWxXTSs1MDNCYmtVcXdUcmUxeXJrYVJNWjFiVmw2ckZLMUovU3k2UFBkUmpBS0gwVkVpN0xna0ZLYk1aSHBXdHFuSTNKellvTDdCMFZoUXJzQ244QWRGTTErL0Z5TnpKT1dYK0hjdzEzZERoMExmcFBaK3ZMT3YvV3JBPQ%3D%3D%7C1716545592657%7CVTJGc2RHVmtYMS9GWUNtQXN1Y3lkcmtkNi8xbHFCd0FsK3JzTHdTMXNYQzV5YWVpWDQ1bE5UYnBnWnFOeXprc2xTQTZzelh3d3dDbGduSTVzY3FIbHc9PQ%3D%3D%7CVTJGc2RHVmtYMTlpejV6cHVCd2hhK3hsVk0zMmdadVdZcy9Ua3B5VXhNQTNteHI1TjdneWxRaEZGUkxKVWUybVpuVUlKUGFKOWszQWFkUVB6cU9EZlRYVis0UkJVcWpVL1U3NVZ1RWpsRDlqRkJhN09CQmgrRDdHY1I5Q2F2aTd5YjNNTEVDYVZtbWZrTERYVk9PZjgzTFZ1Y05MV0w1b2JKT24wYTg0Yy9CTHhqR3hwV2lTY1A1a3NCTCszY0VxbGVmYTkvRVd3TllIK1dSanVudXRJQlVRVThjZHNjWndRdUlvNG9aa1ladmpsNFZPMUJaM1VuVndpQXpQV3pCc252TlA5bkUwU0lwWXZma3Z0MVZOeHVOVDBSNGR4WXJKU3VDZjJPQU5QeTNvTm5kaGF5RFJwbXQraGh4TDlINTkxbmJjVzIxbStvWXIxcUIvMFdUTVdOcVF3ZWdRVWdGbzZ2dGxyR3hwK0VoNFZaUWpMV3VJcndVUFdaTFpMUkNZdk4zODM5YjhxLzkrN1JUZ3dlRkMwM2hNQjdLcDFPWC84cThIK1FoK3E3cUpLcWJKQU1lN0ZFcXVCY3Q3TVYxb3ZSWXduMTRZR05pNlZWZmpVeHdWNnZlVCtCWG1wQzE1Kzk4OU1GRG10MDNYWk9yWkF4S3NyZmNlZWlORklPb1ZhRnhxbW1GSENBVnFHWHB5b216b3ZEYjRsQWNOcC9Cdi9iMVV1NGgyOEw2bisrY1RJdXhwb1B0VWU5Q0dJK3ZoOUlXV2NDbjlST3BDbHJyQVFIVElBOW12M01wVkRwenRhK0tuVW5xek9ZWXp6SHhrWm5qMThqL0ZSU3BoSStsZ3hYak4rRzhBTUVWZXdsVEJmRDU0TWJtSE5tL29OMC9abE1rQ0YwalBHWWc9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

def extract_hotel_info(soup):
    # 创建空列表用于存储提取的数据
    data = []

    # 找到所有酒店的容器
    hotel_containers = soup.find_all('div', class_='inner clearfix')

    for container in hotel_containers:
        # 提取酒店名称
        name = container.find('h2', class_='hoterl-name')
        name = name.text.strip() if name else "未知"

        # 提取酒店地址
        address = container.find('p', class_='address')
        address = address.text.strip() if address else "未知"

        # 提取价格
        price = container.find('a', class_='price-new')
        price = price.text.strip() if price else "未知"

        # 将提取的数据添加到列表中
        data.append([name, address, price])

    return data

def save_to_excel(data, filename):
    wb = Workbook()
    ws = wb.active

    # 写入表头
    ws.append(['酒店名称', '酒店地址', '价格'])

    # 写入数据
    for row in data:
        ws.append(row)

    # 保存Excel文件
    wb.save(filename)

def scrape_qunar_hotels(scenic_spot, headers, num_pages):
    all_data = []

    for page in range(1, num_pages + 1):
        url = f'http://hotel.qunar.com/city/beijing_city/dt-1/?fromDate=2024-05-20&toDate=2024-05-21&from=qunarHotel&showMap=0&cityurl=beijing_city&cityName=北京&page={page}&q={scenic_spot}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = extract_hotel_info(soup)
        all_data.extend(data)

        # 模拟点击下一页按钮，如果没有下一页则跳出循环
        next_page = soup.find('a', class_='next')
        if not next_page:
            print("已经到达最后一页。")
            break

    # 调用保存到Excel文件的函数
    filename = f'{scenic_spot}_hotels.xlsx'
    save_to_excel(all_data, filename)

if __name__ == "__main__":
    scenic_spot = '中南百草原'  # 你可以替换成你想搜索的景点
    scrape_qunar_hotels(scenic_spot, headers, num_pages=100)
