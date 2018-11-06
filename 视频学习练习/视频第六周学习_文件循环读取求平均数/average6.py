# # 读取文件，求平均数实例
# def main():
#     fileaName = input("what file are the numbers in>")
#     infile = open(fileaName,'r')
#     print(infile)
#     sum = 0.0
#     count = 0
#     line  = infile.readline()
#     while line != "":
#         sum = sum+eval(line)
#         count = count + 1
#         line = infile.readline()
#     print("\nThe average of the numbers is", sum/count)
#
# main()

# 循环嵌套
'''决策和循环相互嵌套可以实现复杂算法
之前实例中文件每行只存一个数字，这一次数字以逗号分隔出现在文件的同一行上。'''
def main():
    fileName = input("what file are the number in?")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum/ count)

if __name__ == '__main__':
    main()