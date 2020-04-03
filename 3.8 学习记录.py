# 1.一对三引号可表示多行字符串，当没被使用时，可当作注释使用
# 2.'0123456789'[::-1] >>> '987654321'
# 3.字符串操作符：
#   x+y：连接两个字符串x和y
#   n*x或x*n：复制n此字符串x
#   x in s：如果x是s的子串，返回True，否则返回False
# 4.hex(x)/oct(x):将整数x的十六进制或八进制小写形式字符串，hex(425)>>>'0x1a9'
# 5.chr(u)<=>ord(x):unicode编码与对应字符x相互转换
# 6.八个常用的字符串处理方法.一定以.的形式使用
#   str.lower()或str.upper()
#   str.split(sep=None)
#   str.count(sub),计数
#   str.replace(),替换，'python'.replace('n','n123.io')
#   str.center(width[,fillchar]):'python'.center(20,'=')>>> ===python===
#   str.strip(chars):去掉z左右chars中列出的字符；'= python= '.strip(' =np')
#   str.join(iter):在除最后元素外，增加，主要用于分隔：','.join('12345')
# 7.槽-{}表示，占位信息，{2}可指定对应format参数
#   槽内部配置{<参序><引导符号:><填充><对齐><宽度> <,><.精度><类型>}
#   整数类型：b二进制，cunicode，d十进制，o八进制，x/X十六进制
#   浮点数类型：e/E科学计数法，f普通，%百分数形式
# 8.time库包括三类函数：
#   时间获取：time() ctime() gmtime()
#   时间格式化：strftime() strptime()
#   程序计时：sleep() perf_counter()
# 9.\r是刷新的关键