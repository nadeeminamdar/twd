from flask import Flask, jsonify, request
app = Flask(__name__)

# Dummy data, we are not using any database.. yet

accounts = [
	{'name': "John",       'balance': 453.75},
	{'name': "George",     'balance': 109.83},
	{'name': "Jerry",      'balance': 109.32},
	{'name': "Kramer",     'balance': 10.98},
	{'name': "Martin",     'balance': 1.42},
	{'name': "Michael",    'balance': 453.75},
	{'name': "Francis",    'balance': 109.83},
	{'name': "James",      'balance': 59.32},
	{'name': "Arthur",     'balance': 10.98},
	{'name': "Jerome",     'balance': 117.32},
	{'name': "Newman",     'balance': 134.99},
	{'name': "Sacamano",   'balance': 1554.73},
	{'name': "Peter",      'balance': 110.00},
	{'name': "Timothy",    'balance': 209.44}
]

#----------- Introduction ----------------------------------

@app.route('/')
def index():
  return 'You are at the base for these REST services'

@app.route('/about')
def about():
  return 'About this page'

#---------- REST Services ---------------------------------

@app.route('/accounts', methods=["GET"])
def getAccounts():
    return jsonify(accounts)

@app.route('/account/<int:id>', methods=["GET"])
def getAccount(id):
    id = int(id) -1
    return jsonify(accounts[id])

@app.route('/account', methods=["POST"])
def addAccount(id):
    name    = request.json['name']
    balance = request.json['balance']
    data    = {'name': name, 'balance': balance}
    accounts.append(data)
    return jsonify(data)

#---------- Runner -------------

if __name__ == '__main__':
	app.run(port=8001)



