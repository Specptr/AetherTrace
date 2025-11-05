# aethertrace/core.py

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import matplotlib.gridspec as gridspec
from .utils import speed_to_color, get_mood
from . import config
from matplotlib.collections import LineCollection

class AetherTracePoint:
    def __init__(self):
        # 基本属性初始化 | Basic attributes
        self.name = "Nomi"                # 它的名字 | Its name
        self.paused = False                # 暂停状态 | Pause state
        self.mood_history = []          # 情绪历史数据 | Mood history data
        self.show_grid_and_target = False   # 显示网格与目标点标记 | Show grid and target marker
        self.target_marker = None    # 目标点标记对象 | Target marker object
        self.manual_control = False  # 手动控制模式 | Manual control mode
        self.mouse_pos = [0, 0]      # 鼠标位置 | Mouse position

        # 图形窗口与布局 | Figure and layout
        self.fig = plt.figure(figsize=config.FIGSIZE)   #设置图形窗口大小 | Set figure size
        self.fig.canvas.manager.set_window_title(config.WINDOW_TITLE)   #设置窗口标题 | Set window title
        gs = gridspec.GridSpec(2, 3, height_ratios=config.HEIGHT_RATIOS, width_ratios=[2, 1, 1])  #定义网格布局 | Define grid layout
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)  #鼠标移动事件 | Mouse move event

        # 子图区域 | Subplots
        self.ax_main = self.fig.add_subplot(gs[:, 0])   # 主图区域
        self.ax_mood = self.fig.add_subplot(gs[1, 1])   # 情绪图区域
        self.ax_speed = self.fig.add_subplot(gs[1, 2])  # 速度图区域

        # 主图设置 | Main plot configuration
        self.ax_main.set_xlim(0, 10)
        self.ax_main.set_ylim(0, 10)
        self.ax_main.set_facecolor(config.MAIN_BG)  # 主图背景色 | Main plot background color
        self.fig.patch.set_facecolor(config.FIG_BG) # 整体背景色 | Overall background color

        # 速度图设置 | Speed plot configuration
        self.ax_speed.set_xlim(0, config.SPEED_HISTORY) # X 轴显示最近多少帧 | X-axis shows recent frames
        self.ax_speed.set_ylim(0, config.SPEED_YLIM)    # Y 轴范围 | Y-axis range
        self.ax_speed.set_facecolor(config.SPEED_BG)    # 速度图背景色 | Speed plot background color
        self.ax_speed.tick_params(axis='y', labelsize=config.SPEED_TICK_SIZE, colors=config.SPEED_TICK_COLOR)   # Y 轴刻度设置 | Y-axis tick settings
        self.ax_speed.set_title(config.SPEED_TITLE, color=config.SPEED_TITLE_COLOR, fontsize=config.SPEED_TITLE_SIZE)   # 标题 | Title

        # 情绪图设置 | Mood plot configuration
        self.ax_mood.set_facecolor(config.MOOD_BG)  # 情绪图背景色 | Mood plot background color
        self.ax_mood.set_xlim(0, config.MOOD_X_RANGE)   # X 轴显示帧数 | X-axis shows frames
        self.ax_mood.set_ylim(*config.MOOD_Y_RANGE)  # Y 轴范围 | Y-axis range
        self.ax_mood.set_yticks(config.MOOD_Y_TICKS)    # Y 轴刻度位置 | Y-axis tick positions
        self.ax_mood.set_yticklabels(config.MOOD_Y_LABELS, fontsize=config.MOOD_LABEL_FONT_SIZE)    # Y 轴刻度标签 | Y-axis tick labels
        self.ax_mood.tick_params(colors=config.MOOD_TICK_COLOR)   # 刻度颜色 | Tick colors
        self.ax_mood.set_xticks([]) # 隐藏 X 轴刻度 | Hide X-axis ticks
        for spine in self.ax_mood.spines.values():
            spine.set_color(config.MOOD_SPINE_COLOR)    # 坐标轴边框颜色 | Spine colors
        self.ax_mood.set_title(config.MOOD_TITLE, color=config.MOOD_TITLE_COLOR, fontsize=config.MOOD_TITLE_SIZE)   # 标题 | Title

        # 图形元素 | Visual elements
        self.line, = self.ax_main.plot([], [], lw=2, color=config.LINE_COLOR)   # 轨迹线 | Trajectory line
        self.point, = self.ax_main.plot([], [], 'o', color=config.POINT_COLOR, markersize=1)    # 当前点 | Current point (Nomi)

        self.info_text = self.ax_main.text(11.5, 9, "", fontsize=9, ha='left', color=config.TEXT_COLOR)   # 信息文本 | Info text
        self.max_speed_text = self.ax_main.text(11.5, 8.5, "", fontsize=9, ha='left')   # 最大速度文本 | Max speed text
        self.mood_text = self.ax_main.text(11.5, 8.0, "", fontsize=9, ha='left', color=config.TEXT_COLOR)  # 情绪文本 | Mood text
        self.next_target_text = self.ax_main.text(11.5, 7.5, "", fontsize=9, ha='left', color=config.TEXT_COLOR)  # 下一个目标文本 | Next target text
        self.distance_text = self.ax_main.text(11.5, 7.0, "", fontsize=9, ha='left', color=config.TEXT_COLOR)  # 距离文本 | Distance text

        self.ax_main.text(0.1, -0.4, config.WATERMARK_TEXT, fontsize=7, color=config.FOOTNOTE_COLOR, alpha=0.5)  # 水印 | Watermark
        self.ax_main.text(3.5, -0.4, config.HINT_TEXT, fontsize=7, color=config.FOOTNOTE_COLOR, alpha=0.5)   # 操作提示 | Instruction text

        # 数据初始化 | Data initialization
        self.current_pos = [random.uniform(0, 10), random.uniform(0, 10)]   # 当前点位置 | Current point position
        self.target_pos = [random.uniform(0, 10), random.uniform(0, 10)]    # 目标点位置 | Target point position
        self.target_speed = random.uniform(0.01, 0.2)                     # 目标速度 | Target speed
        self.xdata, self.ydata = [], [] # 轨迹数据 | Trajectory data
        self.speed_buffer = []  # 速度缓冲区 | Speed buffer
        self.speed_plot_y = []  # 速度图数据 | Speed plot data

        # 事件绑定 | Event bindings
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)    #鼠标点击事件 | Mouse click event
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)   #键盘按键事件 | Key press event

    def on_click(self, event):
        #鼠标点击事件：设置新目标点 | Mouse click event: assign new target
        if event.inaxes == self.ax_main and event.xdata is not None and event.ydata is not None:
            self.target_pos = [event.xdata, event.ydata]
            self.target_speed = random.uniform(0.1, 0.2)  # 鼠标点击时速度更快 | Faster speed on click

    def init_frame(self):
        #初始化动画帧 | Initialize animation frame
        self.line.set_data([], [])
        self.point.set_data([], [])
        self.info_text.set_text("")
        self.max_speed_text.set_text("")
        self.speed_buffer.clear()
        self.speed_plot_y.clear()
        self.ax_speed.clear()
        self.ax_speed.set_xlim(0, config.SPEED_HISTORY)
        self.ax_speed.set_ylim(0, config.SPEED_YLIM)
        self.distance_text.set_text("")
        dist = np.hypot(self.target_pos[0] - self.current_pos[0], self.target_pos[1] - self.current_pos[1])
        self.next_target_text.set_text(f"Next Target: {dist:.2f}")
        return self.line, self.point, self.info_text, self.max_speed_text, self.distance_text, self.next_target_text

    def update_frame(self, frame):
        # 每帧更新逻辑 | Update logic for each frame
        if self.paused:
            return self.line, self.point, self.info_text, self.max_speed_text, self.distance_text, self.next_target_text
        # 如果暂停则不更新 | Do not update if paused

        # ─────────────────────────────────────────────
        # 目标点逻辑 | Target logic
        dist = np.hypot(self.target_pos[0] - self.current_pos[0], self.target_pos[1] - self.current_pos[1]) # 计算与目标点距离 | Calculate distance to target
        adjusted_dist = max(0.0, dist - 0.14) # 调整距离显示 | Adjusted distance display
        self.distance_text.set_text(config.DISTANCE_TEXT_TEMPLATE.format(value=adjusted_dist))  # 更新距离文本 | Update distance text

        if not self.manual_control and dist < 0.15:
            self.target_pos = [random.uniform(0, 10), random.uniform(0, 10)]  # 达到目标点后生成新目标点 | Generate new target point upon reaching
            self.target_speed = random.uniform(config.TARGET_SPEED_MIN, config.TARGET_SPEED_MAX) # 新目标点速度 | New target speed
            new_dist = np.hypot(self.target_pos[0] - self.current_pos[0], self.target_pos[1] - self.current_pos[1]) # 计算新目标点距离 | Calculate new target distance
            self.next_target_text.set_text(config.NEXT_TARGET_TEXT_TEMPLATE.format(value=new_dist)) # 更新下一个目标文本 | Update next target text

        # ─────────────────────────────────────────────
        # 位移与速度计算 | Movement and speed
        if self.manual_control and self.mouse_pos is not None: # 手动控制模式 | Manual control mode v1.2
            dx = self.mouse_pos[0] - self.current_pos[0]
            dy = self.mouse_pos[1] - self.current_pos[1]
            self.current_pos = self.mouse_pos.copy()
        else:
            dx = (self.target_pos[0] - self.current_pos[0]) * self.target_speed
            dy = (self.target_pos[1] - self.current_pos[1]) * self.target_speed
            self.current_pos[0] += dx
            self.current_pos[1] += dy


        speed = np.hypot(dx, dy) * 100 # 计算当前速度 | Calculate current speed
        self.speed_buffer.append(speed) # 更新速度缓冲区 | Update speed buffer
        if len(self.speed_buffer) > 50:
            self.speed_buffer.pop(0)
        max_speed = max(self.speed_buffer)

        # ─────────────────────────────────────────────
        # 轨迹更新 | Trajectory update
        self.xdata.append(self.current_pos[0])
        self.ydata.append(self.current_pos[1])
        if len(self.xdata) > 10:
            self.xdata.pop(0)
            self.ydata.pop(0)

        # ─────────────────────────────────────────────
        # 主图元素更新 | Main plot visuals
        self.line.set_data(self.xdata, self.ydata)
        self.point.set_data([self.current_pos[0]], [self.current_pos[1]])

        self.info_text.set_text(config.INFO_TEXT_TEMPLATE.format(
            name=self.name,
            x=self.current_pos[0],
            y=self.current_pos[1],
            speed=speed
        ))

        self.max_speed_text.set_text(config.MAX_SPEED_TEXT_TEMPLATE.format(value=max_speed))
        self.max_speed_text.set_color(speed_to_color(max_speed))

        # ─────────────────────────────────────────────
        # 网格与目标点显示控制 | Grid and target marker v1.2
        if self.show_grid_and_target:
            # 设置更密集的刻度线（每 0.5 单位）
            self.ax_main.set_xticks(np.arange(0, 10.1, 0.5))
            self.ax_main.set_yticks(np.arange(0, 10.1, 0.5))

            # 显示网格
            self.ax_main.grid(True, color=config.GRID_COLOR, linestyle=config.GRID_STYLE, linewidth=config.GRID_WIDTH)

            # 显示目标点标记
            if self.target_marker:
                self.target_marker.set_data([self.target_pos[0]], [self.target_pos[1]])
            else:
                self.target_marker, = self.ax_main.plot(
                    self.target_pos[0], self.target_pos[1],
                    marker=config.TARGET_MARKER_STYLE,
                    color=config.TARGET_MARKER_COLOR,
                    markersize=config.TARGET_MARKER_SIZE,
                    label='Target'
                )
        else:
            # 清除刻度与网格
            self.ax_main.set_xticks([])
            self.ax_main.set_yticks([])
            self.ax_main.grid(False)

            # 移除目标点标记
            if self.target_marker:
                self.target_marker.remove()
                self.target_marker = None

        # ─────────────────────────────────────────────
        # 速度图更新 | Speed graph update
        self.speed_plot_y.append(speed) # 更新速度图数据 | Update speed plot data
        if len(self.speed_plot_y) > config.SPEED_HISTORY:
            self.speed_plot_y.pop(0)    # 保持速度图数据长度 | Maintain speed plot data length
        avg_speed = np.mean(self.speed_plot_y) if self.speed_plot_y else 0 # 计算平均速度 | Calculate average speed
        self.ax_speed.clear() # 清除速度图 | Clear speed plot
        self.ax_speed.set_xlim(max(0, len(self.speed_plot_y) - config.SPEED_HISTORY), len(self.speed_plot_y)) # X 轴范围 | X-axis range
        self.ax_speed.set_ylim(0, max(config.SPEED_YLIM, max(self.speed_plot_y)))   # Y 轴范围 | Y-axis range
        self.ax_speed.plot(
            range(len(self.speed_plot_y)),
            self.speed_plot_y,
            color=config.SPEED_LINE_COLOR,
            linewidth=config.SPEED_LINE_WIDTH
        )
        self.ax_speed.axhline(
            avg_speed,
            color=config.SPEED_AVG_LINE,
            linestyle='--',
            linewidth=config.SPEED_AVG_LINE_WIDTH
        )
        self.ax_speed.text(
            len(self.speed_plot_y)-1,
            avg_speed + 2,
            config.SPEED_AVG_TEXT_TEMPLATE.format(avg=avg_speed),
            color=config.SPEED_AVG_TEXT_COLOR,
            fontsize=config.SPEED_AVG_TEXT_SIZE,
            ha='right'
        )
        self.ax_speed.set_title(config.SPEED_TITLE, color=config.SPEED_TITLE_COLOR, fontsize=config.SPEED_TITLE_SIZE) # 标题 | Title
        self.ax_speed.tick_params(colors=config.SPEED_TICK_COLOR) # 刻度颜色 | Tick colors
        self.ax_speed.set_xticks([]) # 隐藏 X 轴刻度 | Hide X-axis ticks
        for spine in self.ax_speed.spines.values():   # 坐标轴边框颜色 | Spine colors
            spine.set_color(config.SPEED_SPINE_COLOR)

        # ─────────────────────────────────────────────
        # 情绪图更新 | Mood graph update v1.1
        mood = get_mood(avg_speed) # 获取当前情绪 | Get current mood
        self.mood_text.set_text(f"Mood: {mood}") # 更新情绪文本 | Update mood text

        for _ in range(2): # 每帧更新两次情绪数据以平滑曲线 | Update mood data twice per frame for smoothing
            self.mood_history.append(avg_speed)
            if len(self.mood_history) > config.SPEED_HISTORY:
                self.mood_history.pop(0)

        self.ax_mood.clear() # 清除情绪图 | Clear mood plot
        self.ax_mood.set_facecolor(config.MOOD_BG) # 情绪图背景色 | Mood plot background color
        self.ax_mood.set_xlim(
            max(0, len(self.mood_history) - config.MOOD_X_RANGE),
            len(self.mood_history)
        )
        self.ax_mood.set_ylim(*config.MOOD_Y_RANGE) # Y 轴范围 | Y-axis range
        self.ax_mood.set_yticks(list(config.MOOD_EMOJI_MARKS.keys()))   # Y 轴刻度位置 | Y-axis tick positions
        self.ax_mood.set_yticklabels(
            list(config.MOOD_EMOJI_MARKS.values()),
            fontsize=config.MOOD_LABEL_FONT_SIZE
        ) # Y 轴刻度标签 | Y-axis tick labels
        self.ax_mood.set_title(config.MOOD_TITLE, color=config.MOOD_TITLE_COLOR, fontsize=config.MOOD_TITLE_SIZE)  # 标题 | Title
        self.ax_mood.tick_params(colors=config.MOOD_TICK_COLOR)  # 刻度颜色 | Tick colors
        self.ax_mood.set_xticks([]) # 隐藏 X 轴刻度 | Hide X-axis ticks
        for spine in self.ax_mood.spines.values():
            spine.set_color(config.MOOD_SPINE_COLOR)    # 坐标轴边框颜色 | Spine colors

        if len(self.mood_history) >= 2:  # 平滑情绪曲线 | Smooth mood curve v1.1.1
            x = np.arange(len(self.mood_history))
            x_smooth = np.linspace(x.min(), x.max(), len(x) * config.MOOD_SMOOTHNESS)
            y_smooth = np.interp(x_smooth, x, self.mood_history)
            self.ax_mood.plot(x_smooth, y_smooth, color=config.MOOD_LINE_COLOR, linewidth=config.MOOD_LINE_WIDTH)
        elif len(self.mood_history) == 1:
            self.ax_mood.plot([0], [self.mood_history[0]], 'o', color=config.MOOD_LINE_COLOR, markersize=config.MOOD_POINT_SIZE)

        # ─────────────────────────────────────────────
        # 返回更新后的图形元素 | Return updated artists
        return self.line, self.point, self.info_text, self.max_speed_text, self.distance_text, self.next_target_text

    def on_key_press(self, event):
        key = event.key.lower()
        print("Key pressed:", repr(key))

        if key == ' ': # 暂停/继续动画 | Toggle pause/resume v1.1
            self.paused = not self.paused
            title = config.WINDOW_TITLE
            if self.paused:
                title += " | " + config.WINDOW_TITLE_PAUSED_SUFFIX
            if self.manual_control:
                title += " | " + config.WINDOW_TITLE_MOUSE_MODE_SUFFIX
            if self.show_grid_and_target:
                title += " | " + config.WINDOW_TITLE_GRID_SUFFIX
            self.fig.canvas.manager.set_window_title(title)
            self.ax_main.set_facecolor(config.PAUSE_BG_COLOR if self.paused else config.RESUME_BG_COLOR)
            self.fig.canvas.draw_idle()
            print("Paused" if self.paused else "Resumed")

        elif key == 't': # 切换网格与目标点显示 | Toggle grid and target marker v1.2
            self.show_grid_and_target = not self.show_grid_and_target
            print("Grid & Target:", "Visible" if self.show_grid_and_target else "Hidden")
            title = config.WINDOW_TITLE
            if self.paused:
                title += " | " + config.WINDOW_TITLE_PAUSED_SUFFIX
            if self.manual_control:
                title += " | " + config.WINDOW_TITLE_MOUSE_MODE_SUFFIX
            if self.show_grid_and_target:
                title += " | " + config.WINDOW_TITLE_GRID_SUFFIX
            self.fig.canvas.manager.set_window_title(title)

        elif key == 'g': # 切换鼠标控制模式 | Toggle mouse control mode v1.2
            self.manual_control = not self.manual_control
            print("Mouse control mode:", "ON" if self.manual_control else "OFF")

            title = config.WINDOW_TITLE
            if self.paused:
                title += " | " + config.WINDOW_TITLE_PAUSED_SUFFIX
            if self.manual_control:
                title += " | " + config.WINDOW_TITLE_MOUSE_MODE_SUFFIX
            if self.show_grid_and_target:
                title += " | " + config.WINDOW_TITLE_GRID_SUFFIX
            self.fig.canvas.manager.set_window_title(title)

        elif key == 'r': # 生成新目标点 | Generate new target point v1.2
            if not self.manual_control:
                self.target_pos = [random.uniform(0, 10), random.uniform(0, 10)]
                self.target_speed = random.uniform(config.TARGET_SPEED_MIN, config.TARGET_SPEED_MAX)
                new_dist = np.hypot(self.target_pos[0] - self.current_pos[0], self.target_pos[1] - self.current_pos[1])
                self.next_target_text.set_text(config.NEXT_TARGET_TEXT_TEMPLATE.format(value=new_dist))
                print(f"New target manually generated at: [{self.target_pos[0]:.2f}, {self.target_pos[1]:.2f}]")

    def on_mouse_move(self, event): # 鼠标移动事件 | Mouse move event v1.2
        if self.manual_control and event.inaxes == self.ax_main:
            if event.xdata is not None and event.ydata is not None:
                self.mouse_pos = [event.xdata, event.ydata]
        else:
            self.mouse_pos = None  # 鼠标不在主图区域

    def run(self):
        # 启动动画 | Launch animation
        ani = FuncAnimation(
        self.fig,
        self.update_frame,
        init_func=self.init_frame,
        interval=config.ANIMATION_INTERVAL,
        blit=config.ANIMATION_BLIT,
        save_count=500  # 帧缓冲区大小 | Frame buffer size v1.2
    )
        plt.subplots_adjust(**config.SUBPLOT_ADJUST)
        plt.show()
