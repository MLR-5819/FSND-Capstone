import os
import random
import json
from flask import Flask, render_template, redirect, url_for, Response, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Entry, Category
# from auth import AuthError


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)

  @app.route('/')
  def index():
    return render_template('home.html')

  # GET categories
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
        "image": entry.entry_url,
        "votes": entry.votes
      })

    return render_template(
        'categories.html', categories=cat_data, entries=ent_data)

  # GET one category
  @app.route('/categories/<int:id>', methods=['GET'])
  def show_category(id):
    categories = Category.query.order_by(Category.id).all()
    entries = Entry.query.filter(Entry.category == id).all()
    showcat = Category.query.filter(Category.id == id).one()

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
        "image": entry.entry_url,
        "votes": entry.votes
      })

    return render_template('show_category.html', categories=cat_data, showcat=showcat, entries=ent_data)

  # GET one entry
  @app.route('/entries/<int:id>', methods=['GET'])
  def show_entry(id):
    entry = Entry.query.filter(Entry.id == id).one()
    
    return render_template('show_entry.html', entry=entry)

  # TODO POST request
  @app.route('/entries/add', methods=['GET', 'POST'])
  def add_entry():
    if request.method == 'POST':
      error = False
      success = False
      form = request.get_json()

      newE_name = form.get('entryName', None)
      newE_category = form.get('category', None)
      newE_url = form.get('url', None)

      try:
        new_entry = Entry(
          name=newE_name,
          category=newE_category,
          entry_url=newE_url)
        
        db.session.add(new_entry)
        db.session.commit()
        success = True

      except:
        error = True
        if error:
          db.session.rollback()
          #Alertbox
        abort(422)

      finally:
        db.session.close()
        if success:
          #alertboxsuccess msg
          return redirect(url_for('get_categories'))

    categories = Category.query.order_by(Category.id).all()
    cat_data = []

    for category in categories:
      cat_data.append({
        "id": category.id,
        "type": category.type
      })

    #category query data to create drop down on form
    return render_template('add_entry.html', categories=cat_data)


  # TODO PATCH request

  # TODO DELETE request

  # TODO 4 @app.errorhandler

  return app

APP=create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
