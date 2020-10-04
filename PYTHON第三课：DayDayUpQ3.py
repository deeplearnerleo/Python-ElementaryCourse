#DayDayUpQ3.py

#一周内5天进步，两天退步
#首先定义初始条件，基础分1分，进步和退步都是1%，如果工作日就进步，休息日就退步
#则一年共进步多少？


dayup = 1.0
dayfactor = 0.01

for i in range(365):
    if i % 7 in[0]:
        dayup = dayup

        #dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
    
print("工作日的力量:{:.2f}".format(dayup))
