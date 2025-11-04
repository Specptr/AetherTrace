# aethertrace/config.py

"""
配置模块（Config）
集中管理项目中的颜色、尺寸、速度范围等参数
Configuration module for AetherTracePoint
"""

# 图形窗口设置 | Figure window settings
WINDOW_TITLE = "AetherTrace: Nomi v1.1 — Specptr" # 窗口标题 | Window title
FIGSIZE = (8, 3.4)              # 窗口尺寸 (宽, 高) | Figure size (width, height)
FIG_BG = "#000000"          # 整体背景颜色 | Overall figure background color

# 主图设置 | Main plot settings
MAIN_BG = "#1B1B1B"           # 主图背景色 | Background color of main plot
LINE_COLOR = "#9e9e9e"        # 轨迹线颜色 | Trajectory line color
POINT_COLOR = "#ffffff"       # 当前点颜色 | Current point (Nomi) color

# 速度图设置 | Speed graph settings
SPEED_BG = "#1B1B1B"          # 速度图背景色 | Background color of speed graph
SPEED_LINE_COLOR = "#5C5C5C"  # 速度曲线颜色 | Speed curve color
SPEED_AVG_LINE = "#ffffff"    # 平均速度参考线颜色 | Average speed reference line color
SPEED_HISTORY = 200           # 显示最近多少帧速度 | Number of recent frames to display
SPEED_YLIM = 100              # 速度图纵轴最大值 | Maximum Y-axis value of speed graph

# 布局比例（GridSpec）| Layout ratios (GridSpec)
HEIGHT_RATIOS = [3, 4]        # 主图与速度图的垂直高度比例 | Vertical height ratio: main plot vs speed graph
WIDTH_RATIOS = [3, 1.6]       # 主图与速度图的水平宽度比例 | Horizontal width ratio: main plot vs speed graph

