from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ["GET"])
def hello():
    data = [{
        'nama': 'dimas anjay mabar',
        'pekerjaan' : 'penguasa dunia',
        'pesan' : 'kamu pasti takut ketemu evos galang'
    }]
    return make_response(jsonify({'data': data}), 200)

app.run

@app.route('/karyawan', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama' : 'dimas GET',
                'pekerjaan' : 'penguasa dunia',
                'usia' : '10',
            }]
        elif request.method == 'POST':
            data = [{
                'nama' : 'dimas POST',
                'pekerjan' : 'penguasa dunia',
                'usia' : '10',
            }]
        elif request.method == 'PUT':
            data = [{
                'nama' : 'dimas PUT', 
                'pekerjaan' : 'penguasa dunia',
                'usia' : '10'
            }]
        else:
            data = [{
                'nama' : 'alfin DELETE',
                'pekerjaan' : 'penguasa dunia',
                'usia' : '10',
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)

app.run()