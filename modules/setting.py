from PyQt5.Qt import *

class Setting(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("SettingWidget")
        layout = QVBoxLayout(self)

        # 第一行：语言选择
        language_row = QHBoxLayout()
        language_label = QLabel("语言 Language:")
        language_label.setObjectName("LanguageLabel")
        language_row.addWidget(language_label)

        self.language_combo = QComboBox()
        self.language_combo.setObjectName("LanguageCombo")
        self.language_combo.addItems(["简体中文 / zh_cn", "繁体中文 / zh_tw", "English / en_us"])
        language_row.addWidget(self.language_combo)
        layout.addLayout(language_row)

        # 第二行：工程文件夹位置
        project_folder_row = QHBoxLayout()
        project_folder_label = QLabel("工程文件夹位置:")
        project_folder_label.setObjectName("ProjectFolderLabel")
        project_folder_row.addWidget(project_folder_label)

        self.project_folder_path = QLabel("C:\\CraftEngine-Editor\\resources")
        self.project_folder_path.setObjectName("ProjectFolderPath")
        project_folder_row.addWidget(self.project_folder_path)

        project_folder_button = QPushButton("选择")
        project_folder_button.setObjectName("ProjectFolderButton")
        project_folder_button.clicked.connect(self.select_project_folder)
        project_folder_row.addWidget(project_folder_button)
        layout.addLayout(project_folder_row)

        # 第三行：转换输出文件夹位置
        conversion_folder_row = QHBoxLayout()
        conversion_folder_label = QLabel("转换输出文件夹位置:")
        conversion_folder_label.setObjectName("ConversionFolderLabel")
        conversion_folder_row.addWidget(conversion_folder_label)

        self.conversion_folder_path = QLabel("C:\\CraftEngine-Editor\\conversion")
        self.conversion_folder_path.setObjectName("ConversionFolderPath")
        conversion_folder_row.addWidget(self.conversion_folder_path)

        conversion_folder_button = QPushButton("选择")
        conversion_folder_button.setObjectName("ConversionFolderButton")
        conversion_folder_button.clicked.connect(self.select_conversion_folder)
        conversion_folder_row.addWidget(conversion_folder_button)
        layout.addLayout(conversion_folder_row)

    def select_project_folder(self):
        """选择工程文件夹"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择工程文件夹")
        if folder_path:
            self.project_folder_path.setText(folder_path)

    def select_conversion_folder(self):
        """选择转换输出文件夹"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择转换输出文件夹")
        if folder_path:
            self.conversion_folder_path.setText(folder_path)