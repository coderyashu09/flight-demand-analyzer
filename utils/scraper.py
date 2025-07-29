import random

def fetch_flight_data(origin, destination):
    """
    Simulate fetching 12 months of flight data.
    Replace with a real API call if needed.
    """
    # Simulate monthly flight counts between 50 and 500
    flight_data = [random.randint(50, 500) for _ in range(12)]
    return flight_data
