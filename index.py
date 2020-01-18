from flask import request, jsonify, Flask, send_from_directory
import models

app = Flask('student_performance_server')


@app.route('/predict', methods=['POST'])
def predict():
    features = request.json.get('features')
    modelOutputs = models.predict_all_from_features(features, prep=True)
    return jsonify(modelOutputs), 200


@app.route('/<path:path>', methods=['GET'])
def serve_web(path):
    return send_from_directory('web', path)


@app.route('/', methods=['GET'])
def serve_homepage():
    return send_from_directory('web', 'index.html')



app.run()
