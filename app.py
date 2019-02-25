from flask import Flask,jsonify,request, make_response

import jwt
import datetime
from functools import wraps



app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

def auth_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token')

		if not token:
			return jsonify({"message" : "missing token" })

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'massage' : 'invalid token'})
		return f(*args, **kwargs)

	return decorated

@app.route('/')
def index():

	return jsonify({'message' : 'hello your welcome to learing web token auth learning'})


@app.route('/uprotected')
def unprotected():

	return jsonify({'message' : 'Everyone one can see this'})

@app.route('/protected')
@auth_required
def protected():

	return jsonify({'message' : 'this page needs authentications'})



@app.route('/login')
def Login():
	auth = request.authorization
	if auth and auth.password == 'password' and auth.username == 'username':

		token = jwt.encode({'user': auth.username, 'exp' : datetime.datetime.utcnow() + \
		 datetime.timedelta(minutes = 30)},app.config['SECRET_KEY'])
		return jsonify({'token' : token.decode('UTF-8')})



	return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login Required"' })
	


if __name__ == '__main__':
	app.run(debug = True)