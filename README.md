# **Flight Price Lookup** _by ChanceMess_ ✈️
## **Video Demo: 🎥**  <https://youtu.be/XBJLlWftCt8>
### **About:**
My python program is a price lookup tool for roundtrip flights. The program prompts the user for departing and arriving dates as well as the airport they're leaving from and the airport they'll be going to. It gives prices for the dates the user inputs as well as similar dates around the same time to help the user decide which is the best flight option. The program also gives layover airports, if any, just in case the user has a preference on their layover location.

### **Requirements:**
```
pip install datetime
pip install amadeus
pip install pytest
from amadeus import Client, ResponseError
from datetime import datetime, timedelta
```
### **API Key:**
```
amadeus =
        client_id="AYVb3fOiA1iLGpN1uofiJUazbXQhzpFK"
        client_secret="Ykt5d7U4aXhoHqJS"
```
### **How to Use:**
When you run the program, it will ask, "Where are you leaving from?" and "Going to?". The user inputs an IATA airport code in the form of three letters. Once the departure and arrival airport codes are entered, the program will prompt for departure date and arrival date. The user inputes in the ISO 8601 format (YYYY-MM-DD). Once the user inputs all of the information the program will output flight results with prices.
#### **Code Breakdown:**
##### **Valid Iata:**
This function checks to see if the user is inputting a correct airport code. The IATA or, The International Air Transport Association, abbreviates airports to three letters. My code checks that the user is inputting three letters, not less or more, and the code checks to see if the user inputs letters, not numbers or symbols.
##### **Flight Search:**
The flight search function takes the user input and checks it with the _amadeus_ flight search api to get the results. It takes a string of user inputed dates and converts to datetime that the api can use to lookup appropriate dates for the users flight. The program takes in user inputted dates written in the ISO 8601 format.
##### **Get Date Range:**
The get date range functions main goal is to get a range of dates one before and one after the user inputted date. Sometimes there's no flights for the user inputed dates so this makes sure it gets similar dates for the user. Or if the user is flexible on dates, the get date range function can show cheaper flights on the day before or after the user inputed dates.
##### **Results:**
The results function takes the information pinged from _amadeus_ and prints it in a readable format for the user. First it shows the price of the flight in USD, then it shows the departing airport, and lastly it shows the connecting airport if any. This makes it all easily digestable for the user. I wanted the program to show the prices first since this is probably the most important thing the user wants to take into consideration when shopping for flights.
#### **Testing the Code:**
```
from project import results, flight_search, get_date_range, valid_iata
from unittest.mock import MagicMock
from datetime import datetime, timedelta
import pytest
```
##### **Test Valid Iata:**
This test asserts that SAN (San Diego International Airport) and POA (Porto Alegre–Salgado Filho International Airport) are factual inputs and the result is True. The test also asserts that if the user just types in one letter, in this case "S", the test will result in False.
##### **Test Flight Search:**
This test takes in the input, "SAN", "POA", "2025-01-10", "2025-01-20", and asserts the result is not None. It also raises a ValueError if the date is not entered in the ISO 8601 (YYYY-MM-DD) format.
##### **Test Get Date Range:**
This test takes in the date, "2025-01-06" and uses DateTime's TimeDelta to add and subtract one day from the user inputed dates in order to get a date range. This test asserts that the result is what I inteded for the program as using range of 1 day to output dates so the user can decide on the best flight for them.
##### **Test Results:**
This test uses MagicMock to mock a hypothetical result the user might input. I found MagicMock by using a simple google search and I thought it would be a cool way to test this function. It asserts that the hypothetical user input is outputed in the correct format, making it easily digestable for the user.
