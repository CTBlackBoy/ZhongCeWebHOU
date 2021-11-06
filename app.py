import uuid

from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
import config
from models import ReportMessage,ReportBanner,InformationBanner,InformationMessage,TestinMessage,ArticleMessage
from flask import request
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config)
# db.init_app(app)


@app.route('/')
def hello_world():
    ReportR = []
    ReportM = ReportMessage.query.filter().all()
    for M in ReportM:
        title = M.title
        auther = M.auther
        time = M.time
        ReportR.append({'title': title, 'auther': auther, 'time': time})
    InformationM = InformationMessage.query.filter().all()
    InformationR = []
    for M in InformationM:
        title = M.title
        auther = M.auther
        time = M.time
        InformationR.append({'title': title, 'auther': auther, 'time': time})
    ArticleM = ArticleMessage.query.filter().all()
    ArticleR = []
    for M in ArticleM:
        title = M.title
        auther = M.auther
        time = M.time
        ArticleR.append({'title': title, 'auther': auther, 'time': time})
    RelationR = []
    RelationM = ArticleMessage.query.filter().all()
    for M in RelationM:
        title = M.title
        auther = M.auther
        time = M.time
        RelationR.append({'title': title, 'auther': auther, 'time': time})

    # return send_file('templates/src/app/Main/Main.component.html')
    return ''

# 这部分是Client端
@app.route('/Report')
def Report():
    if request.method == 'GET':
        ReportR = []
        ReportM = ReportMessage.query.filter().all()
        for M in ReportM:
            title = M.title
            auther = M.auther
            content = M.content
            time = M.time
            ReportR.append({'title': title,'auther': auther, 'time': time, 'content': content})

    return 'Message'


@app.route('/Information')
def Information():
    InformationM = InformationMessage.query.filter().all()
    InformationR = []
    for M in InformationM:
        title = M.title
        auther = M.auther
        time = M.time
        content = M.content
        image = M.image
        InformationR.append({'title': title, 'auther': auther, 'time': time, 'content':content, 'image': image})

    InformationB = InformationBanner.query.filter().all()
    InformationBR = []
    for B in InformationB:
        title = B.title
        content = B.content
        image = B.image
        InformationBR.append({'title': title, 'content': content, 'image': image})

    return {'Message':InformationR, 'Banner':InformationBR}

@app.route('/Article')
def Article():
    if request.method == 'GET':
        ArticleR = []
        ArticleM = ArticleMessage.query.filter().all()
        for M in ArticleM:
            title = M.title
            auther = M.auther
            time = M.time
            ArticleR.append({'title': title,'auther': auther, 'time': time})

    return {'Message':ArticleR}


@app.route('/Relation')
def Relation():


    return {'Message'}

@app.route('/Testin')
def Testin():
    TestinM = TestinMessage.query.filter().all()
    if request.method == 'GET':
        TestinR = []
        TestinM = TestinMessage.query.filter().all()
        for M in TestinM:
            title = M.title
            auther = M.auther
            time = M.time
            image = M.image
            TestinR.append({'title': title,'auther': auther, 'time': time, 'image': image})

    return {'testin': TestinR}

# 这是Bussniss端(用户)
@app.route('/write/Article', methods = ['GET', 'POST'])
def WriteArticle():
    if request.method == 'GET':
        return ''
    elif request.method == 'POST':
        auther = request.form['auther']
        title = request.form['title']
        time = datetime.now()
        image = request.form['image']
        content = request.form['content']

        article = ArticleMessage(auther= auther,title= title, time= time, image= image, content= content)
        db.session.add(article)
        db.session.commit()
    return ''
@app.route('/Write/Read', methods = ['GET', 'POST'])
def WriteRead():
    if request.method == 'POST':
        ReportR = []
        ReportM = ArticleMessage.query.filter().all()
        for M in ReportM:
            title = M.title
            auther = M.auther
            time = M.time
            UUID = uuid.uuid1()
            agree = M.agree
            talk = M.talk
            read = M.read
            ReportR.append({'title': title,'auther': auther, 'time': time, 'UUID': UUID, 'agree': agree, 'talk': talk, 'read': read})

    return {'Message':ReportR}
# 这是Admin端(用户)
@app.route('/Admin/Report', methods = ['GET', 'POST'])
def AdminReport():
    if request.method == 'POST':
        auther = request.form['auther']
        title = request.form['title']
        time = datetime.now()
        image = request.form['image']
        content = request.form['content']
        report = ReportMessage(auther=auther, title=title, time=time, image=image, content = content)
        db.session.add(report)
        db.session.commit()

    return ''
@app.route('/Admin/Information', methods = ['GET', 'POST'])
def AdminInformation():
    if request.method == 'POST':
        auther = request.form['auther']
        title = request.form['title']
        time = datetime.now()
        image = request.form['image']
        content = request.form['content']
        information = InformationMessage(auther=auther, title=title, time=time, image=image, content = content)
        db.session.add(information)
        db.session.commit()

    return ''

@app.route('/Admin/Testin', methods = ['GET', 'POST'])
def AdminTestin():
    if request.method == 'POST':
        auther = request.form['auther']
        title = request.form['title']
        time = datetime.now()
        image = request.form['image']
        content = request.form['content']
        testin = TestinMessage(auther=auther, title=title, time=time, image=image, content = content)
        db.session.add(testin)
        db.session.commit()

    return ''



if __name__ == '__main__':
    db.create_all()
    app.run(host='10.10.10.1',port=200)
