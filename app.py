from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

emp_list = {}
emp_info = {}
class Employee(Resource):
    def get(self, emp_id):
        return {emp_id: emp_list[emp_id]},200
    def put(self, emp_id):
        emp_info['Name'] = request.form['name']
        emp_info['Age'] = request.form['age']
        emp_info['sex'] = request.form['sex']
        emp_info['salary'] = request.form['salary']
        emp_list[emp_id] = emp_info
        return {emp_id: emp_list[emp_id]},200

api.add_resource(Employee,'/<string:emp_id>')

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
