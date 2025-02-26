from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.commons.utils import JsCode
from pyecharts.render import make_snapshot


# 创建 JavaScript 代码，调用百度地图的 setMapStyleV2 方法
js_code = (
    JsCode("map.setMapStyleV2({styleId:'7ec12f72fdb97cfd7f114773e164182e'})")
)

# 创建百度地图实例
c = (
    BMap()
    .add_schema(
        baidu_ak="iT7rMtmeMX7xYf0f5JAWVfOH6vopt3w3",  # 替换为你的百度地图 API 密钥
        center=[119.666084, 30.638675],  # 安吉县的经纬度
        zoom=12,
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="安吉县地图"),
        visualmap_opts=opts.VisualMapOpts(max_=10)
    )
)

# 将 JavaScript 模板应用到地图实例中
c.add_js_funcs(js_code)

# 渲染地图，并生成 HTML 文件
c.render("folium.html")

# 如果需要生成静态图片，可以使用以下代码
# make_snapshot(snapshot, c.render(), "bmap_with_custom_style.png")
