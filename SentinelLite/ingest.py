# ingest.py
from models import Log, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, UTC
import random

Session = sessionmaker(bind=engine)
session = Session()

def generate_logs():
    sources = ["auth.log", "nginx", "app1"]
    messages = [
        "Failed login attempt from 192.168.1.100",
        "User admin escalated privileges",
        "Connection from suspicious IP 203.0.113.5",
        "Normal user login"
    ]
    levels = ["INFO", "WARNING", "ERROR"]

    log = Log(
        source=random.choice(sources),
        message=random.choice(messages),
        level=random.choice(levels),
        timestamp=datetime.now(UTC)
    )
    session.add(log)
    session.commit()
    print(f"Inserted: {log.message}")

if __name__ == "__main__":
    for _ in range(10):
        generate_logs()