class Station:
    def __init__(self, id_code, base_price):
        self.id_code = str(id_code)
        self.base_price = float(base_price)
        self.is_booked = False

    def __str__(self):
        if self.is_booked:
            return f"Station {self.id_code} - Booked"
        else:
            return f"Station {self.id_code} - Available"

class CoworkingSpace:
    def __init__(self, name):
        self.name = name
        self.zones = {}

    def add_station(self, zone_name, station_obj):
        if zone_name not in self.zones.keys():
            self.zones[zone_name] = []
        self.zones[zone_name].append(station_obj)

    def book_cheapest(self, zone_name):

        station_lowest_price = None
        for station in self.zones[zone_name]:
            if not station.is_booked:
                station_lowest_price = station
                break

        if station_lowest_price is None:
            return None
        else:
            for station in self.zones[zone_name]:
                if not station.is_booked and station.base_price < station_lowest_price.base_price:
                    station_lowest_price = station

            station_lowest_price.is_booked = True
            return station_lowest_price


def generate_report(space_obj):
    new_dictionary = {}

    for zones, list_station in space_obj.zones.items():
        total_number_of_stations = len(list_station)
        potential_revenue_of_zone = 0
        for station in list_station:
            potential_revenue_of_zone += station.base_price

        new_dictionary[zones] = (total_number_of_stations, potential_revenue_of_zone)

    return new_dictionary


if __name__ == "__main__":
    my_hub = CoworkingSpace("Tech Hub Lugano")

    # Setup data
    my_hub.add_station("OpenSpace", Station("OS-1", 25.0))
    my_hub.add_station("OpenSpace", Station("OS-2", 18.0))
    my_hub.add_station("MeetingRoom", Station("MR-1", 100.0))

    # Perform a booking
    res = my_hub.book_cheapest("OpenSpace")
    if res:
        print(f"Booked: {res.id_code}")  # Should be OS-2

    # Output report
    print("Final Report:", generate_report(my_hub))

