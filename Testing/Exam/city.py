def city(capital, country, population=''):
    if population:
        return f"{capital.title()} {country.title()}, population: {population}"
    else:
        return f"{capital.title()} {country.title()}"

print(city('bbb', 'ddd', 123))