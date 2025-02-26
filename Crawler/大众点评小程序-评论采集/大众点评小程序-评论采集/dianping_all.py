##导入相关包
import json
import os
import random
import time
import pandas
import requests

history_page = []
def reload_crawl_done_page():
    if not os.path.exists("./config/done.txt"):
        return
    with open("./config/done.txt", 'r', encoding='utf-8') as f:
        done_pages = [i.strip() for i in f.readlines()]
    for done in done_pages:
        history_page.append(done)


##调用函数获取评论数据
def start_search(shop_id,shop_name, max_page, user_login_token):
    for page in range(0, int(max_page)):

        current_page = f'{shop_id}-{page}'
        if current_page in history_page:
            print(f">>> 当前页面已经被采集过：{current_page}")
            continue

        ##评论接口
        api = 'https://m.dianping.com/ugc/review/reviewlist'

        ##请求参数：cx  _token  mtsireferer 不做校验，可以保留固定值
        params = {
            "yodaReady": "wx",
            "csecplatform": "3",
            "csecversion": "1.4.0",
            "optimus_platform": "13",
            "optimus_partner": "203",
            "optimus_risk_level": "71",
            "optimus_code": "10",
            "tagType": "1",
            "tag": "全部",
            "offset": str(page * 10),
            "shopUuid": shop_id,
        }

        ##发送请求
        while 1:
            try:
                headers = {
                    'Host': 'm.dianping.com',
                    'Connection': 'keep-alive',
                    'mtgsig': '{"a1":"1.2","a2":,"a3":"","a4":"","a5":"","a7":"","x0":3,"d1":""}',
                    'channel': 'weixin',
                    'channelversion': '3.9.8',
                    'minaversion': '9.48.1',
                    'wechatversion': '3.9.8',
                    'sdkversion': '3.2.5',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/8501',
                    'Content-Type': 'application/json',
                    'token': user_login_token,
                    'minaname': 'dianping-wxapp',
                    'Accept': '*/*',
                    'Accept-Language': '*',
                    'Referer': 'https://servicewechat.com/wx734c1ad7b3562129/448/page-frame.html',
                }
                proxy_host = 'http-dynamic.xiaoxiangdaili.com'
                proxy_port = 10030
                proxy_username = '916959556566142976'
                proxy_pwd = 'qHDFwFYk'

                proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                    "host": proxy_host,
                    "port": proxy_port,
                    "user": proxy_username,
                    "pass": proxy_pwd,
                }
                proxies = {
                    'http': proxyMeta,
                    'https': proxyMeta,
                }
                res = requests.get(api, headers=headers, params=params, timeout=(10, 10))
                print(res.status_code)
                time.sleep(random.uniform(.2, .4))
                break
            except Exception as e:
                print(f"账号异常:{e}")
                time.sleep(10)
                return
        ##获取评论列表
        shopReviewInfo = res.json()['reviewInfo']['reviewListInfo']["reviewList"]
        for isr in shopReviewInfo:
            comtents = []
            ##解析出评论文本
            if type(isr.get("reviewBody")) == str:
                continue
            else:
                reviewBody = isr.get("reviewBody").get("children")
                for irev in reviewBody:

                    try:
                        if irev.get("children") is not None:
                            for ichildren in irev.get("children"):
                                if ichildren.get("type") == 'text':
                                    comtents.append(ichildren.get("text"))
                        else:
                            if irev.get("type") == 'text':
                                comtents.append(irev.get("text"))
                    except Exception as e:
                        print(f'parse error:{e}')
                        time.sleep(1)
            comtents_ = '\t'.join(comtents)

            saveitem = {}
            saveitem["店铺名"] = shop_name
            saveitem["店铺id"] = shop_id
            saveitem["发布时间"] = isr.get("addTime").split("T")[0]
            saveitem["更新时间"] = isr.get("lastTime")
            saveitem["评论id"] = isr.get("reviewId")
            saveitem["评分"] = isr.get("star") / 10
            saveitem["人均"] = isr.get("avgPrice")
            saveitem["评论"] = comtents_
            saveitem["图片"] = [i.get("bigurl") for i in isr.get("reviewPics")]
            saveitem['用户id'] = isr.get("userId")
            saveitem['用户名'] = isr.get("userNickName")
            saveitem["点赞数"] = isr.get("flowerTotal")
            saveitem["评论数"] = isr.get("followNoteNo")
            print(shop_id, f'[{page}/{int(max_page)}]', saveitem)

            with open(f"./config/{shop_id}_data.txt", 'a', encoding='utf-8') as f:
                    f.write(json.dumps(saveitem))
                    f.write('\n')


        with open("./config/done.txt", 'a', encoding='utf-8') as f:
            f.write(current_page)
            f.write('\n')

        if len(shopReviewInfo) < 5:
            break


if __name__ == "__main__":

    reload_crawl_done_page()
    for shopname,shopid in [
        (""
         "凤凰山森林公园",'Fm7xlBaSbz8UfJQY'),

    ]:
        start_search(
            shop_id=shopid,
            shop_name=shopname,
            max_page=200,
            user_login_token='0202a01fe0a87c5cca234aff322abbca8b247160fa8f761afcb79887fa432905175b6001f3a7b31f0ed6d965925f5c31957a81d29a4b9f7c0c5f00000000a61f000067de5c697486aea8130dbe27338fc07f595606a9ca7030d3900dd31aef2115b85fbd800383c37781bd07d541981b8847'
        )

    all_records = []
    for txt in os.listdir("./config"):
        if 'Fm7xlBaSbz8UfJQY_data.txt' in txt:
            with open(f"./config/{txt}",'r',encoding='utf-8') as f:
                rlines = [json.loads(i.strip()) for i in f.readlines()]
            all_records+=rlines
    pandas.DataFrame(all_records).to_excel("凤凰山森林公园.xlsx",index=False)