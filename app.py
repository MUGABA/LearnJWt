from flask import Flask,jsonify,request, make_response

import jwt
import datetime
users = [{
	'name':'Rashdi',
	'username': 'mgb',
	'password': 'password'
}]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

@app.route('/uprotected')
def unprotected():

	return ''

@app.route('/protected')
def protected():

	return ''

@app.route('/register',methods = ['POST'] )
def register():
	data = request.get_json()

	name = data['name']
	username = data['username']
	password = data['password']

	for user in users:
		user = dict(name = name, username = username, password = password)

		users.append(user)

	return jsonify({'user' : user})


@app.route('/login')
def Login():
	auth = request.authorization
	print(auth)
	if auth.password == user.password:
		token = jwt.encode({'user': auth.username, 'exp' : datetime.datetime.utcnow() + \
		 datetime.timedelta(minutes = 30)},app.config['SECRET_KEY'])
		return jsonify({'token' : token.decode('UTF-8')})


	return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic-realm = "Login Required"' })
	


if __name__ == '__main__':
	app.run(debug = True)