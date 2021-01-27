from flask import jsonify
def demoApiService():
    return jsonify(
        {
            "status": 0,
            "data": "demo"
        }
    )