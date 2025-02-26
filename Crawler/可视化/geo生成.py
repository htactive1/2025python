from pyecharts import options as opts
from pyecharts.charts import Geo
import json

# 读取地图数据
with open('安吉县.json', 'r', encoding='utf-8') as f:
    j = json.load(f)

# 提取地名及对应的数据
data = [(feature['properties']['name'], 1) for feature in j['features']]

# 创建地理坐标系实例
c = (
    Geo()
    .add_schema(
        maptype="china",
        center=[119.666084, 30.638675],  # 安吉县的经纬度
        zoom=12,
    )
    .add(
        "安吉",
        data,
       # type_=opts.ChartType.EFFECT_SCATTER,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="安吉县地图"),
        visualmap_opts=opts.VisualMapOpts(max_=10)
    )
    .render("geo生成.html")
)
