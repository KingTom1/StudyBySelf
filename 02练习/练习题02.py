
#删除列表中的重复元素
l=[1,1,6,3,1,5,2]
def duplictae(lists):
    L=[]
    for i in lists:
        if i not in L:
            L.append(i)
    return L
print(duplictae(l))
#实现字符串反转 输入str="string"输出'gnirts'
tt='string';
i=0;
result='';
while i<6:
    result=str(tt)[i]+result;
    i+=1;
print(result)