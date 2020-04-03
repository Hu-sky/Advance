模块化设计：紧耦合（模块内部）、松耦合（模块之间）
递归：调用函数自身的方式。链条与基例
PyInstaller安装，cmd命令行条件下： pip install 
 (cmd命令行) pyinstaller -F <文件名.py>
常用参数：
 -h 查看帮助
 --clean  清理打包过程中的临时文件
 -D，--onedir  默认值，生成dist文件夹
 -F，--onefile  在dist文件夹中只生成独立的打包文件
 -i<图标文件名.ico>  指定打包程序使用的图标文件