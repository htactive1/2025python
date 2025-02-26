import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType
import json

data = pd.read_excel('游客人次热力图数据.xlsx')


data_json = {}
for index, row in data.iterrows():
    data_json[row['地名']] = [float(row['经度']), float(row['纬度'])]

with open("BMAP.json", "w") as f:
    json.dump(data_json, f)

hotmap = (
    BMap(is_ignore_nonexistent_coord=True,  # 忽略不存在的坐标
         init_opts=opts.InitOpts(width="1058px", height="600px"))
    .add_schema(baidu_ak="iT7rMtmeMX7xYf0f5JAWVfOH6vopt3w3", center=[119.752354,30.42031],
                zoom=11.8,  # 当前视角的缩放比例
                is_roam=True  # 是否开启鼠标缩放和平移漫游
                )
    .add_coordinate_json("BMAP.json")  # 加载自定义坐标
    .add(
        "人气热度",  # 图例
        data_pair=[list(z) for z in zip(data['地名'].to_list(), data['人气热度'].to_list())],
        type_="heatmap",
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .add(
        "酒店热度",  # 图例
        data_pair=[list(z) for z in zip(data['地名'].to_list(), data['酒店热度'].to_list())],
        type_="heatmap",
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="安吉县景点旅游人次热力图",
                                  pos_left='center',
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=32)
                                  ),
        legend_opts=opts.LegendOpts(pos_right='20%'),
        visualmap_opts=opts.VisualMapOpts(max_=100,range_color=['#4393c3', '#92c5de',  '#fd9001', '#d6604d', '#b2182b', '#67001f'])  # 设置最大值，目的是为了能够精确查看自定坐标位置
    )
    .add_control_panel(
        copyright_control_opts=opts.BMapCopyrightTypeOpts(position=3),
        maptype_control_opts=opts.BMapTypeControlOpts(
            type_=BMapType.MAPTYPE_CONTROL_DROPDOWN
        ),
        scale_control_opts=opts.BMapScaleControlOpts(),
        overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
        navigation_control_opts=opts.BMapNavigationControlOpts(),
        geo_location_control_opts=opts.BMapGeoLocationControlOpts(),
    )
    .render("visits_num.html")
)
