from project import results, flight_search, get_date_range, valid_iata
from unittest.mock import MagicMock
from datetime import datetime, timedelta
import pytest

def main():
    test_flight_search()
    test_results()
    test_get_date_range()
    test_valid_iata()

def test_flight_search():
    result = flight_search("SAN", "POA", "2025-01-10", "2025-01-20")
    assert result is not None

    with pytest.raises(ValueError, match="does not match format '%Y-%m-%d'"):
        flight_search("SAN", "POA", "January 10, 2025", "2025-01-20")

def test_results():
    mock_response = [{"price": {"total": "1500.00"}, "itineraries": [{"segments": [{"departure": {"iataCode": "SAN"}, "arrival": {"iataCode": "POA"}}]}]}]
    departure_date = "2025-01-10"
    output = results(mock_response, departure_date)
    assert "Price: $1500.00" in output
    assert "Departure: SAN" in output
    assert "Arrival: POA" in output

def test_get_date_range():
    departure_date = "2025-01-06"
    range_of = 1

    inputed_date = datetime.strptime(departure_date, "%Y-%m-%d")
    outputed_dates = [(inputed_date - timedelta(days=1)).strftime("%Y-%m-%d"), departure_date, (inputed_date + timedelta(days=1)).strftime("%Y-%m-%d")]

    result = get_date_range(departure_date, range_of)

    assert result == outputed_dates
    assert isinstance(result, list)
    assert all(isinstance(date, str) for date in result)

def test_valid_iata():
    assert valid_iata("SAN") is True
    assert valid_iata("POA") is True
    with pytest.raises(ValueError, match="Invalid IATA code: 'S'"):
        valid_iata("S")


if __name__ == "__main__":
    main()
