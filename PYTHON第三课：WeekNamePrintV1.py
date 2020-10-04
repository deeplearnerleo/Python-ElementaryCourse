#字符串
#字符串操作及表示
#字符串的表示
#有序序列，可索引
#单引号，双引号，三单引号，三双引号

#如果在文本中想要使用双引号表示字符串，
'这里有个双引号(")'  "这里有个单引号(')"
#或又出现单引号，又出现双引号
'''这里既有单引号(')又有双引号(")'''

 #切片[M:N:K]  [::-1]逆序
 #转义符\   (\")"
#字符串操作符
#x+y   n*x    x in s

#x in s的例子
#WeekNamePrinrV1
'''
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字（1-7）："))
pos = (weekId-1)*3
print(weekStr[pos:pos+3])
'''

'''
weekStr = "星期一星期二星期一星期一星期一星期一星期一"
weekId = input("输入数字1-7：")
pos = (eval(weekId)-1)*3
print(weekStr[pos:pos+3])
'''


