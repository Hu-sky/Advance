# 1.pickle模块实现序列化，只适用于python
# 2.pickle.dumps()方法把任意对象序列化成bytes >>> b'\x80\x03}...'
#   Method 2：f=open('dump.txt,'wb') / pickle.dump(d,f) / f.close
# 3.反序列化：pickle.loads()
#   Method 2：f=open('dump.txt,'rb') / pickle.load(f)
# 4.JSON标准格式 import json
# 5.序列化：dumps() 返回str， dump('...',file)把json写入一个file-like Object
#   反序列化：loads() ； load()
# 6.可选参数default把任意对象变成可序列为JSON的对象，需写转换函数
#   把class的实例变为dict lambda obj:obj.__dict__
#   反序列化：loads()先转换成dict对象，然后object_hook负责将dict转换为类实例
#     定义反转函数def d2s(d):/ return Student(d['name',d['age'],...])
#     json.loads(json_str,object_hook=d2s)
# 7.json.dumps(obj,ensure_ascii=False) >>> {"name": "\u5c0f\u660e", ...}
#   ensure_ascii默认是True，这时会把中文转化成unicode  \u5c0f\u660e

# 8.Mac&Linux提供了fork调用，multiprocessing是跨平台版本多进程模块
# from multiprocessing import Process
# import os
# def run_proc(name):  # 子进程要执行的代码
#     print('Run child process %s (%s)...' % (name, os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))  # 创建Process实例
#     print('Child process will start.')
#     p.start()  # 启动子进程
#     p.join()  # 等待子进程结束后继续往下运行，常用于进程间同步
#     print('Child process end.')
# 9.Pool默认大小是CPU核数，p.apply_async(long_time_task, args=(i,))
#   p.close()后不能再添加新的Process