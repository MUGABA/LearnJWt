from flask import Flask ,make_response,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():

	if request.authorization and request.authorization.username == 'username1' and request.authorization.password == 'password':
		return jsonify({"message": "you are logged in "})

	return make_response('could not login', 401, {'WWW-Authenticate': 'Basic realm = "Login Recquired'})


if __name__ == '__main__':
	app.run(debug=True)

