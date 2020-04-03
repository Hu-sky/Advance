# _*_ coding: utf-8 _*_

# 1.要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__私有变量
#   self.__name，解释器会把__name变量添加其它前缀，导致变量错误
# 2.继承：子类会继承父类(超类/基类)的方法
# 3.当我们定义一个class的时候，我们实际上就定义了一种数据类型
#   c = Dog() # c是Dog类型，isinstance(c,Dog)、isinstance(c,Animal)>>> True
# 4.多态：让具有不同功能的函数可以使用相同的函数名
# 5.type判断对象/函数/类的类型
#   使用types模块可以判断一个对象是否是函数type(fn)==types.FunctionType
#   判断一个变量是否是某些类型中的一种isinstance([1, 2, 3],(list, tuple))
# 6.getattr()、setattr()以及hasattr()
#   hasattr(obj, 'x') # 有属性'x'吗？ hasattr(obj,'power')也可以获得对象
#   setattr(obj, 'y', 19) # 设置一个属性'y'
#   getattr(obj, 'y') # 获取属性'y'
#   getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 7.每创建一个实例对象就会执行一次__init__方法


