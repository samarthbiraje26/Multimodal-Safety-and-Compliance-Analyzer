emergencies = []

def add_emergency(event):
    emergencies.insert(0, event)  # latest on top
    return event

def get_all_emergencies():
    return emergencies[:50]  # limit for dashboard