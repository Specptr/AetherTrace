# aethertrace/utils.py

"""
工具函数模块（Utils）
包含颜色映射等辅助功能
Utility functions for AetherTracePoint
"""

def speed_to_color(speed: float) -> str:
    """
    根据速度值映射颜色（白 → 黄 → 红 → 深红）
    Map speed value to color gradient
    """
    if speed < 50:
        b = int(255 - (speed / 50) * 255)
        return f'#FFFF{b:02X}'
    elif speed < 100:
        g = int(255 - ((speed - 50) / 50) * 255)
        return f'#FF{g:02X}00'
    else:
        r = int(max(112, 255 - (speed - 100) * 2))
        return f'#{r:02X}0000'
