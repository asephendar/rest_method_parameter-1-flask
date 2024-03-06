from flask import Flask, jsonify, request
from hackerrank import Find_Digits
import json


app = Flask(__name__)


@app.route("/", methods=["GET"])
def view_tugas_FD():
    response = Find_Digits.findDigits(1012)
    
    return jsonify({"results" : response})

@app.route("/", methods=["POST"])
def add_tugas_FD():
    data = request.json["data"]
    response = Find_Digits.findDigits(data)
    hasil = json.dumps(response, indent=2)
    
    print("tipe data : ", type(data))
    print("tipe response: ", type(response))
    print("tipe json.dumps : ", type(hasil))
    print("tipe request.json : ", type(request.json))
    print("tipe jsonify : ", type(jsonify))
    print("tipe dict: ", type({"results" : response}))
    print("tipe f-str: ", type(f"{hasil}"))
    
    return jsonify({"results" : response})

@app.route("/", methods=["PUT"])
def update_tugas_FD():
    data = int(request.headers["data"])
    response = Find_Digits.findDigits(data)
    
    return {"results" : response}

@app.route("/<int:data>", methods=["PATCH"])
def update2_tugas_FD(data):
    data = int(data)
    response = Find_Digits.findDigits(data)
    
    return {"results" : response}

@app.route("/", methods=["DELETE"])
def delete_tugas_FD():
    data = int(request.args["data"])
    response = Find_Digits.findDigits(data)
    
    return f"Data {response} deleted successfully"

if __name__ == "__main__":
    app.run(debug=True)