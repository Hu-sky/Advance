# _*_ coding :utf-8 _*_
# 1.从外部(磁盘、网络)=>内存 input；反之output
# 2.Stream数据只能单向流动
# 3.读文件f=open('/path/to/file','r') print(f.read())
# 4.使用try...finally保证在出错的情况下f.close()也会被调用
#   with open('file','r') as f: print(f.read()) 不用close
# 5.反复调用read(size)，可以每次只读取size字节
#   readlines()一次读取所有内容并返回list
# 6.读取二进制文件(图片/视频...) f=open('.jpg','rb')
# 7.读取非utf-8编码文本，需要传入encoding参数，可选忽略错误：
#   f=open('file.txt','r',encding='gbk',errors='ignore')
# 8.写文件同读文件，改'r' 为'w’写/'a'追加 write() 换行\n
# 9.from io import StringIO/BytesIO 字符串和二进制数据，读写不可同时进行
#   strip()可以删去末尾\n
#10.Bytes写入的不是字符，而是经过utf-8编码的bytes
#   f.write('中文'.encode('utf-8'))
#11.在python内调用操作系统接口函数：import os
#   环境变量 os.environ >>> ...   
#12.查看当前目录绝对路径：os.path.abspath('.')
#   创建新目录先表示完整路径：os.path.join('d:\\vs code','new'),
#   然后创建目录：os.mkdir('d:\\vs code\\new')
#   删除目录：os.redir('d:\\vs code\\new')
#   os.path.join()合并两个路径可以正确处理不同操作系统的分隔符/\
#   路径拆分：os.path.split(''D:\\Huang\\Desktop\\VS Code\\)
#   获得扩展名 os.path.splitext('/path.txt') >>> ('/path', '.txt')
#   重命名：os.rename('tst.png','tst.jpg')
#   删除文件：os.remove('tst.jpg')
#13.列出当前目录：[x for x in os.listdir('.') if os.path.isdir(x)]
#   列出.py：[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']