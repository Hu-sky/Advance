# 1.多进程同一个变量，各有拷贝互不影响，多线程所有变量都由所有共享，易改乱
# 2.threading模块：t = threading.Thread(target=loop, name='LoopThread')
#   默认name Thread-1，Thread-2……
# 3.threading.current_thread()返回当前线程实例
# 4.lock=threading.Lock() 获取锁：lock.acquire()
#   用try...finally...语句保证锁能释放：lock.release()
# 5.ThreadLocal是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰
#   local_school = threading.local()