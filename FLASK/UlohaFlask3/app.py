from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udmw0ybt4tlrfip6qvod:iBSHgCbIOtxBAixxJoeNQAMXflngee@byncjuw7s8tagen1muul-postgresql.services.clever-cloud.com:50013/byncjuw7s8tagen1muul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)

from models.Orders import Order
from models.Customers import Customer


@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    customers_list = []
    for customer in customers:
        customers_list.append({
            'id': customer.id,
            'name': customer.name,
            'email': customer.email
        })
    return jsonify(customers_list)

@app.route('/orders',methods=['GET'])
def get_orders():
    orders = Order.query.all()
    orders_list = []
    for order in orders:
        orders_list.append({
            'id': order.id,
            'customer_id': order.customer_id,
            'product_name': order.product_name,
            'quantity': order.quantity,
            'order_date': order.order_date.isoformat(),
            'customer':order.customer.name
        })
    return jsonify(orders_list)

@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
def get_orders_by_customer(customer_id):
    orders = Order.query.filter_by(customer_id=customer_id).all()
    orders_list = []
    for order in orders:
        orders_list.append({
            'id': order.id,
            'product_name': order.product_name,
            'quantity': order.quantity,
            'order_date': order.order_date.isoformat()
        })
    return jsonify(orders_list)
@app.route('/customers/<int:customer_id>/orders',methods=['POST'])
def add_order(customer_id):
    data = request.get_json()
    new_order = Order(
        customer_id=customer_id,
        product_name=data['product_name'],
        quantity=data['quantity'],
        order_date=data['order_date']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order added successfully!'}), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    order = Order.query.get_or_404(order_id)
    order.product_name = data['product_name']
    order.quantity = data['quantity']
    order.order_date = data['order_date']
    db.session.commit()
    return jsonify({'message': 'Order updated successfully!'})

@app.route('/orders/<int:id>',methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully!'}), 204


if __name__ == '__main__':
    app.run()
