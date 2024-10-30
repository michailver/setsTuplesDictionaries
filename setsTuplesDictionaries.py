# # 1. Sukurkite dictionary studento duomenims saugoti. Į šį dictionary sudėkite
# # tokias savybes su reikšmėmis: vardas, pavardė, amžius, studijų programa,
# # atsiskaitytų kreditų skaičius, pažymiai, amžius, ūgis, kelintame kurse
# # mokosi, kurioje mokykloje mokosi. Šiuos duomenis galite grupuoti į
# # vidinius dictionary arba visus išrašyti atskirai. Išveskite šią informaciją per
# # vieną print(). Taip pat, pamėginkite išvesti atskirose eilutėse tris
# # skirtingas pasirinktas savybes.
# studentas = {
#     'vardas': 'Petras',
#     'pavarde': 'Petrauskas',
#     'amzius': 22,
#     'kur_mokosi': {
#         'mokykla': 'KTU',
#         'studiju_programa': 'Multimedijos technologijos',
#         'kursas': 3
#     },
#     'pazymiai': [7, 8, 9, 6, 8, 5, 4]
# }
# print(f'vardas:{studentas['vardas']} studijoja {studentas['kur_mokosi']['mokykla']}')
from calendar import prcal

# # print('##############################################################################################################')
# # 2. Sukurkite dictionary informacijai apie filmą saugoti. Į šį dictionary sudėkite
# # tokias savybes su reikšmėmis: pavadinimas, režisierius, biudžetas, kiek
# # uždirbo pinigų po išleidimo, žanras, trukmė, išleidimo metai, aktorių
# # sąrašas (masyvas su jų vardais ir pavardėmis). Išveskite šio dictionary
# # informaciją. Paskaičiuokite ir išveskite šio filmo pelną (uždarbis -
# # biudžetas). Išveskite kiek filme dalyvavo aktorių (jų kiekis). Paskaičiuokite
# # kiek filmui yra metų (dabartinius metus tiesiog galite įrašyti rankomis arba
# # panaudoti datetime.date.today().year funkciją, pačiame failo viršuje
# # reikės nurodyti import datetime).
# import datetime
# film = {
#     "title": "Inception",
#     "director": "Christopher Nolan",
#     "budget": 200000000,
#     "revenue": 828288329,
#     "genre": "Sci-Fi",
#     "runtime": 148,
#     "release_year": 2010,
#     "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page", "Tom Hardy"]
# }
# # Paskaičiuokite ir išveskite šio filmo pelną (uždarbis - biudžetas).
# print('Profit: ',film['revenue']-film['budget'])
# # Išveskite kiek filme dalyvavo aktorių(jų kiekis)
# print('Actors count: ', len(film["actors"]))
# # Paskaičiuokite kiek filmui yra metų
# print('Movie age: ', datetime.date.today().year - film['release_year'] )

