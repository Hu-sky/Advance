# _*_ coding:utf-8 _*_

# 1.定义可变个数参数加*, def calc(*numbers)
#   如已有list或tuple，nums=[1,2,3],可直接加*带入：calc(*nums)
# 2.使用关键字参数可以接收更多参数：def person(name,age,**kw)
#   限制关键字参数名字：def person(name,age,*,city,job)
#   如已有可变参数：def person(name,age,*args,city,job)
#   命名关键字参数可以有缺省值：def person(name,age,*,city='baijing',...)
# 3.参数组合顺序：必选-默认c=0-可变*-命名关键字*,-关键字**
# 4.函数可通过tuple和dict调用，依次塞入，这点没懂！！！
#   对于任意函数，都可以通过类似func(*args,**kw)的形式调用它
# 5.递归函数逻辑清晰，但过深的调用会导致栈溢出；
#   计算n！：def fact(n)：if n=1...return fact(n)=n*fact(n-1)
#   尾递归可减少栈的调用，但一般语言都没有优化 return fx(num-1,2*product+1)
# 6.汉诺塔递归问题,参数只限于当前层调用，各层有各层的参数



