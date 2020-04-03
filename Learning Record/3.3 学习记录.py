# 1.正则表达式是一种用来匹配字符串的好工具，描述性语言定义规则
#   描述字符：给出字母-精确匹配 \d 数字；\w 字母或数字； .匹配任意字符
#   字符长度：*任意长度；+至少1个；？0个或1个字符；{n}n个；{n,m}n-m个
# 2.turtle.setup(width,height,startx,starty)
# 3.坐标绝对：turtle.goto(x,y)
#   海龟坐标：turtle.fowafd(d)前进 别名turtle.fd(d)
#            turtle.bk（d)后退
#            turtle.circle(r,angle)在左侧以曲线运行 
#   空间角度：turtle.seth(angle)改变海归行进方向，angle绝对度数
#   海龟角度：turtle.left(angle)、turtle.right(angle)
# 4.RGB颜色模式： turtle.colormode(mode) 1.0 小数值模式，255整数值模式
# 5.import <库名> as <库别名> import turtle as t  
# 6.画笔控制函数：
#   turtle.penup turtle.pu  turtle.pendown turtle.pd
#   turtle.pensize(width) 别名turtle.width(width)名字不同，功能一样
#   turtle.pencolor(color) 参数：颜色字符串'red' 、RGB小数值或元组值