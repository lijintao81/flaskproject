"""
author:ljt
c_date:2021/1/22 11:45
u_date:2021/1/22 11:45
reversion:1.0
file_name:demo4

"""
from flask import Flask
import os
from views.user import userbp
from views.main import mainbp

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(userbp)
app.register_blueprint(mainbp)
if __name__ == '__main__':
    app.run(host='192.168.11.2', port='8000', debug=True)
