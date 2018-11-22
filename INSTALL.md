## 安装与启动

1. 安装Python3版本，确保加入环境变量，pip命令可用

2. 从[PRAT Github项目](https://github.com/xiaobing0805/PRAT)下载源码

3. 执行以下命令安装PRAT依赖

> pip2 install -r requirements.txt
> pip3 install -r requirements.txt
注意：如果有Python2和Python3两个版本，建议区分pip版本，对应pip2和pip3

4.1 执行以下命令启动PRAT服务

> python2 PRAT.py runserver
> python3 PRAT.py runserver
注意：如果有Python2和Python3两个版本，建议区分Python版本，对应Python2和Python3

4.1.1 访问以下网址，即可

http://127.0.0.1:5000

4.2 执行以下命令可外网访问

> python2 PRAT.py runserver -h 0.0.0.0 -p 8000
> python3 PRAT.py runserver -h 0.0.0.0 -p 8000

4.2.1 即可通过你的IP地址来访问

http://ip:8000

注： 
- -h选项指定为0.0.0.0即为绑定本机ip启动，网络其他用户通过你的ip和-p指定的端口即可访问PRAT

- -p指定PRAT服务启动时的端口

默认账号: PRAT
默认密码: 123456

5. 下载selenium webdriver对应的浏览器驱动放在driver目录即可