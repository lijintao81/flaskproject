"""
author:ljt
c_date:2021/1/22 9:27
u_date:2021/1/22 9:27
reversion:1.0
file_name:demo2

"""
from flask import Flask

app = Flask(__name__)


# 路由在app之后，在启动之前

# 静态路由
@app.route('/')  # 根路径
def index():
    return '欢迎来到首页'


# 动态路由
@app.route('/<int:pk>')
def detail(pk):
    return f'欢迎来到flask{pk}'


if __name__ == '__main__':
    # debug=True  开启调试模式，修改代码不需要重启
    # host设置地址
    # port设置端口
    app.run(host='192.168.11.2', port='6789', debug=True)
