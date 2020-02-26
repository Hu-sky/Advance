# _*_ coding: utf- 8 _*_

# 1.__str__()：定义类的字符串：
#   def __str__(self):  return 'Student object (name: %s)' % self.name
# 2.__repr__()：通常代码与__str__一样：__repr__ = __str__
# 3.__iter__实现class类似list的循环，应返回自己
#   __next__计算下一个值
# 4.__getitem__()通过自己定义，可以表现的和自带的list\tuple\dict无区别
# 5.解释器会试图__getattr__来获得不存在的属性，也可以返回函数
#   __getattr__默认返回是None
# 6.__call__()调用，
# 待补充：没能懂得API和SDK的基本规则，看不懂本章答疑后面的作用在哪

class Student(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('My name is %s.' %self.name)
