from flask import Flask
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)
api = Api(app=app)

class replyMessage(Resource):
    def get(self):
        return {'msg':'Hello Wolrd'}

api.add_resource(replyMessage,'/msg')

app.run(port = 5000)
