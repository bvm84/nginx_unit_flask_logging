import sys
from flask_restful import Api, reqparse, Resource
from flask import current_app, g, jsonify


api = Api()

class Test1(Resource):
    @staticmethod
    def get():
        current_app.logger.info('Test1 logger message')
        print('Test1 print message')
        return {'api_test1': 'sucess'}

class Test2(Resource):
    @staticmethod
    def get():
        current_app.logger.info('Test2 logger message')
        print('Test2 print message')
        return {'api_test2': 'sucess'}



api.add_resource(Test1, '/api/test1')
api.add_resource(Test2, '/api/test2')