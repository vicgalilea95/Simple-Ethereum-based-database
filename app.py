from flask import Flask, request, jsonify

import logic

import json


app = Flask(__name__)


@app.route('/blockchain/putData', methods=['PUT'])
def putData():
    id = request.json['id']
    data = request.json['data']
    status = logic.putData(id, data)
    return json.dumps({'status': status})





@app.route('/blockchain/getData/<_id>', methods=['GET'])
def getSubasta(_id):
    return (logic.getData(_id)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)