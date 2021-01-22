"""
author:ljt
c_date:2021/1/22 9:27
u_date:2021/1/22 9:27
reversion:1.0
file_name:demo2

"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '欢迎来到首页'


@app.route('/<int:pk>')
def detail(pk):
    return f'欢迎来到flask{pk}'


if __name__ == '__main__':
    # debug=True  开启调试模式，修改代码不需要重启
    app.run(host='192.168.11.2', port='6789', debug=True)
