from flask import Flask, jsonify,request,json
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

import jwt
import datetime
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
# basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:////home/rashid/Desktop/LearnJWT/tmp/real.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):

	

	id = db.Column(db.Integer, primary_key = True)
	public_id =  db.Column(db.String(50), unique = True)
	name = db.Column(db.String(50))
	password = db.Column(db.String(20))
	is_admin = db.Column(db.Boolean)

	# def __init__(self,id, public_id, name, password,is_admin):
	# 	self.id = id
	# 	self.public_id = public_id
	# 	self.name = name
	# 	self.password = password
	# 	self.is_admin = is_admin


class Todo(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.String(50))
	complete = db.Column(db.Boolean)
	user_id = db.Column(db.Integer)

@app.route('/users')
def get_all_users():

	return ''

@app.route('/users/<int:user_id>',methods = ['GET'])
def get_one_user(user_id):
	return ''

@app.route('/users', methods = ['POST'])
def create_user():
	data = request.get_json()
	name  = data.get('name')
	password_hash = generate_password_hash(data['password'],method = 'sha256')
	new_user = User(public_id = str(uuid.uuid4()), name = name, \
	 password = password_hash ,is_admin = False )
	
	db.session.add(new_user)

	db.session.commit()

	return jsonify({'message':'user created successifuly'})

@app.route('/users/<int:user_id>',methods = ['PUT'])
def promote_user(user_id):
	return ''

@app.route('/users/<int:user_id>',methods = ['DELETE'])
def delete_user():
	return ''





if __name__ == '__main__':
	app.run(debug = True)



















