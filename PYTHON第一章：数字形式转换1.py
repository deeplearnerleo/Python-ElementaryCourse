template = "零一二三四五六七八九"

s = input()
for c in s:
    print(template[eval(c)],end="")

    
'''
end=""  print()中增加end=""参数表示输出后不增加换行，
多个print()可以连续输出
'''
#问题1，template[]为什么可以表示为汉字字符串
#问题2，template[]的汉字顺序是怎么确定的
#问题3，for循环在后续讲解需要注意
