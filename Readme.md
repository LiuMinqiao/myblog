# myBlog项目

# 1 环境准备
    mysql 5.7.33
    python 3.6
    python 中安装的库见requirements.txt文件

# 2 初始化

```bash
django-admin startproject myBlog
```

新建工程项目后的目录结构

find .

```bash
.
./myBlog
./myBlog/manage.py
./myBlog/myBlog
./myBlog/myBlog/settings.py
./myBlog/myBlog/urls.py
./myBlog/myBlog/wsgi.py
./myBlog/myBlog/__init__.py
./Readme.md



The outer myBlog/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
The inner myBlog/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. myBlog.urls).
myBlog/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
myBlog/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
myBlog/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
myBlog/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.
```

# 3 完成进度

```bash
2021-07-20:
在myBlog的项目中新建了index,polls,unitest共计3个App。
其中unitest用来测试数据库的增删改查功能。
polls尚未进行开发。
index实现了网站的注册，登录，登出功能。
##########################################


```



# 4 运行方法

```bash
# 假设当前位于D:\MyWebsites\web-blog\myBlog， 启动cmd，输入 python manage.py runserver 0:8021，即可在localhost:8021进行访问。
# 若想要通过ip:port的方式访问，需要在myBlog文件夹下的settings.py中，将自己电脑的ip加入到ALLOWED_HOSTS列表中。
D:\MyWebsites\web-blog\myBlog>  python manage.py runserver 0:8021
```








# 5 mysql数据库设置
    用户名: root
    密码： 123456
    数据库名称： myblog

```mysql
-- 表格 index_logindata
-- index_logindata 示例数据：

1,123@qq.com,1234
2,3452@qq.com,12345



```
```mysql
-- 表格 index_user
-- 表格 index_user示例数据

1,小明,23,123@qq.com
2,小红,33,3452@qq.com

```# myblog
