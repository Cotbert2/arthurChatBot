import flask
from flask_cors import CORS
import processor

#denerate a json response key = reponse, value = data
def generate_response(data):
    return flask.jsonify({'response': data})


#api definition

#endpoint for the api
app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

@app.route('/api/', methods=['GET'])
def hello_world_1():
    return 'api endpoint'


#get body of post reques to /api/newMessage
@app.route('/api/newMessage', methods=['POST'])
def new_message():
    data = flask.request.json
    #access to inpuData json key
    data = data['inputData']
    print(data)
    return generate_response(processor.reponse(data))

#run the app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)