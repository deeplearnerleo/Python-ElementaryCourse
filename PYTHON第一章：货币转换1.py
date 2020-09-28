CurStr = input()

if CurStr[0:3] == 'RMB':
    USD = eval(CurStr[3:])/6.78
    print('USD{:.2f}'.format(USD))
elif CurStr[0:3] == 'USD':
    RMB = 6.78*eval(CurStr[3:])
    print('RMB{:.2f}'.format(RMB))
else:
    print()
    
    
#第二种表示方法
'''
CurStr = input()
if CurStr[:3] == 'RMB':
    print('USD{:.2f}'.format(eval(CurStr[3:])/6.78))
elif CurStr[0:3] == 'USD':
    print('RMB{:.2f}'.format(6.78*eval(CurStr[3:])))
else:
    print()
    
