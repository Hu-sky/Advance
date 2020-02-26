# _*_ coding:utf-8 _*_

# 1.切片list[0:3]，索引0，1，2，不包括3
#   第一个索引是0，可省略：list[:3]
#   支持倒数切片：list[-2:-1]，不包括-1(倒数第一个元素)
#   前10，每2取1：list[:10:2]
#   所有数，每5取1：list[::5]
#   list[:]原样复制一个list
# 2.tuple支持切片：(1,2,3,4,5)[:3] >>> (0,1,2)
#   字符串支持切片：'ABCDEFG'[::2] >>> 'ACEG'
# 3.迭代：使用for in遍历list\tuple\str等
#   dict默认迭代key
#   如要迭代value，可用for value in d.values()
#   如要同时迭代key和value，可用 for k,v in d.items()
#   字符串也可迭代： for ch in 'ABC' >>> A B C
#   isinstance(123,Iterable) >>> 整数不可迭代
#   把list变成索引-元素对： for i,value in enumerate(['a','b','c'])
#   for可同时引用两个变量：for x,y in [(1,1),(2,4),(3,,9)]
# 4.列表生成式[x*x for x in range(1,11)] >>> [1,4,9,16...]
#   添加条件判断：[x*x for in range(100) if x%2==0] >>> [4,16,36...]
#   两层全排列[m+n for in 'ABC' for n in 'XYZ'] >>> ['AX','AY'...]
#   使用两个变量生成list：[k+'='+v for k,v in d.items()]
# 5.list改小写：[s.lower() for s in L]
# 6.for前面的if ... else是表达式，而for后面的if是过滤条件，不能else
# 7.生成器generator：一边循环，一边完善
#   有两种生成方法，g=(x*x for x in range(10))
#   第二种：yield 改函数为genderator
# 8.L=[1] L1=[0]+L >>> [0,1]
# 9.可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#   list、dict、str不是Iterator(长度不可知)
#   isinstance(iter([]),Iterator)，可用iter()变成Iterator


