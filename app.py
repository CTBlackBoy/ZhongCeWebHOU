import json
import uuid


from flask import Flask, send_file
from flask_cors import cross_origin
from flask_sqlalchemy import SQLAlchemy
import config
from models import ReportMessage, ReportBanner, InformationBanner, InformationMessage, TestinMessage, ArticleMessage, \
    UserInformation
from flask import request
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config)
# db.init_app(app)


@app.route('/')
@cross_origin(supports_credentials=True)
def hello_world():
    Message = {}
    TestinR = []
    TestinM = TestinMessage.query.filter().all()
    for M in TestinM:
        auther = M.auther
        title = M.title
        content = M.content
        time = M.time
        image = M.image
        TestinR.append({"title": title, "auther": auther, "content": content, "time": time, "image": image})
    Message["TestinR"] = TestinR
    ReportR = []
    ReportM = ReportMessage.query.filter().all()
    for M in ReportM:
        title = M.title
        auther = M.auther
        content = M.content
        time = M.time
        ReportR.append({"title": title, "auther": auther, "time": time, "content": content})
    Message["ReportR"] = ReportR
    InformationM = InformationMessage.query.filter().all()
    InformationR = []
    for M in InformationM:
        title = M.title
        auther = M.auther
        time = M.time
        content = M.content
        image = M.image
        InformationR.append({"title": title, "auther": auther, "time": time, "content": content, "image": image})
    Message["InformationR"] = InformationR
    ArticleR = []
    ArticleM = ArticleMessage.query.filter().all()
    for M in ArticleM:
        title = M.title
        auther = M.auther
        time = M.time
        UUID = M.UUID
        ArticleR.append({"title": str(title), "auther": str(auther), "time": str(time)})
    Message["ArticleR"] = ArticleR
    return (Message)

# 这部分是Client端
@app.route('/Report')
@cross_origin(supports_credentials=True)
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

    return {'ReportR': ReportR}


@app.route('/Information')
@cross_origin(supports_credentials=True)
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


    return {'InformationR':InformationR}

@app.route('/Article')
@cross_origin(supports_credentials=True)
def Article():
    if request.method == 'GET':

        ArticleR = []
        ArticleM = ArticleMessage.query.filter().all()
        for M in ArticleM:
            title = M.title
            auther = M.auther
            time = M.time
            UUID = M.UUID
            ArticleR.append({'title': title,'auther': auther, 'time': str(time)})

    # return json.dumps({'ArticleR': ArticleR})
    return {'ArticleR': ArticleR}

@app.route('/Testin')
@cross_origin(supports_credentials=True)
def Testin():
    if request.method == 'GET':
        TestinR = []
        TestinM = TestinMessage.query.filter().all()
        for M in TestinM:
            auther = M.auther
            title = M.title
            content = M.content
            time = M.time
            image = M.image
            TestinR.append({'title': title,'auther': auther, 'content':content, 'time': time, 'image': image})

    return {'TestinR': TestinR}


@app.route('/Relation')
def Relation():


    return {'Message'}

# 这是Bussniss端(用户)
@app.route('/Admin-register', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def AdminRegister():
    if request.method == 'GET':
        print('Get')
        return '111'
    elif request.method == 'POST':
        auther = request.form["auther"]
        email = request.form["email"]
        password = request.form["password"]

        user = UserInformation(auther= auther, email= email, password= password)
        db.session.add(user)
        db.session.commit()
        return {'msg': "SUCCESS"}
@app.route('/Admin-login', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def AdminLogin():
    if request.method == 'GET':
        print('Get')
        return '111'
    elif request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        passwordGet = UserInformation.query.filter_by(email=email).first().password
        if(password == passwordGet):
            print("success")
        else:
            print('passwordR',passwordGet)
            print('password',password)
            print('Err')
        # db.session.add(user)
        # db.session.commit()
        return {"msg": password}
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
