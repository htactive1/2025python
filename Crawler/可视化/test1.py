from pyecharts import options as opts
from pyecharts.charts import BMap
import json

# 读取地图数据
with open('安吉县.json', 'r', encoding='utf-8') as f:
    j = json.load(f)

# 提取地名及对应的数据
data = [(feature['properties']['name'], 1) for feature in j['features']]

# 创建百度地图实例
c = (
    BMap()
    .add_schema(
        baidu_ak="iT7rMtmeMX7xYf0f5JAWVfOH6vopt3w3",  # 替换为你的个性化地图API密钥
        map_style="whitegrid",
        center=[119.666084, 30.638675],  # 安吉县的经纬度
        zoom=12,
    )
    .add(
        "安吉",
         data,  # 添加地名及对应的数据
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="安吉县地图"),
        visualmap_opts=opts.VisualMapOpts(max_=10)
    )
    .render("test1.html")
)

