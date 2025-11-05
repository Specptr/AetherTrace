# AetherTrace | 以太轨迹

November 3, 2025

---
## 项目简介 | Project Overview

AetherTrace 是一个交互式运动可视化项目，
旨在学习 `matplotlib` 库的使用。
项目最初用于展示单位正方形内的随机点运动，
后来逐步扩展为一个可交互式动态系统。

AetherTrace is an interactive motion visualization project 
designed to explore and learn the use of the `matplotlib` library. 
It began as a simple demonstration of random point movement within a unit square, 
and gradually evolved into an interactive dynamic system.

---
## 项目具体描述 | Detailed Project Description
Nomi 是一个在二维平面中持续运动的点。  
Nomi is a continuously moving point in a 2D plane.

程序启动后，Nomi 会在一个 10×10 单位区域内随机选择目标并以随机速度向其移动。
当与目标距离小于 0.15 时，Nomi会找到新的目标点并再次移动，持续至程序关闭。  
Upon program launch, Nomi randomly selects a target within a 10×10 unit area and moves toward it at a random speed. 
When the distance to the target falls below 0.15 units, a new target is selected and the motion continues until the program is closed.

用户可通过鼠标点击设置新目标。
对于用户选择的目标，Nomi会以更高速度冲向它。  
Users can set a new target by clicking with the mouse. 
Nomi will accelerate toward the user-defined target at a higher speed.

程序配备一系列键盘交互，包括： 
Space：冻结Nomi（暂停，此时画面变暗） 
T：切换网格与目标点显示  
G：启用鼠标引导模式，让 Nomi 跟随光标  
R：刷新一个新的随机目标点  
当前模式会显示在窗口标题中。  
The program supports a series of keyboard interactions, including:
Space: Freeze Nomi (pause; the screen dims during pause)  
T: Toggle grid and target point visibility  
G: Enable mouse-guided mode, allowing Nomi to follow the cursor 
R: Refresh a new random target point  
The current mode is displayed in the window title.


系统实时记录 Nomi 的位置与速度，每 50 帧更新一次最大速度。  
The system tracks Nomi’s position and speed in real time, updating the maximum speed every 50 frames.  
右侧绘制有速度曲线。  
A speed curve is plotted on the right side.  
曲线保留最近几秒数据，持续绘制。对于最近保留的数据会计算出平均速度，在速度图中以虚线标注。  
The curve retains several seconds of recent data and is continuously updated. The average speed is calculated from the retained data and marked with a dashed line on the speed graph.

程序内置情绪系统。 Nomi的情绪值共五档：Calm、Relaxed、Active、Energetic、Excited。  
The program includes a built-in mood system. Nomi’s mood has five levels: Calm, Relaxed, Active, Energetic, Excited.  
情绪状态显示在主图文本区域，并以橙色 emoji 曲线形式呈现在情绪图中。  
The mood state is displayed in the main plot text area and visualized as an orange emoji curve in the mood graph.  
情绪图像保留数据不与速度图像一致。  
The mood graph retains a different set of data than the speed graph.

所有测得的Nomi的数据显示在右上方文本信息区域。包括：  
-位置信息  
-瞬时速度信息  
-最大速度信息（文字颜色会随着值不断变化而变化）  
-当前情绪状态信息  
-新生成目标点的直线距离  
-当前距离目标点的直线距离  
All measured data about Nomi is displayed in the top-right text information area, including:  
-Position information  
-Instantaneous speed  
-Maximum speed (text color changes dynamically based on value)  
-Current mood state  
-Straight-line distance to newly generated target  
-Straight-line distance to current target

视觉效果如字体大小，颜色，线粗等均可在配置文件里更改。  
Visual elements such as font size, color, and line thickness can be adjusted in the configuration file.

---
## 致谢 | Acknowledgements

本项目的中英双语翻译由 Copilot 协助完成 Bilingual translation supported by Copilot

程序图标（像素风格 .ico）由 Cici 创作 Pixel-style .ico icon designed by Cici
