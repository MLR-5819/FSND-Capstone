import os
import random
import json
from datetime import date
from flask import Flask, render_template, redirect, url_for, Response, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, link_db, Entry, Category
from forms import AddEntryForm
# from auth import AuthError

SECRET_KEY=os.urandom(32)

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  app.config['SECRET_KEY'] = SECRET_KEY
  CORS(app)
  setup_db(app)
  db = link_db()

  @app.route('/')
  def index():
    return render_template('home.html')

  # GET categories
  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories = Category.query.order_by(Category.type.asc()).all()
    entries = Entry.query.order_by(Entry.date.desc()).all()

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
    categories = Category.query.order_by(Category.type.asc()).all()
    entries = Entry.query.filter(Entry.category == id).order_by(Entry.date.desc()).all()
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

      try:
        form = AddEntryForm()

        entry = Entry(
          name=form.name.data,
          category=form.category.data,
          entry_url=form.url.data,
          votes="0",
          date=date.today())
        
        db.session.add(entry)
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

    categories = Category.query.order_by(Category.type.asc()).all()
    cat_list = [(i.id, i.type) for i in categories]
    form = AddEntryForm()
    form.category.choices = cat_list
    
    return render_template('add_entry.html', form=form)


  # TODO PATCH request
  # AUTH Users can update entry

  # TODO DELETE request
  # Auth Admin can delete

  # TODO Play section
  

  # TODO 4 @app.errorhandler

  return app

APP=create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
