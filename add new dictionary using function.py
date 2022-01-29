# nested dictionary
travel_log=[
    {
        "country":"France",
        "city_visited":["paris","djong"],
        "total_travel":20
    },
    {
        "Country":"Germany",
        "city_visited":["Berlin","hamburg"],
        "total_travel":12}]
def add_new_country(country_visited,city_visited,travel_time):
    new_country={}
    new_country["country"]=country_visited
    new_country["city_visited"]=city_visited
    new_country["total_travel"]=travel_time
    travel_log.append(new_country)

add_new_country("Russia",["moscow","petersber"],3)
print(travel_log)