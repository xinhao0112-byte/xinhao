# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 定义图像资源
image bg city = "images/bg.jpg"
image icon settings = "images/set.webp"
image icon close = "images/close.webp"
# 游戏开始
label start:

    # 显示主界面
    show screen main_interface     # 显示主界面屏幕（包含设置按钮）。
    
    "欢迎使用悬浮窗口演示程序。"
    "请点击右下角的设置图标打开悬浮窗口。"
    
    "在悬浮窗口中，您可以调整各种游戏设置。"
    "点击右上角的关闭图标可以关闭窗口。"
    
    "悬浮窗口带有背景虚化效果，使您专注于当前设置。"
    "感谢使用Ren'Py游戏引擎！"
    
    return