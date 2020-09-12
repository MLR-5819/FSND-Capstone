import os
import random
import json
from flask import Flask, render_template, url_for, Response, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Entry, Category
#from auth import AuthError

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)

  @app.route('/')
  def index():
    return render_template('home.html')

  #TODO GET request
  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories = Category.query.order_by(Category.id).all()
    entries = Entry.query.all()
    
    cat_data = []
    ent_data = []

    for category in categories:
      cat_data.append({
        "id": category.id,
        "type": category.type
      })

    for entry in entries:
      ent_data.append({
        "id": entry.id,
        "name": entry.name,
        "category": entry.category,
        "image": entry.entry_url,
        "votes": entry.votes
      })

    return render_template('categories.html', categories=cat_data, entries=ent_data)


  #TODO GET request

  #TODO POST request

  #TODO PATCH request

  #TODO DELETE request

  #TODO 4 @app.errorhandler

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)