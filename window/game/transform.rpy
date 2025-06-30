# 虚化效果
transform blur_transform:  #定义一个名为`blur_transform`的变换效果。
    matrixcolor BrightnessMatrix(0.0) * SaturationMatrix(0.5) * ContrastMatrix(0.7)     #使用矩阵运算调整图像颜色。这里通过调整亮度、饱和度和对比度来模拟模糊效果（虽然并非真正的模糊，但可以达到类似目的）。

# 悬浮窗口出现动画
transform float_in:    
    alpha 0.0 zoom 0.8
    easein 0.3 alpha 1.0 zoom 1.0

# 按钮悬停效果
transform button_hover:
    zoom 0.2
    on hover:    #当鼠标悬停时触发。
        ease 0.2 zoom 0.25
    on idle:     #当鼠标离开时触发。
        ease 0.2 zoom 0.2