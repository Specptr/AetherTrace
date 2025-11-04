# AetherTrace | 以太轨迹

November 3, 2025

## 项目简介 | Project Overview

AetherTrace 是一个交互式运动可视化项目，
旨在学习 `matplotlib` 库的使用。
项目最初用于展示单位正方形内的随机点运动，
后来逐步扩展为一个动态系统，
具备轨迹追踪、速度分析、交互控制与美学设计等功能。

AetherTrace is an interactive motion visualization project
designed to explore and master the `matplotlib` library.
It began as a simple animation of random points within a unit square,
and gradually evolved into a dynamic system
that visualizes a moving point's trajectory and speed in real time,
with interactive target setting and aesthetic enhancements.

---

## 项目原理 | Motion Principle

程序启动后，动点Nomi将在一个 10×10 的单位正方形区域内开始运动。
它会以每帧 0.01 到 0.2 倍距离的速度向一个随机生成的目标点移动。
每帧间隔为 10 毫秒，因此速度单位为 **图像坐标单位/帧 × 100**，用于放大视觉效果。

当 Nomi 距离目标点小于 0.1 单位时，系统会自动生成一个新的目标点，保持运动的连续性。

整个运动过程中，Nomi 的坐标和速度会被实时记录，并绘制在右侧的速度图中。
该图每帧更新一次，保留最近 200 帧（约 2 秒）的速度数据，并每 50 帧重新计算一次最大速度。
平均速度也会被计算并以虚线标注。

用户可以通过鼠标点击主图区域，为 Nomi 设置新的目标点。
此时 Nomi 会以更高的速度（0.1 到 0.2 单位/帧）快速冲向目标，形成明显的加速效果。

为了增强可视化效果，系统会根据最近 0.5 秒（约 50 帧）内的最大速度值，动态调整最大速度文本的颜色。
颜色映射遵循以下渐变逻辑：
**白色 → 黄色 → 红色 → 深红色**，用于直观反映运动强度。

Upon launching the program, the moving point Nomi begins navigating within a 10×10 unit square.
It moves toward a randomly generated target at a speed ranging from 0.01 to 0.2 times the distance per frame.
Each frame interval is 10 milliseconds, so the speed unit is **units/frame × 100**, scaled for visual clarity.

When Nomi gets within 0.1 units of the target, a new random target is automatically assigned to maintain continuous motion.

Throughout the animation, Nomi’s position and speed are tracked in real time.
A side graph displays the speed history, updating every frame and retaining the latest 200 frames (≈2 seconds).
Maximum speed is recalculated every 50 frames, and the average speed is marked with a dashed reference line.

Users can interact by clicking anywhere in the main plot to assign a new target.
In response, Nomi accelerates toward the clicked location at a higher speed (0.1 to 0.2 units/frame),
creating a burst-like motion.

To enhance visual feedback, the color of the maximum speed label dynamically reflects the peak speed within the last 0.5 seconds (≈50 frames).
The color transitions through the following gradient:
**White → Yellow → Red → Dark Red**, intuitively representing motion intensity.


## 快速体验 | Quick Start (Windows Executable)

如果你只想直接体验程序，无需安装 Python，可下载打包好的 `.exe` 文件：
[点击这里下载 AetherTrace.exe](https://github.com/Specptr/AetherTrace/releases/download/v1.0/AetherTrace_v1.0.exe)

下载后双击运行即可。

## 致谢 | Acknowledgements

本项目的中英双语翻译由 Copilot 协助完成 Bilingual translation supported by Copilot

程序图标（像素风格 .ico）由 Cici 创作 Pixel-style .ico icon designed by Cici
