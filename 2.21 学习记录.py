# _*_ coding: utf-8 _*_

# 1."abc.py"实际就是一个模块modul，未免重名，先import abc
# 2.任何模块代码的第一个字符串都被视为模块的文档注释
# 3.当在命令行运行hello模块文件时，Python解释器把特殊变量__name__置为__main__
# 4.__name__有2个取值，直接执行时：__name__=='__main__'
#   当被调用时：__name__取值是模块的名字
# 5.面向对象的设计思想是抽象出Class，根据Class创建Instance
#   面向对象的抽象程度比函数要高，因为Class既包含数据，又包含操作数据的方法
# 6.类Class是抽象的模板，比如Student类；实例Instance是根据类创建的具体的“对象”
#   每个对象都拥有相同的方法，但各自的数据可能不同
# 7.class定义类，接类名，通常以大写开头紧接着是(object)：class Student(object)
#   创建实例通过类名+()实现： Bart = Student()
#   可以自由地给一个实例变量绑定属性：bart.name='Bart Simpson'
# 8.给对象发消息就是调用对象对应的关联函数，称为对象的方法（Method）
# 9.绑定必须参数：__init__方法的第一个参数永远是self，表示创建的实例本身
#   在内部，可以把各种属性绑定到self，因为self就指向创建的实例本身
