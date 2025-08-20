# app.py
from flask import Flask, render_template
from models import Log, Alert, engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def dashboard():
    logs = session.query(Log).order_by(Log.timestamp.desc()).limit(20).all()
    alerts = session.query(Alert).order_by(Alert.timestamp.desc()).limit(20).all()
    return render_template("dashboard.html", logs=logs, alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)