import os

from PyQt5.Qt import *

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("转换器")
        self.resize(1024, 600)

        # 获取脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建资源文件的绝对路径
        logo_path = os.path.join(current_dir, '..', 'resources', 'logo.ico')
        self.setWindowIcon(QIcon(logo_path))