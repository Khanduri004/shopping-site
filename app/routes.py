from flask import Blueprint, render_template, request, redirect
from .models import Product, CartItem
from . import db

@main.before_app_first_request
def create_tables():
    db.create_all()
    if not Product.query.first():
        db.session.add_all([
            Product(name='Phone', price=499.99),
            Product(name='Laptop', price=899.99),
            Product(name='Shoes', price=59.99),
        ])
        db.session.commit()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/add/<int:product_id>')
def add_to_cart(product_id):
    item = CartItem.query.filter_by(product_id=product_id).first()
    if item:
        item.quantity += 1
    else:
        item = CartItem(product_id=product_id, quantity=1)
        db.session.add(item)
    db.session.commit()
    return redirect('/cart')

@main.route('/cart')
def view_cart():
    cart_items = CartItem.query.all()
    return render_template('cart.html', cart=cart_items)
