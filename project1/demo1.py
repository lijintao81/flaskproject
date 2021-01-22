"""
author:ljt
c_date:2021/1/22 9:06
u_date:2021/1/22 9:06
reversion:1.0
file_name:demo1

"""
# 1引入flask模块
from flask import Flask

# 2构建flask应用
app = Flask(__name__)
# 3 启动应用
if __name__ == '__main__':
    app.run()
