# _*_ coding: utf-8 _*_

# 1.给实例绑定方法：def set_age(self, age): # 定义一个函数作为实例方法
#                       self.age = age
#                  from types import MethodType
#                  s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
#                  s.set_age(25) # 调用实例方法
#                  s.age # 测试结果 >>> 25
# 2.给一个实例绑定的方法，对另一个实例不起作用
# 3.可以给class绑定方法，以给所有的实例调用
# 4.__slots__变量，来限制该class实例能添加的属性，对继承的子类不起作用
#   如子类也定义__slots__，子类实例允许定义的属性就是自身的加上父类的
# 5.@property广泛应用在类的定义中，以用简短的代码做出必要的检查
#   加上@property，把getter方法变成属性，同时创建_装饰器@score.setter





