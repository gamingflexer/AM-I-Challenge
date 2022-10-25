from flask_restful import Resource

class helloworld(Resource):
    def get(self):
        return "Hello World!"