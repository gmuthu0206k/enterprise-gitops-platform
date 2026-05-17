from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Enterprise GitOps Application Running on EKS"


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
