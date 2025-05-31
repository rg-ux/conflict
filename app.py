from flask import Flask,jsonify
import json

app=Flask(__name__)

@app.route("/")
def home():
    print ('Hey the list is returned')
    with open('data.json') as file:
        data = json.load(file)  # read and parse the file into Python list
    return jsonify(data)        # convert Python list into JSON response


if __name__ == '__main__':
    app.run(debug=True)