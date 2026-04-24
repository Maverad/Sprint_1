world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions.update({2022: 'Аргентина'})

for key, value in world_champions.items():
    print(key, '-', value)

country = 'Италия'

if country in world_champions.values():
    print(country, 'становилась чемпионом мира по футболу в 21 веке!')
else:
    print(country, 'не выигрывала чемпионат мира по футболу в 21 веке.')

