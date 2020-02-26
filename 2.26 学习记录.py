 # _*_ coding: utf-8 _*_

# 1.try...except...finally...的错误处理机制
# 2.logging模块可以记录错误信息，同时让程序执行下去
#   通过配置，还可以把错误记录到日志文件里，方便事后排查
#   except Exception as e:  logging.exception(e)
# 3.raise 抛出错误，尽量使用Python自定错误类型
# 4.try: return int(s)   except: return float(s)
# 5.调试：(1)print可能出错的变量
#      (2)断言assert：assert n != 0, 'n is zero!' "-O" 欧
#      (3)logging：允许指定记录信息级别：debug info warning error
#         logging.basicConfig(level=logging.INFO)
#      (4)调试器pdb：让程序以单步方式运行 命令窗口python -m pdb err.py
#         n执行单步命令   p+变量名 查看变量   q结束调试
#      (5)import pdb  在可能出错的地方放一个pdb.set_trace()断点
#         运行到断点会暂停，p+变量名 查看变量   c继续运行
# 6.编写单元测试类从unittest.TestCase继承，测试方法以test开头
# 7.断言assertEqual
# 8.文档测试 import doctest  /n  doctest.testmod()