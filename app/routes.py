from flask import Blueprint, request, jsonify
from .models import Product, CartItem
from . import db

main = Blueprint('main', __name__)

@main.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify([{'name': p.name, 'price': p.price} for p in products])
