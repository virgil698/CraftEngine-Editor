import os

from PyQt5.Qt import *

from .createproject import CreateProject  # 导入项目创建窗口类
from .conversion import Conversion  # 导入转换器窗口类
from .setting import Setting  # 导入设置窗口类


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("欢迎访问 CraftEngine-Editor")
        self.resize(1920, 1200)

        # 获取脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建资源文件的绝对路径
        logo_path = os.path.join(current_dir, '..', 'resources', 'logo.ico')
        self.setWindowIcon(QIcon(logo_path))

        # 主布局
        main_widget = QWidget()
        self.main_layout = QHBoxLayout(main_widget)  # 定义 main_layout 为实例变量
        self.setCentralWidget(main_widget)

        # 左侧竖状菜单
        self.setup_left_menu(self.main_layout, current_dir)

        # 右侧内容区
        self.right_content = QWidget()  # 定义右侧内容区为实例变量
        self.setup_right_content(self.main_layout, current_dir)

        # 加载样式
        style_path = os.path.join(current_dir, '..', 'styles', 'index.qss')

        with open(style_path, 'r', encoding='utf-8') as f:
            style = f.read()
            self.setStyleSheet(style)

        # 创建项目窗口的引用
        self.create_project_window = None

    def setup_left_menu(self, main_layout, current_dir):
        left_menu = QWidget()
        left_menu.setObjectName("LeftMenu")
        left_menu_layout = QVBoxLayout(left_menu)

        # 构建资源文件的绝对路径
        logo_path = os.path.join(current_dir, '..', 'resources', 'logo.ico')
        projects_button_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'suitcase-solid-full.svg')
        converter_button_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'gears-solid-full.svg')
        settings_button_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'gear-solid-full.svg')

        # 左侧图标 + 右侧程序信息
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)

        # Logo
        logo_label = QLabel()
        logo_label.setPixmap(QPixmap(logo_path).scaled(48, 48, Qt.KeepAspectRatio))
        logo_label.setAlignment(Qt.AlignCenter)

        # 程序信息（垂直布局）
        info_layout = QVBoxLayout()
        program_name = QLabel("CraftEngine-Editor")
        program_name.setFont(QFont("Arial", 14, QFont.Bold))
        program_name.setObjectName("ProgramName")

        version_label = QLabel("v0.0.1")
        version_label.setFont(QFont("Arial", 10))
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setObjectName("VersionLabel")

        info_layout.addWidget(program_name)
        info_layout.addWidget(version_label)

        header_layout.addWidget(logo_label)
        header_layout.addLayout(info_layout)

        # 项目按钮
        projects_button = QPushButton()
        projects_button.setIcon(QIcon(projects_button_icon_path))
        projects_button.setIconSize(QSize(24, 24))
        projects_button.setText("项目")
        projects_button.setObjectName("ProjectsButton")
        projects_button.clicked.connect(lambda: self.switch_right_content("projects"))

        # 转换按钮
        converter_button = QPushButton()
        converter_button.setIcon(QIcon(converter_button_icon_path))
        converter_button.setIconSize(QSize(24, 24))
        converter_button.setText("转换")
        converter_button.setObjectName("ConverterButton")
        converter_button.clicked.connect(lambda: self.switch_right_content("converter"))

        # 设置按钮
        settings_button = QPushButton()
        settings_button.setIcon(QIcon(settings_button_icon_path))
        settings_button.setIconSize(QSize(24, 24))
        settings_button.setText("设置")
        settings_button.setObjectName("SettingsButton")
        settings_button.clicked.connect(lambda: self.switch_right_content("settings"))

        left_menu_layout.addWidget(header_widget)
        left_menu_layout.addWidget(projects_button)
        left_menu_layout.addWidget(converter_button)
        left_menu_layout.addWidget(settings_button)
        left_menu_layout.addStretch()

        main_layout.addWidget(left_menu, 1)

    def setup_right_content(self, main_layout, current_dir):
        self.right_content.setObjectName("RightContent")
        right_content_layout = QVBoxLayout(self.right_content)

        # 搜索按钮和操作栏
        control_bar = QWidget()
        control_bar_layout = QHBoxLayout(control_bar)

        search_bar = QWidget()
        search_layout = QHBoxLayout(search_bar)

        # 构建资源文件的绝对路径
        search_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'magnifying-glass-solid-full.svg')

        search_icon = QLabel()
        search_icon.setPixmap(QPixmap(search_icon_path).scaled(24, 24, Qt.KeepAspectRatio))

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("搜索...")
        search_edit.setObjectName("SearchEdit")

        search_layout.addWidget(search_icon)
        search_layout.addWidget(search_edit)

        # 操作按钮
        buttons_bar = QWidget()
        buttons_layout = QHBoxLayout(buttons_bar)

        new_project_button = QPushButton("新建项目")
        new_project_button.setObjectName("NewProjectButton")
        new_project_button.clicked.connect(self.open_create_project_window)

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

        main_layout.addWidget(self.right_content, 3)

    def switch_right_content(self, content_type):
        """
        切换右侧内容
        :param content_type: 内容类型，"projects"、"converter" 或 "settings"
        """
        # 清空右侧布局
        if self.main_layout.count() > 1:  # 检查是否有右侧内容
            self.main_layout.itemAt(1).widget().deleteLater()

        if content_type == "projects":
            # 创建项目内容
            self.right_content = QWidget()
            self.right_content.setObjectName("RightContent")
            right_content_layout = QVBoxLayout(self.right_content)

            # 搜索按钮和操作栏
            control_bar = QWidget()
            control_bar_layout = QHBoxLayout(control_bar)

            search_bar = QWidget()
            search_layout = QHBoxLayout(search_bar)

            # 构建资源文件的绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            search_icon_path = os.path.join(current_dir, '..', 'resources', 'svg', 'magnifying-glass-solid-full.svg')

            search_icon = QLabel()
            search_icon.setPixmap(QPixmap(search_icon_path).scaled(24, 24, Qt.KeepAspectRatio))

            search_edit = QLineEdit()
            search_edit.setPlaceholderText("搜索...")
            search_edit.setObjectName("SearchEdit")

            search_layout.addWidget(search_icon)
            search_layout.addWidget(search_edit)

            # 操作按钮
            buttons_bar = QWidget()
            buttons_layout = QHBoxLayout(buttons_bar)

            new_project_button = QPushButton("新建项目")
            new_project_button.setObjectName("NewProjectButton")
            new_project_button.clicked.connect(self.open_create_project_window)

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

            self.main_layout.addWidget(self.right_content, 3)

        elif content_type == "converter":
            # 加载转换页面样式
            style_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'styles', 'conversion.qss')
            with open(style_path, 'r', encoding='utf-8') as f:
                style = f.read()

            # 创建转换内容
            self.right_content = Conversion()
            self.right_content.setObjectName("ConversionWidget")
            self.right_content.setStyleSheet(style)
            self.main_layout.addWidget(self.right_content, 3)

        elif content_type == "settings":
            # 加载设置页面样式
            style_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'styles', 'setting.qss')
            with open(style_path, 'r', encoding='utf-8') as f:
                style = f.read()

            # 创建设置内容
            self.right_content = Setting()
            self.right_content.setObjectName("SettingWidget")
            self.right_content.setStyleSheet(style)
            self.main_layout.addWidget(self.right_content, 3)

    def open_create_project_window(self):
        """
        打开创建项目窗口
        """
        if not self.create_project_window or not self.create_project_window.isVisible():
            self.create_project_window = CreateProject()
            self.create_project_window.resize(1024, 600)
        self.create_project_window.show()