# print('##############################################################################################################')
# # 3. Sukurkite du dictionary dviejų knygų informacijai saugoti. Kiekviename
# # dictionary nurodykite tokias savybes su reikšmėmis: pavadinimas,
# # autorius, žanras, kaina, puslapių kiekis, skyrių sąrašas (masyvas su
# # pavadinimais), išleidimo metai, ar knygą galima rasti knygynuose.
# # Išveskite šių knygų informaciją. Išveskite kuri knyga plonesnė (turi mažiau
# # puslapių), bei kurioje knygoje yra daugiau skyrių. Paskaičiuokite, jeigu
# # pigesnės knygos kainą padvigintumėte, ar ji jau būtų brangesnė už kitą
# # knygą?
# book1 = {
#     "title": "The Silent American",
#     "author": "Graham Greene",
#     "genre": "Novel",
#     "price": 12.99,
#     "pages": 256,
#     "chapters": ["Introduction", "Part One", "Part Two", "Conclusion"],
#     "year": 1955,
#     "available_in_bookstore": True
# }
#
# book2 = {
#     "title": "1984",
#     "author": "George Orwell",
#     "genre": "Dystopian",
#     "price": 9.99,
#     "pages": 328,
#     "chapters": ["Book One", "Book Two", "Book Three", "Book Four", "Conclusion"],
#     "year": 1949,
#     "available_in_bookstore": False
# }
# # Išveskite kuri knyga plonesnė (turi mažiau puslapių), bei kurioje knygoje yra daugiau skyrių.
# if book1['pages'] > book2['pages']:
#     thinner_book_title = f'"{book2['title']}" yra plonesne'
# elif book1['pages'] < book2['pages']:
#     thinner_book_title = f'"{book1['title']}" yra plonesne'
# else:
#     thinner_book_title = f'"{book2['title']}" turi tiekpat puslapiu kiek ir knyga "{book1['title']}"'
#
# if len(book1['chapters']) < len(book2['chapters']):
#     chapter_count = f'"{book2['title']}" turi daugiau skiriu'
# elif len(book1['chapters']) > len(book2['chapters']):
#     chapter_count = f'"{book1['title']}" turi daugiau skiriu'
# else:
#     chapter_count = f'"{book2['title']}" turi tiekpat skyriu kiek ir knyga "{book1['title']}"'
#
# print(f'knyga {thinner_book_title} ir knyga {chapter_count}')
# # Paskaičiuokite, jeigu pigesnės knygos kainą padvigintumėte, ar ji jau būtų brangesnė už kitą knygą?
# if book1['price'] > book2['price']:
#     new_price = book2['price']*2
#     if book1['price'] < new_price:
#         print('Padvigubiant pigenes knygos kaina, ji taptu brangesne uz kita')
#     else:
#         print('Padvigubiant pigenes knygos kaina, ji ne taptu brangesne uz kita')
# elif book1['price'] < book2['price']:
#     new_price = book1['price']*2
#     if book2['price'] < new_price:
#         print(f'Padvigubiant pigenes knygos kaina, ji taptu brangesne uz kita')
#     else:
#         print('Padvigubiant pigenes knygos kaina, ji ne taptu brangesne uz kita')
# else:
#     print('kainos ligios')
# print(f'book1 kaina: {book1['price']}, book2 kaina: {book2['price']}, padvigubiant pigiausia: {new_price}')

