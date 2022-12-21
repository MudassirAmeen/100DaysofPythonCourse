# Day 9

# Travel Log. This is the challange to make a funtion named add_new_country that will add one dictionary to the list named travel_log

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Now make funtion that will accept three parameters

countries = input("Which country you want to add ? ")
visits = int(input("How much visits you have done ? "))
city = input("Which cities you have visited ? ").split(",")


def add_new_country(country, visit, cities):
    travel_log.append({
        "country": country,
        "visits": visit,
        "cities": cities,
    })


add_new_country(country = countries, visit = visits, cities = city)
print(travel_log)
