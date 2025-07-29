def analyze_flight_data(origin, destination, flight_data):
    """
    Analyze flight data and generate insights + chart info.
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    
    total_flights = sum(flight_data)
    peak_month_index = flight_data.index(max(flight_data))
    avg_flights = total_flights // 12

    insights = [
        f"Total annual flights: {total_flights}",
        f"Peak travel month: {months[peak_month_index]} with {flight_data[peak_month_index]} flights",
        f"Average monthly flights: {avg_flights}",
        f"Demand is {'very high' if flight_data[peak_month_index] > 400 else 'high' if flight_data[peak_month_index] > 300 else 'moderate'} during peak season",
        f"Best time to book: {months[(peak_month_index + 6) % 12]} (6 months before peak)"
    ]

    chart_data = {
        "labels": months,
        "values": flight_data,
        "label": f"Flights from {origin} to {destination}"
    }

    return insights, chart_data
