# _*_ coding: utf-8 _*_

# 1.函数可作为返回值，内部函数可以引用外部函数的参数和局部变量
#   每次调用外部函数f=lazy_sum,都会返回新的函数，相互不影响，f1!=f2
# 2. 返回闭包牢记：返回函数不要引用任何循环变量，或者后续会发生变化的变量
#   在返回父函数前，子函数的自由变量...pass
# 3.匿名函数lambda x: x表示函数参数，只能有一个表达式，可被调用
#   list(filter(lambda x:x % 2 == 1, range(1, 20))) >>> [1,3,5...]
# 4.Decorator装饰器：在代码运行期间动态增加功能的方式，而不改变原函数
#   理解装饰器https://www.jianshu.com/p/ee82b941772a
#   https://www.runoob.com/w3cnote/python-func-decorators.html(关注)
# 5.函数后的括号：把一对小括号放在后面，这个函数就会执行
# 6.def int2(x, base=2):  return int(x, base)
#   偏函数：int2=functools.partial(int,base=2),即设置默认参数

#补充：
# +1.定义在函数内部的子函数，不能在外部调用
# +2.fn=decorater(fn) fn() >>> 装饰器调用的是函数，不是函数值
# +3.from functools import wraps  @wraps修改名字和注释文档


