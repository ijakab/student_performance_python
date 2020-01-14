from flask import request, jsonify, Flask

app = Flask('student_performance_server')


@app.route('/', methods=['POST'])
def create_task():
    features = request.json.get('features')
    return jsonify(features), 200


app.run()
