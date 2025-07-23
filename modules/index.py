import os

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("欢迎访问 CraftEngine-Editor")
        self.resize(1280, 800)

        # 获取脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建资源文件的绝对路径
        logo_path = os.path.join(current_dir, '..', 'resources', 'logo.ico')
        self.setWindowIcon(QIcon(logo_path))

        # 主布局
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        # 左侧竖状菜单
        self.setup_left_menu(main_layout, current_dir)

        # 右侧内容区
        self.setup_right_content(main_layout, current_dir)

        # 加载样式
        style_path = os.path.join(current_dir, '..', 'styles', 'index.qss')

        with open(style_path, 'r', encoding='utf-8') as f:
            style = f.read()
            self.setStyleSheet(style)

    def setup_left_menu(self, main_layout, current_dir):
        left_menu = QWidget()
        left_menu.setObjectName("LeftMenu")
        left_menu_layout = QVBoxLayout(left_menu)

        # 构建资源文件的绝对路径
        logo_path = os.path.join(current_dir, '..', 'resources', 'logo.ico')
        projects_button_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'suitcase-solid-full.svg')
        converter_button_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'gears-solid-full.svg') # 新增图标路径

        # Logo + 程序名 + 版本号
        logo_label = QLabel()
        logo_label.setPixmap(QPixmap(logo_path).scaled(48, 48, Qt.KeepAspectRatio))
        logo_label.setAlignment(Qt.AlignCenter)

        program_name = QLabel("CraftEngine-Editor")
        program_name.setFont(QFont("Arial", 14, QFont.Bold))
        program_name.setAlignment(Qt.AlignCenter)

        version_label = QLabel("v0.0.1")
        version_label.setFont(QFont("Arial", 10))
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setObjectName("VersionLabel")

        # 项目按钮
        projects_button = QPushButton()
        projects_button.setIcon(QIcon(projects_button_icon_path))
        projects_button.setIconSize(QSize(24, 24))
        projects_button.setText("项目")
        projects_button.setObjectName("ProjectsButton")

        # 转换器按钮（新增）
        converter_button = QPushButton()
        converter_button.setIcon(QIcon(converter_button_icon_path))
        converter_button.setIconSize(QSize(24, 24))
        converter_button.setText("转换")
        converter_button.setObjectName("ConverterButton") # 新增标识符

        left_menu_layout.addWidget(logo_label)
        left_menu_layout.addWidget(program_name)
        left_menu_layout.addWidget(version_label)
        left_menu_layout.addWidget(projects_button)
        left_menu_layout.addWidget(converter_button) # 新增按钮
        left_menu_layout.addStretch()

        main_layout.addWidget(left_menu, 1)

    def setup_right_content(self, main_layout, current_dir):
        right_content = QWidget()
        right_content.setObjectName("RightContent")
        right_content_layout = QVBoxLayout(right_content)

        # 搜索框功能和操作栏
        control_bar = QWidget()
        control_bar_layout = QHBoxLayout(control_bar)

        # 搜索
        search_bar = QWidget()
        search_layout = QHBoxLayout(search_bar)

        # 构建资源文件的绝对路径
        search_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'magnifying-glass-solid-full.svg')

        search_icon = QLabel()
        search_icon.setPixmap(QPixmap(search_icon_path).scaled(24, 24, Qt.KeepAspectRatio))

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("搜索项目...")
        search_edit.setObjectName("SearchEdit")

        search_layout.addWidget(search_icon)
        search_layout.addWidget(search_edit)

        # 操作按钮
        buttons_bar = QWidget()
        buttons_layout = QHBoxLayout(buttons_bar)

        new_project_button = QPushButton("新建项目")
        new_project_button.setObjectName("NewProjectButton")

        open_project_button = QPushButton("打开")
        open_project_button.setObjectName("OpenProjectButton")

        buttons_layout.addWidget(new_project_button)
        buttons_layout.addWidget(open_project_button)

        control_bar_layout.addWidget(search_bar)
        control_bar_layout.addWidget(buttons_bar)

        # 项目记录列表
        projects_list = QListWidget()
        projects_list.setObjectName("ProjectsList")

        # 添加示例项目
        projects = ["项目1 (最近使用)", "项目2", "项目3"]
        for project in projects:
            item = QListWidgetItem(project)
            projects_list.addItem(item)

        right_content_layout.addWidget(control_bar)
        right_content_layout.addWidget(projects_list)

        main_layout.addWidget(right_content, 3)