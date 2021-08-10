from app import db
from datetime import datetime

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'publisher is {}'.format(self.name)

class Book(db.Model):
    __tablename__='book'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(500),nullable=True,index=True)
    author= db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(500))
    img_url = db.Column(db.String(500))
    num_page = db.Column(db.String(100))
    pub_id = db.Column(db.Integer,db.ForeignKey('publication.id'))

    def __init__(self,title,author,avr_rating,pub_id,format,img_url,num_page):
        self.title = title
        self.author = author
        self.avg_rating =avr_rating
        self.format = format
        self.img_url = img_url
        self.num_page = num_page
        self.pub_id = pub_id

    def __repr__(self):
        return "book is {} , {}, {}, {}, {}, {}, {}".format(self.title,self.author,self.avg_rating,self.format,self.img_url,self.num_page,self.pub_id)



