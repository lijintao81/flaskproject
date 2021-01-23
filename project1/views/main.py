"""
author:ljt
c_date:2021/1/23 14:44
u_date:2021/1/23 14:44
reversion:1.0
file_name:main

"""
from flask import render_template, Blueprint

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

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    articles = book['articles']
    return render_template('index.html', **locals())


@mainbp.route('/<int:pk>')
def detail(pk):
    article = None
    for a in book['articles']:
        if int(a['id']) == pk:
            article = a
    return render_template('detail.html', **locals())
