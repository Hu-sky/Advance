# 1.collections是Python内建的集合模块
# 2.namedtuple是一个函数，可以用来创建一个tuple对象，且可以属性访问：
#   Point=namedtuple('Point',['x','y']) >>> p.x/p.y存在
# 3.deque是为实现插入和删除的双向操作，适用于队列和栈
#   q=deque([list]): q.appendleft('element')/q.popleft()
# 4.defaultdict支持key不存在时返回默认值，而不是报错
#   dd=defaultdict(lambda:"N/A")，默认值由函数调用，其它行为与dict一致
# 5.OrderedDict可以保持key的顺序，（dict的key是无序的）
#   od=OrderedDict([(key1,valuea),(key2,value2),...])>>>OrderedDict(...)
#   利用OederedDict可实现先进先出(FIFO)
# 6.Counter计数器,可以统计字符个数：c=Counter()
#   for ch in 'string': c[ch]=c[ch]+1 print(c)
# 7.ChainMap此处没有学懂