from exts import db
import DateTime

class ReportMessage(db.Model):
    __tablename__ = 'ReportMessage'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(200))
    auther = db.Column(db.String(20),nullable = False)
    content = db.Column(db.String(200),nullable = False)
    time = db.Column(db.DateTime,nullable = False)
    image = db.Column(db.String(100),nullable = False)
class ReportBanner(db.Model):
    __tablename__ = 'ReportBanner'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(20),nullable = False)
    content = db.Column(db.String(200),nullable = False)
    image = db.Column(db.String(100),nullable = False)

class InformationMessage(db.Model):
    __tablename__ = 'InformationMessage'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(200))
    auther = db.Column(db.String(20),nullable = False)
    content = db.Column(db.String(200),nullable = False)
    time = db.Column(db.DateTime,nullable = False)
    image = db.Column(db.String(100),nullable = False)
class InformationBanner(db.Model):
    __tablename__ = 'InformationBanner'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(20),nullable = False)
    content = db.Column(db.String(200),nullable = False)
    image = db.Column(db.String(100),nullable = False)

class ArticleMessage(db.Model):
    __tablename__ = 'ArticleMessage'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    auther = db.Column(db.String(20),nullable = False)
    title = db.Column(db.String(100),nullable = False)
    time = db.Column(db.DateTime,nullable = False)
    image = db.Column(db.String(100),nullable = False)
    content = db.Column(db.String(100),nullable=False)
    agree = db.Column(db.Integer,default=0)
    talk = db.Column(db.Integer, default=0)
    read = db.Column(db.Integer, default=0)

class TestinMessage(db.Model):
    __tablename__ = 'TestinMessage'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    auther = db.Column(db.String(20),nullable = False)
    title = db.Column(db.String(100),nullable = False)
    content = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime,nullable = False)
    image = db.Column(db.String(100),nullable = False)

