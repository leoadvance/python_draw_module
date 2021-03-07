# coding=utf-8

from typing import List

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Bar3D, Line, Scatter

DEFAULT_WIDTH = "1440px"

DATAZOOM_VERTICAL_POS_LEFT = "2%"  # 垂直缩放左边距


class PyechartsDraw:
    # def __init__(self):
    #
    #     pass
    #
    # def __del__(self):
    #     pass

    @classmethod
    def draw_line(
        cls, title: str, xaxis_data: List[str], yaxis_data: pd.DataFrame
    ) -> Line:
        """
        根据df内容绘制折线图
        :param title:           标题
        :param xaxis_data:      横轴数据
        :param yaxis_data:      纵轴绘制数据
        :return:
        """
        # 获取dataframe最大最小值
        min_data = yaxis_data.min().min()
        max_data = yaxis_data.max().max()
        c = (
            Line(init_opts=opts.InitOpts(width=DEFAULT_WIDTH))
            .add_xaxis(xaxis_data)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=title, pos_left="0%"),
                toolbox_opts=opts.ToolboxOpts(),  # 显示工具箱
                tooltip_opts=opts.TooltipOpts(is_show=True),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, type_="none"
                ),  # 指针移动时显示所有数值
                legend_opts=opts.LegendOpts(
                    is_show=True,
                    selected_mode="multiple",
                    # pos_bottom="0%",
                    # pos_right="0%",
                    # orient="vertical",
                ),  # 显示图例说明
                datazoom_opts=[
                    opts.DataZoomOpts(
                        range_start=0,
                        range_end=100,
                        orient="vertical",
                        pos_left=DATAZOOM_VERTICAL_POS_LEFT,
                    ),
                    opts.DataZoomOpts(range_start=0, range_end=100, orient="horizontal"),
                ],  # 增加缩放配置横纵轴都支持缩放
                # visualmap_opts = opts.VisualMapOpts(max_ = max_data, min_ = min_data, pos_bottom="10%")
            )
        )

        # 遍历dataframe 依次添加数据到y轴
        column_list = yaxis_data.columns.tolist()
        for column in column_list:
            c.add_yaxis(
                column,
                yaxis_data[column].tolist(),
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(type_="min", symbol_size=60),
                        opts.MarkPointItem(type_="max", symbol_size=60),
                    ]
                ),


            )
        return c

    @classmethod
    def draw_scatter(
        cls, title: str, xaxis_data: List[str], yaxis_data: pd.DataFrame
    ) -> Scatter:
        """
        根据df内容绘制散点
        :param title:           标题
        :param xaxis_data:      横轴数据
        :param yaxis_data:      纵轴绘制数据
        :return:
        """
        c = (
            Scatter(init_opts=opts.InitOpts(width=DEFAULT_WIDTH))
            .add_xaxis(xaxis_data)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=title),

                # 工具箱配置
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True,
                    orient="vertical",      # 纵向排列
                    pos_left = None,
                    pos_top="5%",
                    pos_right="5%",
                ),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, type_="none"
                ),  # 指针移动时显示所有数值
                # 配置图列
                legend_opts=opts.LegendOpts(
                    is_show=True,
                    # is_show=False,
                    selected_mode="multiple",# 支持多选
                    # pos_left="5%",          # 图列距离容器左侧百分比
                    pos_top="5%",  # 图列距离容器左侧百分比
                    # type_='scroll',          # 支持滚动查看到图列
                    # align = "left",
                    # pos_bottom="0%",
                    orient="horizontal",

                ),  # 显示图例说明
                datazoom_opts=[
                    opts.DataZoomOpts(
                        range_start=0,
                        range_end=100,
                        orient="vertical",
                        pos_left=DATAZOOM_VERTICAL_POS_LEFT,
                        pos_top="20%", pos_bottom="30%"


                    ),
                    opts.DataZoomOpts(range_start=0, range_end=100, orient="horizontal",pos_left="20%",pos_right="30%"),
                ],  # 增加缩放配置横纵轴都支持缩放
            )
        )
        # 遍历dataframe 依次添加数据到y轴
        column_list = yaxis_data.columns.tolist()
        for column in column_list:
            c.add_yaxis(
                        column,
                        yaxis_data[column].tolist(),
                        symbol_size=10,
                        label_opts=opts.LabelOpts(is_show=False),
                        )
        return c

    @classmethod
    def draw_bar(
        cls, title: str, xaxis_data: List[str], yaxis_data: pd.DataFrame
    ) -> Bar:
        """
        根据df内容绘制柱状图
        :param title:           标题
        :param xaxis_data:      横轴数据
        :param yaxis_data:      纵轴绘制数据
        :return:
        """
        # 获取dataframe最大最小值
        min_data = yaxis_data.min().min()
        max_data = yaxis_data.max().max()
        c = (
            Bar(
                init_opts=opts.InitOpts(
                    width=DEFAULT_WIDTH,
                    animation_opts=opts.AnimationOpts(
                        animation_delay=200, animation_easing="bounceOut"
                    ),  #   增加启动动效
                )
            )
            .add_xaxis(xaxis_data)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=title, pos_left="0%"),
                toolbox_opts=opts.ToolboxOpts(),  # 显示工具箱
                tooltip_opts=opts.TooltipOpts(is_show=True),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, type_="none"
                ),  # 指针移动时显示所有数值
                legend_opts=opts.LegendOpts(
                    is_show=True,
                    selected_mode="multiple",
                    # pos_bottom="0%",
                    # pos_right="0%",
                    # orient="vertical",
                ),  # 显示图例说明
                datazoom_opts=[
                    opts.DataZoomOpts(
                        range_start=0,
                        range_end=100,
                        orient="vertical",
                        pos_left=DATAZOOM_VERTICAL_POS_LEFT,
                    ),
                    opts.DataZoomOpts(range_start=0, range_end=100, orient="horizontal"),
                ],  # 增加缩放配置横纵轴都支持缩放
                # visualmap_opts=opts.VisualMapOpts(type_="color", max_=1, min_=-1),
                # visualmap_opts = opts.VisualMapOpts(max_ = max_data, min_ = min_data)
            )
        )
        # 遍历dataframe 依次添加数据到y轴
        column_list = yaxis_data.columns.tolist()
        for column in column_list:
            c.add_yaxis(
                column,
                yaxis_data[column].tolist(),
                # markpoint_opts=opts.MarkPointOpts(
                #     data=[
                #         opts.MarkPointItem(type_="min"),
                #         opts.MarkPointItem(type_="max"),
                #     ]
                # ),
            )
        return c

    @classmethod
    def draw_bar3D(cls, title: str, data: pd.DataFrame) -> Bar3D:
        """
        根据df内容绘制3D柱状图
        :param title:           标题
        :param data:            包含三轴数据的dataframe  index为x轴 column为Y轴 value为z轴
        :return:
        """
        data_list = []
        index_list = data.index.tolist()
        column_list = data.columns.tolist()

        # 获取dataframe最大最小值
        min_data = data.min().min()
        max_data = data.max().max()
        # 遍历dataframe，准备待操作数组
        for i in range(len(index_list)):
            for j in range(len(column_list)):
                # 记录 XYZ
                temp_list = [index_list[i], column_list[j], data.iloc[i, j]]
                # print(i,j,index_list[i],column_list[j])
                data_list.append(temp_list)

        c = (
            Bar3D(
                init_opts=opts.InitOpts(
                    width=DEFAULT_WIDTH,
                    animation_opts=opts.AnimationOpts(
                        animation_delay=200, animation_easing="bounceOut"
                    ),  #   增加启动动效
                )
            )
            .add(
                series_name=title,
                data=data_list,
                xaxis3d_opts=opts.Axis3DOpts(type_="category", data=index_list),
                yaxis3d_opts=opts.Axis3DOpts(type_="category", data=column_list),
                zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=title, pos_left="0%"),
                toolbox_opts=opts.ToolboxOpts(),  # 显示工具箱
                tooltip_opts=opts.TooltipOpts(is_show=True),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, type_="none"
                ),  # 指针移动时显示所有数值
                legend_opts=opts.LegendOpts(
                    is_show=True,
                    selected_mode="multiple",
                    # pos_bottom="0%",
                    # pos_right="0%",
                    # orient="vertical",
                ),  # 显示图例说明
                # datazoom_opts=[
                #     opts.DataZoomOpts(
                #         range_start=0, range_end=100, orient="vertical", pos_left="2%"
                #     ),
                #     opts.DataZoomOpts(range_start=0, range_end=100, orient="horizontal"),
                # ],  # 增加缩放配置横纵轴都支持缩放
                visualmap_opts=opts.VisualMapOpts(max_=max_data, min_=min_data)
                # visualmap_opts=opts.VisualMapOpts(type_="color", max_=1, min_=-1),
            )
        )
        return c
