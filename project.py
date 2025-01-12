### main function plus 3 additional functions (not nested)
from datetime import datetime, timedelta
from amadeus import Client, ResponseError

### generated from free amadeus account
amadeus = Client(
        client_id="AYVb3fOiA1iLGpN1uofiJUazbXQhzpFK",
        client_secret="Ykt5d7U4aXhoHqJS"
    )

### get valid airport code(three letters only)
def valid_iata(code):
    if len(code) != 3 or not code.isalpha():
        raise ValueError(f"Invalid IATA code: '{code}'")
    return True

### search api for flights
def flight_search(departure, arrival, departure_date, arrival_date):
    try:
        valid_iata(departure)
        valid_iata(arrival)
        datetime.strptime(departure_date, "%Y-%m-%d")
        datetime.strptime(arrival_date, "%Y-%m-%d")
        response= amadeus.shopping.flight_offers_search.get(originLocationCode=departure,destinationLocationCode=arrival,departureDate=departure_date,returnDate=arrival_date,adults=1)
        return response
    except ValueError as IncorrectInput:
        raise ValueError(str(IncorrectInput))
    except ResponseError as IncorrectInput:
        return None

### get dates near user_inputed date if no flights found for user_input
def get_date_range(departure_date, range_of):
    if not isinstance(departure_date, str):
        raise TypeError
    try:
        user_input_date = datetime.strptime(departure_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: '{departure_date}'. Please input 'YYYY-MM-DD'.")

    date_range = [user_input_date]
    for i in range(1, range_of + 1):
        date_range.append(user_input_date + timedelta(days=i))
        date_range.append(user_input_date - timedelta(days=i))
    formatted_dates = ([date.strftime("%Y-%m-%d") for date in date_range])
    return sorted(formatted_dates)

### display api results
def results(response, departure_date):
    output = []
    data = response.data if hasattr(response, "data") else response
    if data:
        output.append(f"Flights found for: {departure_date}")
        for flight in data:
            price = flight["price"]["total"]
            departure = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            arrival = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            output.append(f"Price: ${price}")
            output.append(f"Departure: {departure}")
            output.append(f"Arrival: {arrival}")

    else:
        output.append(f"No flights found for: {departure_date}")
    return "\n".join(output)

### get user_input for departure/ arrival location and date
def main():
    try:
        departure = input("Where are you leaving from? ")
        arrival = input("Going to? ")

        valid_iata(departure)
        valid_iata(arrival)

        departure_date = input("Departure date: ")
        arrival_date = input("Arrival date: ")

    ### flexible days +/- 1
        range_of = 1
        date_range = get_date_range(departure_date, range_of)

        for current_date in date_range:
            print(f"Searching for flights on {current_date} ")
            response = flight_search(departure, arrival, current_date, arrival_date)

            print(results(response, current_date))
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
