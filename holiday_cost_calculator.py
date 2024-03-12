# Task 13 - User Defined Functions

# This program asks user to input holiday destination and calculates 
# flight cost depending on the city chosen, hotel cost depending on city
# and hotel chosen, and car rental cost depending on car chosen and number
# of days. Finally total cost for holiday is calculated using
# user defined functions and prints it 

import string

# Create Destinatons, hotels, cars as list 
city_list = ["Rome", "Paris", "Tenerife", "Cyprus", "Dubai"]
hotel_list = ["Hotel Plaza", "Hotel Hamilton", "Hotel Ritz", "Hotel Milano"]
car_list = ["Ayona", "Insight", "Corolla", "Jaguar"]

rent_days = 0
num_night = 0

# Nested dictionary to store hotels and tariffs for cities
city_hotels_tariffs = [
    {"city": "Rome", "hotels": {"Hotel Plaza": 250, "Hotel Hamilton": 300, 
                                "Hotel Ritz": 350, "Hotel Milano": 400}},
    {"city": "Paris", "hotels": {"Hotel Plaza": 300, "Hotel Hamilton": 400, 
                                "Hotel Ritz": 500, "Hotel Milano": 600}},
    {"city": "Tenerife", "hotels": {"Hotel Plaza": 200, "Hotel Hamilton": 300, 
                                    "Hotel Ritz": 400, "Hotel Milano": 500}},
    {"city": "Cyprus", "hotels": {"Hotel Plaza": 100, "Hotel Hamilton": 200, 
                                "Hotel Ritz": 300, "Hotel Milano": 400}},
    {"city": "Dubai", "hotels": {"Hotel Plaza": 400, "Hotel Hamilton": 500, 
                                "Hotel Ritz": 600, "Hotel Milano": 700}}
]

# Nested dictionary to store car rental charges for cities
city_car_rentals = [
    {"city": "Rome", "cars": {"Ayona": 20, "Insight": 30, "Corolla": 35, 
                            "Jaguar": 40}},
    {"city": "Paris", "cars": {"Ayona": 30, "Insight": 40, "Corolla": 50, 
                            "Jaguar": 60}},
    {"city": "Cyprus", "cars": {"Ayona": 20, "Insight": 30, "Corolla": 40, 
                                "Jaguar": 50}},
    {"city": "Tenerife", "cars": {"Ayona": 10, "Insight": 20, "Corolla": 30, 
                                "Jaguar": 40}},
    {"city": "Dubai", "cars": {"Ayona": 40, "Insight": 50, "Corolla": 60, 
                            "Jaguar": 70}}
]


def display_hotel(city_name):
        ''' Displays hotel tariff per night depending on city chosen'''
        if city_name == "Rome":
            print("Hotel Plaza: 250, Hotel Hamilton: 300, Hotel Ritz: 350, \
Hotel Milano: 400\n")
        elif city_name == "Paris":
            print("Hotel Plaza: 300, Hotel Hamilton: 400, Hotel Ritz: 500, \
Hotel Milano: 600\n")
        elif city_name == "Cyprus":
            print("Hotel Plaza: 200, Hotel Hamilton: 300, Hotel Ritz: 400, \
Hotel Milano: 500\n")
        elif city_name == "Tenerife":
            print("Hotel Plaza: 100, Hotel Hamilton: 200, Hotel Ritz: 300, \
Hotel Milano: 400\n")
        elif city_name == "Dubai":
            print("Hotel Plaza: 400, Hotel Hamilton: 500, Hotel Ritz: 600, \
Hotel Milano: 700\n")
        else:
            print("Invalid input.")


# Function to retrieve hotel price
def get_hotel_price(city_name, hotel_name):
    ''' Returns hotel tariff per night depending on city and hotel'''
    for city_info_dict in city_hotels_tariffs:
        if city_info_dict["city"] == city_name:
            hotels_dict = city_info_dict["hotels"]
            if hotel_name in hotels_dict:
                return hotels_dict[hotel_name]
            else:
                return None
    return None


def display_car(city_name):
        ''' Displays Car rental charges depending on city chosen'''
        if city_name == "Rome":
            print("Ayona: 20, Insight: 30, Corolla: 35, Jaguar: 40\n")
        elif city_name == "Paris":
            print("Ayona: 30, Insight: 40, Corolla: 50, Jaguar: 60\n")
        elif city_name == "Cyprus":
            print("Ayona: 20, Insight: 30, Corolla: 40, Jaguar: 50\n")
        elif city_name == "Tenerife":
            print("Ayona: 10, Insight: 20, Corolla: 30, Jaguar: 40\n")
        elif city_name == "Dubai":
            print("Ayona: 40, Insight: 50, Corolla: 60, Jaguar: 70\n")
        else:
            print("Invalid input.")


def get_car_rental(city_name, car_name):
    ''' Returns car rental price depending on city chosen and car make chosen'''
    for car_info_dict in city_car_rentals:
        if car_info_dict["city"] == city_name:
            cars_dict = car_info_dict["cars"]
            if car_name in cars_dict:
                return cars_dict[car_name]
            else:
                return None
    return None


# Create function to calculate hotel cost 
def hotel_cost(num_nights):
    ''' Returns hotel charges depending on hotel and number of nights'''
    hot_cost = 0
    hot_cost = num_nights * hotel_pernight
    return hot_cost


