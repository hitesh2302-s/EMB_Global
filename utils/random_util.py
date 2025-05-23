import random
from datetime import datetime

def generate_unique_mrn():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_part = random.randint(100, 999)
    return f"{timestamp}{random_part}"
