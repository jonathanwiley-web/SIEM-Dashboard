# rules.py
from models import Log, Alert, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def run_rules():
    logs = session.query(Log).all()
    for log in logs:
        if "Failed login" in log.message:
            alert = Alert(rule_name="Brute Force Attempt",
                          description=f"Suspicious failed login detected: {log.message}",
                          severity="High")
            session.add(alert)
        elif "escalated privileges" in log.message:
            alert = Alert(rule_name="Privilege Escalation",
                          description=f"Admin privileges escalated: {log.message}",
                          severity="Critical")
            session.add(alert)
    session.commit()
    print("Rules executed.")

if __name__ == "__main__":
    run_rules()