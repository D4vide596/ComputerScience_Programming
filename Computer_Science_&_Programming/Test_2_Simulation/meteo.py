import csv, pickle

def create_station_dict(row):
    return {
        "location": row[0],
        "altitude": int(row[1])
    }

def get_stations_by_canton(file_path):
    cantons = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)

        for row in reader:
            cantons_name = row[4]
            station_info = create_station_dict(row)
            if cantons_name not in cantons:
                cantons[cantons_name] = []
            cantons[cantons_name].append(station_info)
    return cantons

def save_to_pickle(station_list, filename):
    with open(filename, 'wb') as p_file:
        pickle.dump(station_list, p_file)
        print(f"Successfully saved {len(station_list)} stations to {filename}")

if __name__ == '__main__':
    weather_data = get_stations_by_canton("meteoswiss.csv")
    if "TI" in weather_data:
        ticino_stations = weather_data['TI']
        print("Stations in Ticino:", ticino_stations)
        save_to_pickle(ticino_stations, 'ticino.pkl')
    else:
        print("No stations found for Canton TI.")

