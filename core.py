# aethertrace/core.py

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import matplotlib.gridspec as gridspec
from .utils import speed_to_color
from . import config

class AetherTracePoint:
    def __init__(self):

        self.name = "Nomi"

        # 初始化图形窗口与子图布局 | Initialize figure and layout
        self.fig = plt.figure(figsize=config.FIGSIZE)
        self.fig.canvas.manager.set_window_title(config.WINDOW_TITLE)
        gs = gridspec.GridSpec(2, 2, height_ratios=config.HEIGHT_RATIOS, width_ratios=config.WIDTH_RATIOS)
        self.ax_main = self.fig.add_subplot(gs[:, 0])   # 主图区域 | Main plot
        self.ax_speed = self.fig.add_subplot(gs[1, 1])  # 速度图区域 | Speed graph

        # 主图设置 | Configure main plot
        self.ax_main.set_xlim(0, 10)
        self.ax_main.set_ylim(0, 10)
        self.ax_main.set_facecolor(config.MAIN_BG)
        self.fig.patch.set_facecolor(config.FIG_BG)

        # 速度图设置 | Configure speed graph
        self.ax_speed.set_xlim(0, config.SPEED_HISTORY)
        self.ax_speed.set_ylim(0, config.SPEED_YLIM)
        self.ax_speed.set_facecolor(config.SPEED_BG)
        self.ax_speed.tick_params(axis='y', labelsize=9, colors='white')

        # 图形元素 | Visual elements
        self.line, = self.ax_main.plot([], [], lw=2, color=config.LINE_COLOR)  # 轨迹线 | Trajectory line
        self.point, = self.ax_main.plot([], [], 'o', color=config.POINT_COLOR, markersize=1)  # 当前点 | Current point
        self.info_text = self.ax_main.text(11.5, 9, "", fontsize=9, ha='left', color='white')  # 坐标与速度信息 | Position & speed
        self.max_speed_text = self.ax_main.text(11.5, 8.5, "", fontsize=9, ha='left')          # 最大速度文本 | Max speed label

        # 数据初始化 | Initialize data
        self.current_pos = [random.uniform(0, 10), random.uniform(0, 10)]  # 当前坐标 | Current position
        self.target_pos = [random.uniform(0, 10), random.uniform(0, 10)]   # 目标坐标 | Target position
        self.target_speed = random.uniform(0.01, 0.2)                      # 初始速度 | Initial speed
        self.xdata, self.ydata = [], []                                   # 轨迹数据 | Trajectory data
        self.speed_buffer = []                                            # 最大速度缓存 | Max speed buffer
        self.speed_plot_y = []                                            # 速度图数据 | Speed graph data

        # 绑定鼠标事件 | Bind mouse click event
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        # 水印 | Watermark
        self.ax_main.text(0.1, -0.3, "Created by Specptr", fontsize=7, color='gray', alpha=0.5)

    def on_click(self, event):
        """鼠标点击事件：设置新目标点 | Mouse click event: assign new target"""
        if event.inaxes == self.ax_main and event.xdata is not None and event.ydata is not None:
            self.target_pos = [event.xdata, event.ydata]
            self.target_speed = random.uniform(0.1, 0.2)  # 鼠标点击时速度更快 | Faster speed on click

    def init_frame(self):
        """初始化动画帧 | Initialize animation frame"""
        self.line.set_data([], [])
        self.point.set_data([], [])
        self.info_text.set_text("")
        self.max_speed_text.set_text("")
        self.speed_buffer.clear()
        self.speed_plot_y.clear()
        self.ax_speed.clear()
        self.ax_speed.set_xlim(0, config.SPEED_HISTORY)
        self.ax_speed.set_ylim(0, config.SPEED_YLIM)
        return self.line, self.point, self.info_text, self.max_speed_text

    def update_frame(self, frame):
        """每帧更新逻辑 | Update logic for each frame"""
        dist = np.hypot(self.target_pos[0] - self.current_pos[0], self.target_pos[1] - self.current_pos[1])
        if dist < 0.15:
            # 到达目标点附近，生成新目标 | If close to target, assign new one
            self.target_pos = [random.uniform(0, 10), random.uniform(0, 10)]
            self.target_speed = random.uniform(0.01, 0.2)

        # 计算位移 | Calculate displacement
        dx = (self.target_pos[0] - self.current_pos[0]) * self.target_speed
        dy = (self.target_pos[1] - self.current_pos[1]) * self.target_speed
        self.current_pos[0] += dx
        self.current_pos[1] += dy

        # 计算速度 | Compute speed
        speed = np.hypot(dx, dy) * 100
        self.speed_buffer.append(speed)
        if len(self.speed_buffer) > 50:
            self.speed_buffer.pop(0)
        max_speed = max(self.speed_buffer)

        # 更新轨迹数据 | Update trajectory
        self.xdata.append(self.current_pos[0])
        self.ydata.append(self.current_pos[1])
        if len(self.xdata) > 10:
            self.xdata.pop(0)
            self.ydata.pop(0)

        # 更新图形元素 | Update visuals
        self.line.set_data(self.xdata, self.ydata)
        self.point.set_data([self.current_pos[0]], [self.current_pos[1]])
        self.info_text.set_text(
            f"{self.name} Position: ({self.current_pos[0]:.2f}, {self.current_pos[1]:.2f})\n"
            f"{self.name} Speed: {speed:06.2f}"
        )
        self.max_speed_text.set_text(f"Max Speed: {max_speed:.2f}")
        self.max_speed_text.set_color(speed_to_color(max_speed))

        # 更新速度图数据 | Update speed graph data
        self.speed_plot_y.append(speed)
        if len(self.speed_plot_y) > config.SPEED_HISTORY:
            self.speed_plot_y.pop(0)

        # 绘制速度图 | Draw speed graph
        self.ax_speed.clear()
        self.ax_speed.set_xlim(max(0, len(self.speed_plot_y) - config.SPEED_HISTORY), len(self.speed_plot_y))
        self.ax_speed.set_ylim(0, max(config.SPEED_YLIM, max(self.speed_plot_y)))
        self.ax_speed.plot(range(len(self.speed_plot_y)), self.speed_plot_y, color=config.SPEED_LINE_COLOR, linewidth=0.6)
        self.ax_speed.set_title("Speed", color='white', fontsize=9)
        self.ax_speed.tick_params(colors='white')
        self.ax_speed.set_xticks([])

        # 平均速度参考线 | Average speed reference line
        avg_speed = np.mean(self.speed_plot_y) if self.speed_plot_y else 0
        self.ax_speed.axhline(avg_speed, color=config.SPEED_AVG_LINE, linestyle='--', linewidth=0.5)
        self.ax_speed.text(len(self.speed_plot_y)-1, avg_speed + 2, f"Avg: {avg_speed:.1f}", color='white', fontsize=7, ha='right')

        # 设置边框颜色 | Set spine colors
        for spine in self.ax_speed.spines.values():
            spine.set_color('white')

        return self.line, self.point, self.info_text, self.max_speed_text

    def run(self):
        """启动动画 | Launch animation"""
        ani = FuncAnimation(self.fig, self.update_frame, init_func=self.init_frame, interval=10, blit=False)
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.3)
        plt.show()

