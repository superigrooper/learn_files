# city
def city_country(city, country):
    data = f"{city} {country}"
    return data.title()

while True:
    print("\nГорода и страны.")
    print("(для завершения нажмите 'q')")

    city = input("\nВведи название города: ")
    if city == 'q':
        break

    country = input("Введи название страны: ")
    if country == 'q':
        break
    print(city_country(city, country))