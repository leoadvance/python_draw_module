# coding=utf-8

from typing import List

import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.offline as py_offline

PLOTLY_LAYOUT_TEMPLATE = "plotly_white"
IMAGE_OUTPUT_DIR = "../.outImage/"
MAX_SUBPLOT_ROW = 4  # 单屏幕显示最大列数


class PlotlyDraw:
    @classmethod
    def golden_cross_collect(
        cls, df_revenues: pd.DataFrame, screen_hight: int, screen_width: int
    ):
        """
        绘制总营收图
        :param df_revenues: 待处理DataFrame
        """
        # 建立子图
        subplot_titles = ("营收率汇总",)

        # 设置每幅图占据的空间 row and column 两层[[]]表示纬度
        subplot_specs = [[{"rowspan": 1, "colspan": 1}], [None], [None], [None]]
        fig = plotly.subplots.make_subplots(
            rows=MAX_SUBPLOT_ROW,
            cols=1,
            subplot_titles=subplot_titles,
            specs=subplot_specs,
        )

        trace_min_revenue_rate = go.Scatter(
            x=df_revenues["stockName"],
            y=df_revenues["minRevenueRate"],
            mode="markers+lines",  # 点线图
            name="最大亏损率",
        )
        trace_max_revenue_rate = go.Scatter(
            x=df_revenues["stockName"],
            y=df_revenues["maxRevenueRate"],
            mode="markers+lines",  # 点线图
            name="最大营收率",
        )
        trace_current_revenue_rate = go.Scatter(
            x=df_revenues["stockName"],
            y=df_revenues["currentRevenueRate"],
            mode="markers+lines",  # 点线图
            name="当前营收率",
        )
        trace_max_retracement_rate = go.Scatter(
            x=df_revenues["stockName"],
            y=df_revenues["maxRetracementRate"],
            mode="markers+lines",  # 点线图
            name="最大回撤率",
        )
        fig.append_trace(trace_min_revenue_rate, row=1, col=1)
        fig.append_trace(trace_max_revenue_rate, row=1, col=1)
        fig.append_trace(trace_current_revenue_rate, row=1, col=1)
        fig.append_trace(trace_max_retracement_rate, row=1, col=1)
        # xy 轴说明
        fig.update_xaxes(title_text="股票", row=1, col=1)
        fig.update_yaxes(title_text="营收率", row=1, col=1)
        # 设置画布的名称和高宽
        fig["layout"].update(
            height=screen_hight * MAX_SUBPLOT_ROW / 2,
            width=screen_width,
            title="GoldenCross营收汇总",
        )

        file_name = IMAGE_OUTPUT_DIR + "TotalRevenuePoltly.html"
        fig.layout.template = PLOTLY_LAYOUT_TEMPLATE
        py_offline.plot(fig, filename=file_name)
