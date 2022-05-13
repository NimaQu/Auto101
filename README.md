# Auto101

使用 Python 和 opencv 实现的卡牌大师自动切牌

[![Python 3.10](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org)

## 配置
复制 config.ini.example 到 config.ini 并修改配置
如果不确定键值，可以打开 debug 模式，这会在控制台输出你所按下按键的值，默认值为 j 红牌，k 蓝牌， l 红牌，
可以配合鼠标驱动使用侧键进行使用，不能使用默认技能按键 w

## 使用
前往 [releases](https://github.com/NimaQu/Auto101/releases) 页面下载预先打包好的文件，修改 config.ini 后运行 auto101.exe 即可
程序运行后会自动检测技能栏的位置，确保技能图表无遮挡并且在屏幕下半部分

## 手动安装
使用 pip 安装 requirements.txt 里的依赖，修改 config.ini 后运行 main.py 即可

## 免责声明
这个程序不会对游戏客户端及内存进行任何读写，但它也不会试图隐藏自己，没有任何关于规避反作弊的措施。
如果你不能实现，那我建议你不要在在线游戏中使用，被封了也不要来找我
