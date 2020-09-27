import os
import random
import json
from datetime import date
from flask import Flask, render_template, redirect, url_for, Response, request, abort, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, link_db, Entry, Category
from forms import AddEntryForm, UpdateEntryForm
from auth import AuthError, requires_auth

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
  @app.route('/api/categories', methods=['GET'])
  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories = Category.query.order_by(Category.type.asc()).all()
    entries = Entry.query.order_by(Entry.date.desc()).all()

    if not categories:
      abort(404)

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

    if request.path == '/api/categories':
      return jsonify({
        'success': True,
        'categories': cat_data,
        'entries': ent_data
      }), 200

    return render_template(
        'categories.html', categories=cat_data, entries=ent_data)

  # GET one category
  @app.route('/api/categories/<int:id>', methods=['GET'])
  @app.route('/categories/<int:id>', methods=['GET'])
  def show_category(id):
    categories = Category.query.order_by(Category.type.asc()).all()
    entries = Entry.query.filter(Entry.category == id).order_by(Entry.date.desc()).all()
    showcat = Category.query.filter(Category.id == id).one_or_none()

    if not showcat:
      abort(404)

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

    if request.path == '/api/categories/' + str(id):
      return jsonify({
        'success': True,
        'categories': cat_data,
        'entries': ent_data
      }), 200

    return render_template('show_category.html', categories=cat_data, showcat=showcat, entries=ent_data)

  # GET one entry
  @app.route('/api/entries/<int:id>', methods=['GET'])
  @app.route('/entries/<int:id>', methods=['GET'])
  def show_entry(id):
    entry = Entry.query.filter(Entry.id == id).one_or_none()
    
    if not entry:
      abort(404)

    ent_data = []

    ent_data.append({
        "id": entry.id,
        "name": entry.name,
        "image": entry.entry_url,
        "votes": entry.votes
    })

    if request.path == '/api/entries/' + str(id):
      return jsonify({
        'success': True,
        'entry': ent_data
      }), 200

    return render_template('show_entry.html', entry=entry)

  # DONE POST request
  @app.route('/api/entries/add', methods=['GET', 'POST'])
  @app.route('/entries/add', methods=['GET', 'POST'])
  # @requires_auth('post:entry') App allows non-user to add entries
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
  @app.route('/entries/<int:id>/update', methods=['GET', 'POST', 'PATCH'])
  @requires_auth(permission='patch:entry')
  def update_entry(payload, id):
    entry = Entry.query.filter(Entry.id == id).one()
    category = Category.query.filter(Category.id == entry.category).one()
    
    if not entry:
      abort(404)
    
    if request.method == 'GET':
      categories = Category.query.order_by(Category.type.asc()).all()
      cat_list = [(i.id, i.type) for i in categories]
      form = UpdateEntryForm()
      form.category.choices = cat_list
      
      return render_template('update_entry.html', form=form, category=category, entry=entry)
    
    error = False
    success = False
      
    try:
      update = UpdateEntryForm()
      entry.name = update.name.data
      entry.category = update.category.data

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
      #if success:
        #alertboxsuccess msg
      
    return redirect(url_for('get_categories'))
     

  # TODO DELETE request
  # Auth Admin can delete
  @app.route('/entries/<int:id>/delete', methods=['GET', 'DELETE'])
  @requires_auth(permission='delete:entry')
  def delete_entry(payload, id):
    entry = Entry.query.filter(Entry.id == id).one_or_none()
    
    if not entry:
      abort(404)

    error = False
    success = False

    try:
      db.session.delete(entry)
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
      #if success:
        #alertboxsuccess msg

    return redirect(url_for('get_categories'))

  # TODO Play section for future version
  @app.route('/play')
  def play():
    return render_template('play.html')

  # TODO Results Section for future version

  # DONE 4 @app.errorhandler
  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "Bad Request"
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
       "error": 404,
       "message": "Resource Not Found"
    }), 404

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 405,
      "message": "Method Not Allowed"
    }), 405

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "Unprocessable"
    }), 422

  @app.errorhandler(500)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
    }), 500

  @app.errorhandler(AuthError)
  def auth_error(error):  
    return jsonify({
      "success": False,
      "error": error.status_code,
      "message": error.error
    }), error.status_code

  return app

APP=create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
