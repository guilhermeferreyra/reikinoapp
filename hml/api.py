from flask import Flask
from flask import request
import json

app = Flask(__name__)
apiToken = "Bearer 2eyJhbGciOiJSUzUxMiIsImtpZCI6IjhEMzMzNTQyRUQ3RTY0RjY2OUEwNEREMzNEQTU1QTE0QjcwNjIzMEMiLCJ0eXAiOiJKV1QifQ"

@app.route("/printMessage",  methods = ['GET'])
def saveConfigToDatabase():
    try:
        message = request.get_json()
        if  request.content_type != "application/json":
            return json.dumps({'success':False, 'message':'Must be application/json'}), 400, {'ContentType':'application/json'}
        else:
            if apiToken == request.headers['Authorization']:
                return json.dumps({'message': json.dumps(message)}), 200, {'ContentType':'application/json'}
            else:
                return json.dumps({'success':False, 'message':'Invalid API Token'}), 401, {'ContentType':'application/json'}
    except Exception as e:
        return json.dumps({'success':False, 'message':str(e)}), 400, {'ContentType':'application/json'}

if  __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)