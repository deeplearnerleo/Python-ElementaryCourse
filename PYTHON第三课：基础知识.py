#字符串处理函数
#len(x)  返回字符串长度  len("123四五六")=6
#str(x)   将任意类型的x变成对应的字符串形式 str(1.23)="1.23"   str([1,2])="[1,2]"
#str()  与  eval()功能相反
#hex(x) oct(x) 将整数x的十六进制或八进制小写形式字符串
#方法<a>.<b>中的<b>为方法，<a>为面向对象
#8个方法
#str.lower()  str.upper()  返回字符串的副本，全部字符为大写/小写
#str.split(sep=None)   返回一个列表，由str根据sep被分隔的部分组成 "A,B,C".split(",")结果为['A','B','C']
#str.count(sub) #返回sub在str中出现的次数  "an apple a day".count("a")结果为4
#str.replace(old,new)  返回字符串str副本，所有old字串被替换为new
#str.center(width[,fillchar]) 字符串str根据宽度width居中，fillchar可选  "python".center(12,"+")结果为+++python+++
#str.strip(chars) 从str中去掉其左侧和右侧chars中列出的字符  "= python=".strip(" =np")结果为"ytho"
#str.join(iter) 在iter变量除最后元素外每个元素后增加一个str  ",".join("12345")结果为"1,2,3,4,5" #主要用于字符串分隔等



#字符串格式化
#使用.format()的方法,如下：
#<模板字符串>.format(<逗号分隔的参数>)
#一个概念：槽其只在字符串中有用  用{}.format()表示
#"{1}:计算机{0}的CPU占用率为{2}%".format("2020-10-4","C",10)

