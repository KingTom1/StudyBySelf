# pyhton大小写敏感
# 程序编写模板 IPO思想  input函数获取用户输入I， 处理P ， print输出O
# 绘制小蟒蛇程序
import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

if __name__ == '__main__':
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)
