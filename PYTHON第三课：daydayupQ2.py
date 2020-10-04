#DayDayUpQ2.py

deyfactor =0.019
dayup = 1
daydown = 1
for i in range(365):
    dayup = dayup*(1+deyfactor)
    daydown = daydown*(1-deyfactor)
#dayup = pow(1+deyfactor,365)
#daydown = pow(1-deyfactor,365)
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))
