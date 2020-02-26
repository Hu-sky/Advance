# _*_ coding: utf_8 _*_

# 1.惰性序列，不主动遍历，不会计算元素中的值
# 2.map()函数接收两个参数，一个是函数，一个是Iterable
#   list(map(str, [1, 2, 3])) >>> ['1','2','3']
# 3.reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2)x3),x4),必须接受两个参数
# 4.filter()把函数依次作用于元素，根据返回值是True还是False决定是否保留
# 5.删除空字符串def not_empty(s): >>> return s and s.strip()
# 6.filter所需判断函数是一个条件：judge(n)  s[x] == s[len(s)-x-1]
# 7.删选1000以内的回数：filter(judge,range(1000))
# 8.sorted()默认数值大小和ASCII顺序排列
#   sorted(list,key=func,reverse=True)，可接受key函数

