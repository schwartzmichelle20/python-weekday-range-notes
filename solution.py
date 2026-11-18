from datetime import date, timedelta

def solve(value):
    return [d.isoformat() for d in (date.fromisoformat(value[0]) + timedelta(days=i) for i in range((date.fromisoformat(value[1])-date.fromisoformat(value[0])).days)) if d.weekday() < 5]
