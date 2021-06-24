from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/dataentry", methods=["POST","GET"])
def submitData():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        
        name        = post_data.get('name'),
        department  = post_data.get('department')

        print(name)
        print(department)
        
        response_object['message'] ='Data added!'
        return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)