# print('##############################################################################################################')
# # 4. Sukurkite tris dictionary prekių duomenims saugoti. Kiekviename
# # dictionary sudėkite šias savybes su reikšmėmis: pavadinimas, kaina,
# # savikaina, kodas, turimas kiekis sandėlyje, siuntimui dėžės matmenys (x, y,
# # z ašys). Išveskite visų trijų prekių informaciją. Išveskite visų prekių kainas
# # vienoje eilutėje (pirma prekė kainuoja - ..., antra prekė kainuoja - ..., ir t.t.).
# # Raskite ir išveskite kuri prekė yra brangiausia (jos pavadinimą ir kainą
# # arba visą rastos prekės informaciją). Raskite ir išveskite atskirose eilutėse
# # kiekvienos prekės dėžės tūrį. Raskite ir išveskite atskirose eilutėse
# # kiekvienos prekės pelningumą ((kaina - savikaina) * kiekis
# # sandėlyje).
# product1 = {
#     "name": "Smartphone",
#     "price": 399.99,
#     "cost": 250.00,
#     "code": "TEL123",
#     "quantity_in_stock": 100,
#     "box_dimensions": {"x": 15, "y": 8, "z": 2}
# }
#
# product2 = {
#     "name": "Headphones",
#     "price": 59.99,
#     "cost": 30.00,
#     "code": "AUS456",
#     "quantity_in_stock": 50,
#     "box_dimensions": {"x": 10, "y": 5, "z": 1}
# }
#
# product3 = {
#     "name": "Laptop",
#     "price": 1299.99,
#     "cost": 800.00,
#     "code": "KOM789",
#     "quantity_in_stock": 20,
#     "box_dimensions": {"x": 35, "y": 25, "z": 5}
# }
#
# # Išveskite visų prekių kainas vienoje eilutėje (pirma prekė kainuoja - ..., antra prekė kainuoja - ..., ir t.t.).
# print (f'pirma prekė kainuoja - {product1['price']}, antra prekė kainuoja - {product2['price']}, trecia preke kainuoja = {product3['price']}')
# # Raskite ir išveskite kuri prekė yra brangiausia (jos pavadinimą ir kainą arba visą rastos prekės informaciją).
# warehouse = [product1, product2, product3]
# price = warehouse[0]['price']
# expensive_product_name = ''
# for product in warehouse:
#     if product['price'] >= price:
#         price = product['price']
#         expensive_product_name = product['name']
# print(f'brangiausiai preke: {expensive_product_name}, jo kaina: {price}')
# print('#'*50)
# # Raskite ir išveskite atskirose eilutėse kiekvienos prekės dėžės tūrį.
# for product in warehouse:
#     volume = product['box_dimensions']['x']*product['box_dimensions']['y']*product['box_dimensions']['z']
#     print(f'produktui {product['name']} dezes turis yra: {volume} cm3')
# print('#'*50)
# # Raskite ir išveskite atskirose eilutėse kiekvienos prekės pelningumą ((kaina - savikaina) * kiekis sandėlyje).
# for product in warehouse:
#     profitability = (product['price'] - product['cost'])*product['quantity_in_stock']
#     print(f'produktui {product['name']} pelningumą yra: {round(profitability,2)} pinigu')
# print('#'*50)
# print('##############################################################################################################')
# # 5. Sukurkite dictionary automobilio duomenims saugoti. Į šį dictionary
# # savybes su reikšmėmis sukelkite, po to kai sukursite tuščią dictionary (14-
# # as pavyzdys). Sudėkite šias savybes su reikšmėmis: markė, modelis, rida,
# # gamybos metai, spalva, darbinis tūris, ar daužta, ar parduodama. Išveskite
# # visą automobilio informaciją. Paskaičiuokite ir išveskite kiek automobiliui
# # yra metų (rankomis įrašykite dabartinius metus arba panaudokite
# # datetime.date.today().year funkciją, pačiame failo viršuje reikės
# # nurodyti import datetime). Paskaičiuokite ir išveskite kiek vidutiniškai
# # per metus yra nuvažiavęs automobilis (jeigu viso nuvažiavo 300 kilometrų,
# # o automobiliui yra 2 metai, tai per metus vidutiniškai gaunasi 150 km.).
#
# car = {}
#
# car["make"] = "Toyota"
# car["model"] = "Corolla"
# car["kilometers"] = 120000
# car["year"] = 2015
# car["color"] = "silver"
# car["engine_size"] = 1.6
# car["has_accidents"] = True
# car["for_sale"] = False
# # Paskaičiuokite ir išveskite kiek automobiliui yra metų.
# import datetime
# car_age = datetime.date.today().year - car['year']
# print('Car age: ', datetime.date.today().year - car['year'])
#
# # Paskaičiuokite ir išveskite kiek vidutiniškai per metus yra nuvažiavęs automobilis
# print ('Average kilometers by year: ',round(car['kilometers']/car_age,0))

# print('##############################################################################################################')
# 6. Sukurkite savo norimą dictionary(-us). Kiekviename sudėkite bent 5
# savybes su reikšmėmis (reikšmes galite įdėti ir atskirai). Išveskite
# informaciją. Pagalvokite ką dar galite su šiuo dictionary atlikti (paskaičiuoti
# ir pan.) ir tai padarykite.
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"]
}
book = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "genre": "Fantasy",
    "pages": 1178,
    "published_year": 1954,
    "is_read": False
}
print(person["first_name"] + ' ' + person["last_name"])
import datetime
if book['is_read']:
    print('padaryti betka: ',datetime.date.today().year - person['age'])
else:
    book['author'] = person["first_name"] + ' ' + person["last_name"]
    print(book)

# 7. Susikurkite dictionary informacijai apie knygyną saugoti. Į šį dictionary
# sudėkite tokias savybes su reikšmėmis: pavadinimas, adresas, plotas (kv.
# m.), kiek turi knygų, darbo valandos, ar atidarytas. Išveskite šio knygyno
# dictionary raktus su reikšmėmis.
# 8. Susikurkite du dictionary, dviejų studentų informacijai saugoti. Abiejuose
# dictionary sudėkite šias savybes su reikšmėmis: vardas ir pavardė, studijų
# programos pavadinimas, pažymiai. Raskite abiejų studentų pažymių
# vidurkius. Išveskite abiejų studentų informaciją, bei pažymių vidurkius.
# Raskite ir išveskite, kurio studento pažymių vidurkis yra didesnis ir
# išveskite jo vardą su pavarde.