#!/bin/bash
 # 从第一行到最后一行分别表示：
 # 1. 收集静态文件到根目录
 # 2. 生产数据库迁移文件
 # 3. 根据数据库迁移文件来修改数据库
 # 4. 用 uwsgi启动 django 服务, 不再使用python manage.py runserver
 python3 manage.py collectstatic --noinput&&
 python3 manage.py makemigrations&&
 python3 manage.py migrate&&
 uwsgi --ini /var/www/html/myproject/uwsgi.ini
 #uwsgi --ini  /Volumes/LMQ/Downloads/PM/my/myproject_docker/myproject/uwsgi.ini
 #python3 manage.py runserver 0.0.0.0:8000

