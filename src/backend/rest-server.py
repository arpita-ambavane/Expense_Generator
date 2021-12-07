##
from flask import Flask, request, Response, jsonify
import platform
import io, os, sys
import pika, redis
#import hashlib, requests
import json
import pickle
import platform
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from db import *
from flask_cors import CORS
app = Flask(__name__)



# Initialize the Flask application
app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "hvhvgcgc675765bhbj"  # Change this!
jwt = JWTManager(app)

##
## Configure test vs. production
##



@app.route('/api/auth/signup', methods=['POST'])
def signup():
    try:

        # enqueueDataToLogsExchange('Into fetch prices api',"info")

        data = request.get_json()
        print("-------Data-------" + str(data))

        #product = data['product_name']
        #final_output = start_scraping(product)
        response = insert_customer(data)

        # enqueueDataToLogsExchange('Fetch prices api executed succesfully',"info")

        return Response(response=json.dumps(response), status=200, mimetype="application/json")
        
    except Exception as e:
        #enqueueDataToLogsExchange('Error occured in api /api/auth/signup','info')
        return Response(response="Something went wrong!", status=500, mimetype="application/json")


@app.route('/api/auth/signin', methods=['POST'])
def signin():
    try:

        # enqueueDataToLogsExchange('Into fetch prices api',"info")

        data = request.get_json()
        print("-------Data-------" + str(data))
        email = request.json.get("username",None)
        password = request.json.get("password",None)
        #calling db function
        response = search_customer(data)
        #print(response)
        
        if response != 'Incorrect username/password!':
            print("hi")
            access_token = create_access_token(identity=email)
            #print(access_token)

        response.update({'accessToken': access_token})
        # enqueueDataToLogsExchange('Fetch prices api executed succesfully',"info")
        print("Response:")
        print(response)
        return Response(response=json.dumps(response), status=200, mimetype="application/json")
        #return make_response(jsonify(response=response), 201)
        
    except Exception as e:
        #enqueueDataToLogsExchange('Error occured in api /api/auth/signin','info')
        return Response(response="Something went wrong!", status=500, mimetype="application/json")
    

@app.route('/api/upload', methods=['POST'])
def handle_form():
    print("Posted file: {}".format(request.files['file']))
    file = request.files['file']
    #print(type(file))
    print(request.form['category'])
    print(request.form['username'])
    return ""



# start flask app
app.run(host="0.0.0.0", port=5000)
