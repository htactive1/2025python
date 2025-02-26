import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType
import json

data = pd.read_excel('热力图模拟数据.xlsx')

hotmap = (
    BMap(is_ignore_nonexistent_coord=True,  # 忽略不存在的坐标
         init_opts=opts.InitOpts())
    .add_schema(baidu_ak="iT7rMtmeMX7xYf0f5JAWVfOH6vopt3w3", center=[119.752354,30.42031],
                zoom=11.8,  # 当前视角的缩放比例
                is_roam=True  # 是否开启鼠标缩放和平移漫游
                )
    .add(
        "热度",  # 图例
        data_pair=[list(z) for z in zip(data['城市'].to_list(), data['热度'].to_list())],
        type_="heatmap",
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="十一期间全国旅游景点热度",
                                  pos_left='center',
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=32)
                                  ),
        legend_opts=opts.LegendOpts(pos_right='20%'),
        visualmap_opts=opts.VisualMapOpts()
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
    .render("基于pyecharts内置经纬度的热力图.html")
)

# hotmap.render_notebook()