# Create function to calculate plane cost depending on city chosen
def plane_cost(city_flight):
    ''' Returns plane charges depending on the city chosen'''
    pl_cost = 0
    if city_flight == "Rome":
        pl_cost = 400
    elif city_flight == "Paris":
        pl_cost = 250
    elif city_flight == "Tenerife":
        pl_cost = 450
    elif city_flight == "Cyprus":
        pl_cost = 450
    elif city_flight == "Dubai":
        pl_cost = 500
    else:
        print("Invalid input.")
    return pl_cost


# Create function to calculate car rental charges
def car_rental(rental_days):
    ''' Returns car rental charges depending on car chosen and number of days'''
    car_cost = 0
    car_cost = rental_days * car_daily
    return car_cost


# Create function to calculate total charges
def total_cost(hot_cost, pl_cost, car_cost):
    ''' Returns total holiday cost '''
    tot_cost = 0
    tot_cost = hot_cost + pl_cost + car_cost
    return tot_cost

print("\nHello!\n")
print("Welcome to Python Travels!")
print()
print("Come holiday with us for an unforgettable experience!")
print()

# Ask user to input the destination city
city_flight = input("Please choose the city you would like to travel to: \
Rome / Paris/ Cyprus / Tenerife / Dubai: ")
city_flight = string.capwords(city_flight)

# Check if user input is in the city list
while city_flight not in city_list:
    print("\nInvalid input.\n")
    city_flight = input("Please choose the city you would like to travel to: \
Rome / Paris/ Cyprus / Tenerife / Dubai: ")
    city_flight = string.capwords(city_flight)

print(f"Thank you. Your chosen city is {city_flight}.") 
print("\nWould you like to book a Hotel for your stay? The following are \
hotels and tariff per night. \n")

hotel_selection = display_hotel(city_flight)

hotel_chosen = input("Please choose the hotel: ")
hotel_chosen = string.capwords(hotel_chosen)

# Check if user input is in the city list
while hotel_chosen not in hotel_list:
    print("\nInvalid input.\n")
    hotel_chosen = input("Please choose the hotel from the list above: ")
    hotel_chosen = string.capwords(hotel_chosen)

hotel_pernight = get_hotel_price(city_flight, hotel_chosen)
print()

# Use Try Except block to handle ValueError for num_night
try:
    num_night = input("\nHow many nights would you like to stay at the hotel? ")
    num_night = int(num_night)
except ValueError as ve:
    print(f"You entered '{num_night}' which is not a number.")
    num_night = int(input("\nHow many nights would you like to stay at the \
hotel? "))

# Give discount if number of nights is greater than 30
if num_night > 30:
    print("\nWhoa! You could be eligible for a discount! Please email to \
nightmares@pythontravels.com.")
else:
    print(f"\nThank you. Your hotel will be booked for {num_night} nights.") 

print("\nWhy not enhance your travel experience further by renting a car for \
the following charges (in Pounds) per day?\n")

car_display = display_car(city_flight)

car_chosen = input("\nPlease choose the car you would like to rent: ")
car_chosen = string.capwords(car_chosen)

# Check if user input is in the city list
while car_chosen not in car_list:
    print("Invalid input.\n")
    car_chosen = input("\nPlease choose the car from the list above: ")
    car_chosen = string.capwords(car_chosen)

car_daily = get_car_rental(city_flight, car_chosen)

# Use Try Except block to handle ValueError for rent_days
try:
    rent_days = input("\nPlease enter the number of days you would like to \
rent the car: ")
    rent_days = int(rent_days)
except ValueError as ve:
    print(f"\nYou entered '{rent_days}' which is not a number.")
    rent_days = int(input("\nPlease enter the number of days you \
would like to rent the car: "))

# Give discount if car rental days is greater than 30
if rent_days > 30 and rent_days < 100:
    print("\nWhoa! You could be eligible for a discount! Please email to \
timepass@pythontravels.com.")
elif rent_days > 100:
    print("\nWHOA WHOA! You could be better off buying a car rather than \
renting!")
else:
    print(f"\nThank you, Your car will be booked for {rent_days} days.") 

print("\nThe summary of your charges is as follows:")

# Calling user defined functions to calculate costs
flight_charges = plane_cost(city_flight)
print(f"\nYour flight charges to {city_flight} will be: £{flight_charges}")

hotel_charges = hotel_cost(num_night)
print(f"Your hotel charges at {hotel_chosen} for {num_night} nights will be: \
£{hotel_charges}")

car_charges = car_rental(rent_days)
print(f"Your {car_chosen} rental charges for {rent_days} days will be:\
£{car_charges}")

total_charges = total_cost(flight_charges, hotel_charges, car_charges)
print(f"\nThe total charges will be: £{total_charges}")

booking_conf = input("\nWould you like to go ahead with your booking? \
Enter yes/no: ")
booking_conf = booking_conf.lower()

if booking_conf == "yes":
    print("\nThank you for booking your holiday with Python Travels. Have a \
good day!\n")
elif booking_conf == "no":
    print("\nHmmm Ok. Good luck finding better holiday prices than us!\n")
else:
    print("\nYou too. Thank you for visiting Python Travels! Have a good \
day!\n")


