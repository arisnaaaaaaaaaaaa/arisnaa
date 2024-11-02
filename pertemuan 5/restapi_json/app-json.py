from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)
app.config["DEBUG"] = True

file_json = open("mahasiswa.json")

data = json.loads(file_json.read())

@app.route('/', methods = ['GET'])
def index():
    for dtmhs in data['mahasiswa']:
        print(f"Nama: {dtmhs['nama']}")
        print(f"Sosial Media:")
        print(f"- facebook: {dtmhs['social_media']['facebook']}")
        print(f"- twitter: {dtmhs['social_media']['twitter']}")
        print(f"- instagram: {dtmhs['social_media']['instagram']}")

        return make_response(jsonify({'Biodata' : data}), 200)
    
app.run()