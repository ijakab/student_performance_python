from flask import request, jsonify, Flask
import models

app = Flask('student_performance_server')
@app.route('/', methods=['POST'])
def create_task():
    features = request.json.get('features')
    modelOutputs = models.predict_all_from_features(features, prep=True)
    return jsonify(modelOutputs), 200


app.run()
