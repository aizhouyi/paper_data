from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"


# def bar_base() -> Bar:
#     c = (
#         Bar()
#         .add_xaxis(["sondid", "userid", "comment", "content"])
#         .add_yaxis("爬取结果", [300, 132435, 132435, 132435])
#         .add_yaxis("清洗之后", [257, 60892, 71065, 66937])
#         .set_global_opts(title_opts=opts.TitleOpts(title="清洗前后对比", subtitle=""))
#     )
#     return c


# bar_base().render("temp.html")
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["sondid", "userid", "comment", "content"])
        .add_yaxis("爬取结果", [300, 132435, 132435, 132435])
        .add_yaxis("清洗之后", [257, 60892, 71065, 66937])
        .set_global_opts(title_opts=opts.TitleOpts(title="清洗前后对比", subtitle=""))
    )
    return c


bar_base().render("temp.html")