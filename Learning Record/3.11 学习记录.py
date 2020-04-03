# 1.for...in遍历循环；while无限循环
# 2.二分支紧凑形式：<表达式1> if <条件> else <表达式2> （只支持表达式，非赋值）
#   print('猜{}了'.format('对' if guess==99 else '错'))
# 3.try:执行语句 except <预定义异常类型>: 只抛出异常类型的错误
#   高级模式：try...except...else...finally  不出错则奖励执行else语句
# 4.break跳出并结束当前整个循环，执行循环后的语句
#   continue结束当次循环，继续执行后续次数循环
# 5.循环与else，当循环没有被break退出，则执行else奖励语句
# 6.伪随机数：采用梅森旋转数列生成的（伪）随机数列
#   随机数种子 -> 梅森旋转算法 -> （确定的）随机序列
# 7.random库，基本函数-2个
#   seed(a=None) >>>random.seed(10),初始化随机数种子，默认为第一次系统时间
#   random() 生成一个[0.0,1.0)之间的随机小数 2个不包含，+randrange
# 8.random库，扩展函数-常用6个
#   randint(a,b) 生成一个[a,b]之间的整数
#     random.randint(10,100) >>> 64
#   uniform(a,b) 生成一个[a,b]之间的随机小数
#     random.uniform(10,100) >>> 13.096321648808136
#   getrandbits(k) 生成一个k比特长的随机整数
#     random.getrandbits(16) >>> 37885
#   randrange(m,n[,k]) 生成一个[m,n)之间以k为步长的随机数整数
#     random.randrange(10,100,10) >>> 80
#   getrandbits(k) 生成一个k比特长的随机整数
#     random.getrandbits(16) >>> 37885
#   choice(seq) 从序列seq中随机选择一个元素
#     random.choice([1,2,3,4...]) >>> 3
#   shuffle(seq) 将序列seq中元素随机排列，返回打乱后的序列,名称仍是seq
#     random.shuffle([1,2,3,4...]) >>> [3,5,8,9...]