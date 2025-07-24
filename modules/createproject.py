import os
from PyQt5.Qt import *

class CreateProject(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("创建项目")
        self.resize(1024, 600)

        # 获取脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建资源文件的绝对路径
        logo_path = os.path.join(current_dir, '..', 'resources', 'logo.ico')
        self.setWindowIcon(QIcon(logo_path))

        # 构建样式文件的绝对路径
        qss_path = os.path.join(current_dir, '..', 'styles', 'createproject.qss')
        with open(qss_path, 'r') as f:
            self.setStyleSheet(f.read())

        # 创建主窗口的中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建表单布局
        form_layout = QGridLayout()

        # 第一行：项目名称
        name_label = QLabel("项目名称")
        name_label.setObjectName("formLabel")
        self.name_edit = QLineEdit()
        self.name_edit.setObjectName("formInput")
        form_layout.addWidget(name_label, 0, 0)
        form_layout.addWidget(self.name_edit, 0, 1)

        # 第二行：项目作者
        author_label = QLabel("项目作者")
        author_label.setObjectName("formLabel")
        self.author_edit = QLineEdit()
        self.author_edit.setObjectName("formInput")
        form_layout.addWidget(author_label, 1, 0)
        form_layout.addWidget(self.author_edit, 1, 1)

        # 第三行：项目版本
        version_label = QLabel("项目版本")
        version_label.setObjectName("formLabel")
        self.version_edit = QLineEdit()
        self.version_edit.setObjectName("formInput")
        form_layout.addWidget(version_label, 2, 0)
        form_layout.addWidget(self.version_edit, 2, 1)

        # 第四行：项目叙述
        description_label = QLabel("项目叙述")
        description_label.setObjectName("formLabel")
        self.description_edit = QTextEdit()
        self.description_edit.setObjectName("formInput")
        form_layout.addWidget(description_label, 3, 0)
        form_layout.addWidget(self.description_edit, 3, 1)

        # 第五行：项目是否启用
        enabled_label = QLabel("项目是否启用")
        enabled_label.setObjectName("formLabel")
        self.enabled_combo = QComboBox()
        self.enabled_combo.setObjectName("formInput")
        self.enabled_combo.addItem("启用", True)
        self.enabled_combo.addItem("禁用", False)
        self.enabled_combo.currentIndexChanged.connect(self.update_combo_style)
        form_layout.addWidget(enabled_label, 4, 0)
        form_layout.addWidget(self.enabled_combo, 4, 1)

        # 添加表单布局到主布局
        main_layout.addLayout(form_layout)

        # 创建按钮布局
        button_layout = QHBoxLayout()

        # 创建按钮
        self.create_button = QPushButton("创建")
        self.create_button.setObjectName("createButton")
        self.cancel_button = QPushButton("取消")
        self.cancel_button.setObjectName("cancelButton")

        # 添加按钮到按钮布局
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.cancel_button)

        # 添加按钮布局到主布局
        main_layout.addLayout(button_layout)

        # 为按钮连接槽函数
        self.create_button.clicked.connect(self.create_project)
        self.cancel_button.clicked.connect(self.close)

        # 初始化选择器样式
        self.update_combo_style()

    def update_combo_style(self):
        # 根据选择状态更新样式
        current_index = self.enabled_combo.currentIndex()
        if current_index == 0:  # 启用
            self.enabled_combo.setStyleSheet('''
                #formInput {
                    border: 1px solid #4CAF50;
                    background-color: #E8F5E9;
                }
                #formInput::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 15px;
                    border-left: 1px solid #4CAF50;
                }
            ''')
        elif current_index == 1:  # 禁用
            self.enabled_combo.setStyleSheet('''
                #formInput {
                    border: 1px solid #F44336;
                    background-color: #FFEBEE;
                }
                #formInput::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 15px;
                    border-left: 1px solid #F44336;
                }
            ''')

    def create_project(self):
        # 获取表单数据
        project_name = self.name_edit.text()
        project_author = self.author_edit.text()
        project_version = self.version_edit.text()
        project_description = self.description_edit.toPlainText()
        project_enabled = self.enabled_combo.currentData()

        # 在这里可以添加项目创建的逻辑
        print(f"创建项目: {project_name}")
        print(f"作者: {project_author}")
        print(f"版本: {project_version}")
        print(f"描述: {project_description}")
        print(f"启用状态: {project_enabled}")

        # 关闭窗口
        self.close()