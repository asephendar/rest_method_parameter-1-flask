from flask import Flask, jsonify
from hackerrank import Find_Digits


app = Flask(__name__)


@app.route("/", methods=["GET"])
def view_tugas_FD():
    response = Find_Digits.findDigits(1012)
    
    return jsonify({"results" : response})

if __name__ == "__main__":
    app.run(debug=True)