from pyecharts import options as opts
from pyecharts.charts import BMap

# 定义地图数据
data = [
    ("上海", 100),
    ("北京", 90),
    ("广州", 80),
    ("深圳", 70),
    ("杭州", 60),
    ("成都", 50),
    ("南京", 40),
    ("武汉", 30),
    ("重庆", 20),
    ("西安", 10),
]

# 初始化地图
c = (
    BMap()
    .add_schema(baidu_ak="您的百度地图开发者AK")
    .add(
        "热力图",
        data,
        type_="heatmap",
        label_opts=opts.LabelOpts(formatter="{b}", position="inside"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="百度地图热力图"),
        visualmap_opts=opts.VisualMapOpts(max_=100),
    )
)

# 生成 HTML 文件（或者调用 render_notebook() 在 Jupyter Notebook 中显示）
c.render("bmap_heatmap.html")
