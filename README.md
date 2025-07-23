![](resources/logo.ico)
# CraftEngine-Editor

## 简介
CraftEngine-Editor是一个基于PyQt5的项目，用于快速创建和编辑基于CraftEngine插件的拓展包配置文件。

## 特性
- 快速创建新的插件配置文件
- 编辑已有的插件配置文件
- 实时预览配置文件编辑结果
- 支持 ItemsAdder & Nexo 配置转换为 CraftEngine 配置
- 支持插件配置文件的版本控制
- 支持插件配置文件的备份和恢复
- 支持插件配置文件的导入和导出

## 项目结构
```angular2html
CraftEngine-Editor/
├── app.py # 应用程序的入口
├── resources/ # 存放资源文件（如图像、图标等）
│ ├── icon.png
├── styles/ # 存放样式文件（如QSS等）
│ ├── style.qss
├── modules/ # 存放项目UI和模块的目录
│ ├── module1.py
│ ├── module2.py
└── README.md # 项目的说明文件
```

## 安装依赖
```bash
pip install -r requirements.txt
```

## 运行项目
```bash
python app.py
```
