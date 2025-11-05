# AetherTrace | 以太轨迹

November 3, 2025

---
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
##项目原理 | Motion Principle

Nomi 是一个在二维平面中持续运动的点，具备目标导航、速度调节、用户交互和视觉反馈四个核心机制。程序启动后，Nomi 会在一个 10×10 单位区域内随机选择目标并向其移动。每帧间隔 10 毫秒，速度为目标距离的 0.01–0.2 倍（单位：单位/帧 ×100）。当与目标距离小于 0.15 时，会自动生成新的目标点以保持连续运动。
用户可通过鼠标点击设置新目标。此时 Nomi 会以更高速度（0.1–0.2 单位/帧）快速冲向目标，形成加速效果。
键盘交互包括：
Space：暂停 / 恢复动画（暂停时画面变暗）
T：切换网格与目标点显示
G：启用鼠标引导模式，让 Nomi 跟随光标
R：刷新目标点
当前模式会显示在窗口标题中。
系统实时记录 Nomi 的位置与速度，并在右侧绘制速度曲线。曲线保留最近 200 帧数据（约 2 秒），每 50 帧更新一次最大速度。平均速度以虚线标注，最大速度文字颜色随近期峰值变化（白 → 黄 → 红 → 深红），反映运动强度。
程序内置情绪系统，根据最近平均速度判断 Nomi 的“状态”，共五档：Calm、Relaxed、Active、Energetic、Excited。情绪状态显示在主图文本区域，并以橙色 emoji 曲线形式呈现在情绪图中，突出短期变化。
文本信息区域显示目标距离，包括新目标的初始距离与当前距离。水印旁附暂停提示。视觉上，Nomi 的体积和轨迹略微缩小，布局调整以容纳情绪图，使画面更紧凑清晰。

Nomi is a continuously moving point in a 2D plane, driven by four core systems: target navigation, speed control, user interaction, and visual feedback.
At launch, Nomi moves within a 10×10 unit area toward a randomly generated target. Each frame updates every 10 ms, and the movement speed is 0.01–0.2 times the target distance (units/frame ×100).
When the distance to the target falls below 0.15 units, a new target is automatically generated to maintain continuous motion.
Users can set a new target by clicking on the main plot. Nomi will accelerate toward it at a higher speed (0.1–0.2 units/frame), creating a burst motion.
Keyboard controls:
Space — Pause / Resume animation (screen dims when paused)
T — Toggle grid and target visibility
G — Enable mouse-guided mode (Nomi follows cursor)
R — Refresh target instantly
The current mode is shown in the window title.
Nomi’s position and velocity are tracked in real time and plotted on a speed graph. The graph keeps the latest 200 frames (~2 seconds) and updates the max speed every 50 frames. The average speed is marked with a dashed line, while the max-speed label color shifts (white → yellow → red → dark red) to visualize recent intensity.
A built-in mood system maps recent average speed to five emotional states: Calm, Relaxed, Active, Energetic, and Excited.
The current mood is displayed in the main plot and visualized in a separate mood graph with orange emoji markers emphasizing short-term changes.
The text area shows distance metrics — the initial distance to each new target and the real-time distance to the current one.
A pause hint is displayed near the watermark.
Visually, Nomi’s size and trail are slightly reduced, and the layout is optimized to fit the mood graph for a more compact and balanced interface.

---
## 致谢 | Acknowledgements

本项目的中英双语翻译由 Copilot 协助完成 Bilingual translation supported by Copilot

程序图标（像素风格 .ico）由 Cici 创作 Pixel-style .ico icon designed by Cici
