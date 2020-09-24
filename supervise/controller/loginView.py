import json

from conf.account import USERS
from flask import render_template, request
from flask_login import login_user, logout_user, login_required

from supervise import login_manager
from supervise.models.User import User


def get_user(user_name):
    """根据用户名获得用户记录"""
    for user in USERS:
        if user.get("name") == user_name:
            return user
    return None

@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(user_id):
    return User.get(user_id)


def login():
    if request.method == 'POST':
        recv_data = json.loads(request.get_data(as_text=True))
        response ={}
        user_name = recv_data['user_name']
        password = recv_data['password']
        user_info = get_user(user_name)  # 从用户数据中查找用户记录
        if user_info is None:
            response['code'] = 1
            response['emsg'] = "用户名或密码密码有误"
            return response
        else:
            user = User(user_info)  # 创建用户实体
            if user.password_hash == password:  # 校验密码
                login_user(user)  # 创建用户 Session
                response['code'] = 0
                return response
            else:
                response['code'] = 1
                response['emsg'] = "用户名或密码密码有误"
                return response
    return render_template('login.html')
@login_required
def logout():
    logout_user()
    return render_template('login.html')

def add_login_view(app):
    app.add_url_rule('/login',methods=['POST','GET'], view_func=login)
    app.add_url_rule('/logout',methods=['POST','GET'], view_func=logout)