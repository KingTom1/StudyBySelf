# pyhton大小写敏感
# 程序编写模板 IPO思想  input函数获取用户输入I， 处理P ， print输出O
# 绘制小蟒蛇程序
import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad, angle) # turtle.circle()函数 rad参数描述圆形轨迹半径的位置 angle参数表示小乌龟沿着圆形爬行的弧度值
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad) # turtle.fd()函数==turtle.forward()函数 表示小乌龟直线爬行，参数rad表示爬行距离
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

if __name__ == '__main__':
    turtle.setup(1300, 800, 0, 0) # 启动一个图形窗口，以左上角为原点，向下为Y，向右为X
    pythonsize = 30
    turtle.pensize(pythonsize) # 设置画笔的粗细
    turtle.pencolor("blue") # 设置画笔颜色
    turtle.seth(-40) # 设置爬行方位，按照0 90 180 360坐标系
    drawSnake(40,80,5,pythonsize/2)