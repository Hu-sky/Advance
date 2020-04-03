#_*_ coding: utf-8 _*_

# 1.枚举类型:可看作一系列常量的集合,通常用于表示某些特定的有限集合，如星期
#   枚举类型不可实例化，不可更改
#   定义枚举，成员名不可重复，成员值可相同，第二成员名被视作第一个成员的别名
#   在通过取值获取枚举成员时，只获取第一成员， print(Color(1)) >>> Color.red
# 2.枚举取值：成员名 print(Color['red']) >>> Color.red
#   成员值 print(Color(1)) >>> Color.red
# 3.每个成员都有名称属性和值属性：print(Color.red.name/value) >>> red/1
# 4.支持遍历成员，但重复值只获取第一成员：for color in Color
# 5. __members__ 是一个将名称映射到成员的有序字典,
#   for color in Color.__members__.items():
#   详细链接：https://segmentfault.com/a/1190000017327003
# 6.type()创建新的类型：Hello = type('Hello', (object,), dict(hello=fn))
#   type()传入的参数依次为class的名称
#   继承的父类集合，如果只有一个父类，请注意tuple单元素的写法
#   class的方法名称与函数绑定
# 7.metaclass，元类：命名一般以Metaclass结尾
#   def __new__(cls,name,bases,attrs):接受的参数依次是：
#      (1)当前准备创建的类的对象
#      (2)类的名字
#      (3)类继承的父类集合
#      (4)类的方法集合
