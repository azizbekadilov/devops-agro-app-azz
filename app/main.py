from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
requests_total = Counter("requests_total", "Total HTTP requests", ["path"])

@app.get("/")
def home():
    requests_total.labels(path="/").inc()
    return "Agro App is running!"

@app.get("/health")
def health():
    requests_total.labels(path="/health").inc()
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
