import sys
from flask_restful import Api, reqparse, Resource
from flask import current_app, g, jsonify


api = Api()

class Test1(Resource):
    @staticmethod
    def get():
        print('test1')
        return {'api_test1': 'sucess'}

class Test2(Resource):
    @staticmethod
    def get():
        print('test2')
        return {'api_test2': 'sucess'}



api.add_resource(Test1, '/api/test1')
api.add_resource(Test2, '/api/test2')