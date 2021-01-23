"""
author:ljt
c_date:2021/1/22 11:45
u_date:2021/1/22 11:45
reversion:1.0
file_name:demo4

"""
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'akljffje783e378bhd'
book = {
    'name': '降龙十八掌',
    'author': '金庸',
    'articles': [
        {
            'id': '001',
            'title': '第一式:飞龙在天',
            'content': '气走督脉行手阳明大肠经商阳，二间，三间，合谷，阳溪，偏历，温溜，下廉，上廉，手三里，曲池，肘髎，手五里，臂臑，肩髃，巨骨，天鼎，扶突，口和髎，迎香.',
        },
        {
            'id': '002',
            'title': '第二式:见龙在田',
            'content': '提气凝神,运气与手少阳三焦经行 关冲液门中渚阳池外关支沟会宗三阳络四渎天井清冷渊消泺臑会肩髎天髎天牖翳风瘛脉颅息角孙耳门耳和髎丝竹空.返任脉停于掌心.',
        },
        {
            'id': '003',
            'title': '第三式:鸿渐于陆',
            'content': '气走浮郄委阳委中附分魄户膏肓神堂譩譆膈关魂门阳纲意舍胃仓肓门志室胞肓秩边合阳承筋承山.气凝会阴.',
        },
    ]
}
users = [
    {
        'email': '123456@qq.com',
        'password': '123456'
    }
]


@app.route('/')
def index():
    articles = book['articles']
    return render_template('index.html', **locals())


@app.route('/<int:pk>')
def detail(pk):
    article = None
    for a in book['articles']:
        if int(a['id']) == pk:
            article = a
    return render_template('detail.html', **locals())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', **locals())
    elif request.method == 'POST':
        user = None
        email = request.form.get('email')
        password = request.form.get('password')
        for u in users:
            print(u['email'], u['password'], '=================')
            if u['email'] == email and u['password'] == password:
                session['user'] = email
                return redirect(url_for('index'))
        flash("用户名或者密码错误")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html', **locals())
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        for u in users:
            if u["email"] == email:
                flash("邮箱已经注册")
                return redirect(url_for('regist'))
        if password != password2:
            flash("密码不一致")
            return redirect(url_for('regist'))

        users.append({
            "email": email,
            "password": password
        })
        print(users, '+++++++++++++++++++')
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='192.168.11.2', port='8000', debug=True)
