'''
#温度转换
TempStr = input('请输入带有符号的温度：')
if TempStr[-1] in ['f','F']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print('转换后的温度输出是：{:.2f}C'.format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print('转换后的温度是：{:.2f}F'.format(F))
else:
    print('输入格式错误')
'''

#TempStr

TempStr = input()
if TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print('温度:{:.2f}F'.format(F))
elif TempStr[-1]in ['F','f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print('温度:{:.2f}C'.format(C))
else:
    print('输入格式错误')
