class FlightTable:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight_id, from_city, to_city, price):
        self.flights[flight_id] = (from_city, to_city, price)

    def search_by_city(self, city):
        matching_flights = [(flight_id, from_city, to_city, price) for flight_id, (from_city, to_city, price) in self.flights.items() if city in (from_city, to_city)]
        return matching_flights

    def search_by_from_city(self, from_city):
        matching_flights = [(flight_id, from_city, to_city, price) for flight_id, (f_city, to_city, price) in self.flights.items() if f_city == from_city]
        return matching_flights

    def search_between_cities(self, from_city, to_city):
        matching_flights = [(flight_id, f_city, t_city, price) for flight_id, (f_city, t_city, price) in self.flights.items() if f_city == from_city and t_city == to_city]
        return matching_flights

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for flight_id, from_city, to_city, price in flight_data:
        flight_table.add_flight(flight_id, from_city, to_city, price)

    print("Choose search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city: ")
        result = flight_table.search_by_city(city)
    elif choice == 2:
        from_city = input("Enter the source city: ")
        result = flight_table.search_by_from_city(from_city)
    elif choice == 3:
        from_city = input("Enter the source city: ")
        to_city = input("Enter the destination city: ")
        result = flight_table.search_between_cities(from_city, to_city)
    else:
        print("Invalid choice")

    if result:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight_id, from_city, to_city, price in result:
            print(f"{flight_id}\t\t{from_city}\t{to_city}\t{price}")
    else:
        print("No matching flights found.")

if __name__ == "__main__":
    main()