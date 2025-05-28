from  app import db

class Member(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    registration_date = db.Column(db.DateTime)