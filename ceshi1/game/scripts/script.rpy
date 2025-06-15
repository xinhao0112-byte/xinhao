# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define s = Character("苏新皓")
define x = Character("信号灯")

image chuolian:
    "images/chuolian.jpg"
    zoom 1.3

define flag = 0

# 游戏在此开始。

label start:
    scene chuolian
    play music "audio/wuding.mp3"
    s "大家好。"
    s "我是小名叫帅帅长得也很帅帅的苏新皓"

    menu:
        "你想说些什么呢?"
        "很高兴认识你":
            "我也是"
            $ flag = 1
        "oi小鬼":
            "我才不是小鬼!"
            $ flag = 2
    

    if flag == 1:
        "你愿意陪我走一段吗"
    else:
        "你看起来也没有比我大很多嘛!"
    
    return

label s1:
    e ""
 



