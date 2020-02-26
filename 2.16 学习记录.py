# _*_ coding: utf-8 _*_

# 1.break可以提前退出循环；continue可以跳过本轮循环
# 2.dict={key1:value1,key2:value2,...},key必须不可变！
#   dict类似部首查字法，量大时速度快但内存大；list相反
#   dict[key1] = valuex，后面的赋值会替代前面的
#   判断key是否存在1：print(key in dict) >>> True/False
#   dict.get(key) >>> value/None
#   当key不存在，还可返回指定的值：dict.get(key0,-1) >>> -1
#   添加：直接赋值给dict的key：dict[key+]=value+
#   删除：dict.pop(key)删除key和对应的value
# 3.set可看作无序与无重复元素的集合，可交&可并|
#   创建以list作为输入集合：s=set([key1,key2,...])={key1,key2,...}
#   原理与dict一致，区别在于set没有value
#   添加：s.add(key+)，可重复添加，但不会有效果
#   删除：s.remove(key)
# 4.['c','b','a'].sort() >>> ['a','b','c']
#   'abc'.replace('a','A') >>> 'Abc'
# 5.不可变对象(1,2,3)可作为key放入dict和set中，(1,[,3])不可
# 6.数字转字符的一种发法format(16,'#b') >>> 10000
#   判断变量类型：type(format(10,'#x')) >>> <class 'str'>
# 7.def...return，return默认返回None
#   定义pass，可作为占位符，缺少占位符会有语法错误
#   Python的函数返回多值其实就是返回一个tuple，但写起来更方便
# 8.默认参数降低了函数调用的难度
#   定义默认参数须指向不变对象（add_end(l=[])）是个坑


