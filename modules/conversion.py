from PyQt5.Qt import *

class Conversion(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("ConversionWidget")
        layout = QVBoxLayout(self)

        # 第一行：选择要转换的包配置文件夹
        first_row = QHBoxLayout()
        select_folder_label = QLabel("选择要转换的包配置文件夹：")
        select_folder_label.setObjectName("SelectFolderLabel")
        first_row.addWidget(select_folder_label)

        select_folder_button = QPushButton("选择文件夹")
        select_folder_button.setObjectName("SelectFolderButton")
        select_folder_button.clicked.connect(self.select_folder)
        first_row.addWidget(select_folder_button)
        layout.addLayout(first_row)

        # 第二行：选择原来的包配置加载插件
        second_row = QHBoxLayout()
        select_plugin_label = QLabel("选择原来的包配置加载插件：")
        select_plugin_label.setObjectName("SelectPluginLabel")
        second_row.addWidget(select_plugin_label)

        self.plugin_combo = QComboBox()
        self.plugin_combo.setObjectName("PluginCombo")
        self.plugin_combo.addItems(["ItemsAdder", "Nexo"])  # 添加选项
        second_row.addWidget(self.plugin_combo)
        layout.addLayout(second_row)

        # 添加一个空间来填充，使按钮靠下
        layout.addStretch()

        # 开始转换按钮
        convert_button = QPushButton("开始转换")
        convert_button.setObjectName("ConvertButton")
        convert_button.clicked.connect(self.start_conversion)
        layout.addWidget(convert_button, alignment=Qt.AlignRight)

    def select_folder(self):
        """选择文件夹"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            QMessageBox.information(self, "选择文件夹", f"已选择文件夹：{folder_path}")

    def start_conversion(self):
        """开始转换"""
        selected_plugin = self.plugin_combo.currentText()
        QMessageBox.information(self, "开始转换", f"开始转换，选择的插件：{selected_plugin}")