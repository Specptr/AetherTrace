"""
配置模块
Config
集中管理项目中的颜色、尺寸、速度范围等参数
Configuration module for AetherTracePoint
"""

# ─────────────────────────────────────────────
# 项目元信息与窗口标题 | Project metadata & window title
WINDOW_TITLE = "AetherTrace: Nomi v1.2.0 — Specptr" # 主窗口标题 | Main window title
WINDOW_TITLE_PAUSED_SUFFIX = "Paused" # 暂停状态后缀 | Paused mode suffix
WINDOW_TITLE_MOUSE_MODE_SUFFIX = "Mouse Mode" # 鼠标模式后缀 | Mouse mode suffix
WINDOW_TITLE_GRID_SUFFIX = "Grid Mode" # 网格模式后缀 | Grid mode suffix

# ─────────────────────────────────────────────
# 图形窗口与布局设置 | Figure window & layout
FIGSIZE = (8, 3.4) # 窗口尺寸 | Window size
FIG_BG = "#000000" # 窗口背景色 | Window background color

SUBPLOT_ADJUST = {
    "left": 0.05,
    "right": 0.95,
    "top": 0.95,
    "bottom": 0.05,
    "wspace": 0.3
} # 子图间距调整 | Subplot spacing adjustments

HEIGHT_RATIOS = [3, 4] # 子图高度比例 | Subplot height ratios
WIDTH_RATIOS = [3, 1.6] # 子图宽度比例 | Subplot width ratios

# ─────────────────────────────────────────────
# 动画设置 | Animation settings
ANIMATION_INTERVAL = 10 # 动画更新间隔（毫秒）| Animation update interval (ms)
ANIMATION_BLIT = False # 是否启用blit以提升性能 | Enable blit for performance

# ─────────────────────────────────────────────
# 目标速度范围 | Target speed range
TARGET_SPEED_MIN = 0.01 # 最小目标速度 | Minimum target speed
TARGET_SPEED_MAX = 0.2 # 最大目标速度 | Maximum target speed

# ─────────────────────────────────────────────
# 主图设置 | Main plot appearance
POINT_SIZE = 0.1 # Nomi点大小 | Nomi point size
LINE_WIDTH = 1.2 # Nomi轨迹线宽度 | Nomi trajectory line width
MAIN_BG = "#1B1B1B" # 主图背景色 | Main plot background color
LINE_COLOR = "#7E7E7E" # 主图线条颜色 | Main plot line color
POINT_COLOR = "#FFFFFF" # 主图点颜色 | Main plot point color
TEXT_COLOR = "#FFFFFF" # 主图文本颜色 | Main plot text color
FOOTNOTE_COLOR = "#DDDDDD" # 主图脚注颜色 | Main plot footnote color
PAUSE_BG_COLOR = "#0D0D0D" # 暂停背景色 | Pause background color
RESUME_BG_COLOR = "#1B1B1B" # 恢复背景色 | Resume background color

# ─────────────────────────────────────────────
#  主图文本模板 | Main plot text templates
WATERMARK_TEXT = "Created by Specptr" # 水印文本 | Watermark text
HINT_TEXT = "[Space]=Pause  [T]=Grid Mode  [R]=New Target  [G]=Mouse Mode" # 提示文本 | Hint text
INFO_TEXT_TEMPLATE = "{name}'s Position: ({x:.4f}, {y:.4f})\n{name}'s Speed: {speed:06.4f}" # 信息文本模板 | Info text template
MAX_SPEED_TEXT_TEMPLATE = "Max Speed: {value:.2f}" # 最大速度文本模板 | Max speed text template
DISTANCE_TEXT_TEMPLATE = "Distance to Target: {value:.2f}"  # 到目标距离文本模板 | Distance to target text template
NEXT_TARGET_TEXT_TEMPLATE = "Next Target: {value:.2f}" # 下一个目标文本模板 | Next target text template

