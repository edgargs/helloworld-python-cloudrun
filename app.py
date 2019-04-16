import os

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    target =os.environ.get('TARGET','World')
    return 'Hello {} from Cloud Run!\n'.format(target)

class Hello(Resource):
    def get(self, name):
    return {"Hello":name}

api.add_resource(Hello, '/hello/<name>')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))