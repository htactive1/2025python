from pyecharts.charts import BMap
from pyecharts import options as opts
import json

# 读取自定义地图样式 JSON 文件
with open('custom_map_config.json', 'r', encoding='utf-8') as f:
    custom_style_json = json.load(f)

# 设置百度地图 JavaScript API 的密钥
baidu_ak = "Your_Baidu_Map_API_Key"

# 创建地图实例
c = (
    BMap(init_opts=opts.InitOpts(width="800px", height="600px"))
    .add_schema(
        baidu_ak="iT7rMtmeMX7xYf0f5JAWVfOH6vopt3w3",   # 你需要替换为你自己的百度地图API密钥
        center=[119.666084, 30.638675],  # 安吉县的经纬度
        zoom=12,
        map_style=custom_style_json,  # 应用自定义地图样式
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="安吉县地图"))
)

# 生成 HTML 文件
c.render("custom_baidu_map.html")
