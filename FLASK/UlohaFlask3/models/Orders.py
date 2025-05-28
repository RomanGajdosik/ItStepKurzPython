from app import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_name = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    order_date = db.Column(db.DateTime)
    customer = db.relationship('Customer', backref='orders')