# ─────────────────────────────────────────────
# 速度图设置 | Speed graph settings
SPEED_BG = "#1B1B1B" # 速度图背景色 | Speed plot background color
SPEED_LINE_COLOR = "#5C5C5C" # 速度线颜色 | Speed line color
SPEED_AVG_LINE = "#FFFFFF" # 平均速度线颜色 | Average speed line color
SPEED_SPINE_COLOR = "#FFFFFF" # 速度图轴颜色 | Speed plot spine color
SPEED_TITLE_COLOR = "#FFFFFF"   # 速度图标题颜色 | Speed plot title color
SPEED_TICK_COLOR = "#FFFFFF" # 速度图刻度颜色 | Speed plot tick color
SPEED_AVG_TEXT_COLOR = "#FFFFFF" # 平均速度文本颜色 | Average speed text color
SPEED_LINE_WIDTH = 0.6 # 速度线宽度 | Speed line width
SPEED_AVG_LINE_WIDTH = 0.5 # 平均速度线宽度 | Average speed line width
SPEED_AVG_TEXT_TEMPLATE = "Avg: {avg:.1f}" # 平均速度文本模板 | Average speed text template
SPEED_AVG_TEXT_SIZE = 7 # 平均速度文本字体大小 | Average speed text font size
SPEED_HISTORY = 200 # 速度历史记录长度 | Speed history length
SPEED_YLIM = 100 # 速度图Y轴上限 | Speed plot Y-axis limit
SPEED_TICK_SIZE = 9 # 速度图刻度字体大小 | Speed plot tick font size
SPEED_TITLE = "Speed" # 速度图标题 | Speed plot title
SPEED_TITLE_SIZE = 9 # 速度图标题字体大小 | Speed plot title font size

# ─────────────────────────────────────────────
#  情绪图设置 | Mood plot settings
MOOD_BG = SPEED_BG # 情绪图背景色 | Mood plot background color
MOOD_X_RANGE = SPEED_HISTORY # 情绪图X轴范围 | Mood plot X-axis range
MOOD_Y_RANGE = (0, 30) # 情绪图Y轴范围 | Mood plot Y-axis range
MOOD_Y_TICKS = [5, 10, 15, 20, 25] # 情绪图Y轴刻度 | Mood plot Y-axis ticks
MOOD_Y_LABELS = ["Calm", "Relaxed", "Active", "Energetic", "Excited"] # 情绪图Y轴标签 | Mood plot Y-axis labels
MOOD_EMOJI_MARKS = {
    5: "😐", 10: "☺️", 15: "😃", 20: "😮", 25: "😆"
} # 情绪图表情符号标记 | Mood plot emoji marks
MOOD_LABEL_FONT_SIZE = 9 # 情绪图标签字体大小 | Mood plot label font size
MOOD_TICK_COLOR = "#FF7700" # 情绪图刻度颜色 | Mood plot tick color
MOOD_SPINE_COLOR = "#FFFFFF" # 情绪图轴颜色 | Mood plot spine color
MOOD_TITLE = "Mood" # 情绪图标题 | Mood plot title
MOOD_TITLE_COLOR = "#FFFFFF"  # 情绪图标题颜色 | Mood plot title color
MOOD_TITLE_SIZE = 9 # 情绪图标题字体大小 | Mood plot title font size
MOOD_LINE_COLOR = "#FF7700" # 情绪图线条颜色 | Mood plot line color
MOOD_LINE_WIDTH = 0.6 # 情绪图线条宽度 | Mood plot line width
MOOD_POINT_SIZE = 3 # 情绪图点大小 | Mood plot point size
MOOD_SMOOTHNESS = 10 # 情绪图平滑度 | Mood plot smoothness

# ─────────────────────────────────────────────
#  手动显示设置 | Manual toggle settings
GRID_COLOR = "gray" # 网格颜色 | Grid color
GRID_STYLE = ":" # 网格线样式 | Grid line style
GRID_WIDTH = 0.2 # 网格线宽度 | Grid line width
TARGET_MARKER_STYLE = "x" # 目标标记样式 | Target marker style
TARGET_MARKER_COLOR = "red" # 目标标记颜色 | Target marker color
TARGET_MARKER_SIZE = 6 # 目标标记大小 | Target marker size
