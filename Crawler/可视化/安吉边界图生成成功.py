from pyecharts import options as opts
import json
from pyecharts.charts import Map

with open('安吉县_FeaturesToJSON.json', 'r', encoding='utf-8') as f:
    j = json.load(f)

    # 提取地名及对应的数据
    data = [(feature['properties']['name'], 1) for feature in j['features']]

c = (
    Map()
    .add_js_funcs("echarts.registerMap('安吉', {});".format(j))  # 注册地图
    .add("安吉",
               data, "安吉")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="安吉县地图"), visualmap_opts=opts.VisualMapOpts(max_=10)
    )
    .render("安吉.html")
)
# c.render_notebook()





