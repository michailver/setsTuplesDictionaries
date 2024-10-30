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
from getpass import fallback_getpass

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

# # print('##############################################################################################################')
# # 6. Sukurkite savo norimą dictionary(-us). Kiekviename sudėkite bent 5
# # savybes su reikšmėmis (reikšmes galite įdėti ir atskirai). Išveskite
# # informaciją. Pagalvokite ką dar galite su šiuo dictionary atlikti (paskaičiuoti
# # ir pan.) ir tai padarykite.
# person = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 30,
#     "city": "New York",
#     "hobbies": ["reading", "coding", "hiking"]
# }
# book = {
#     "title": "The Lord of the Rings",
#     "author": "J.R.R. Tolkien",
#     "genre": "Fantasy",
#     "pages": 1178,
#     "published_year": 1954,
#     "is_read": False
# }
# print(person["first_name"] + ' ' + person["last_name"])
# import datetime
# if book['is_read']:
#     print('padaryti betka: ',datetime.date.today().year - person['age'])
# else:
#     book['author'] = person["first_name"] + ' ' + person["last_name"]
#     print(book)
# print('##############################################################################################################')
# # 7. Susikurkite dictionary informacijai apie knygyną saugoti. Į šį dictionary
# # sudėkite tokias savybes su reikšmėmis: pavadinimas, adresas, plotas (kv.
# # m.), kiek turi knygų, darbo valandos, ar atidarytas. Išveskite šio knygyno
# # dictionary raktus su reikšmėmis.
# bookstore = {
#     "name": "Knygų pasaulis",
#     "address": "Vilniaus g. 25, Vilnius",
#     "area": 150,  # kvadratiniai metrai
#     "book_count": 5000,
#     "working_hours": "9:00 - 21:00",
#     "is_open": True
# }
# for key, value in bookstore.items():
#     print (f'key: {key}, | value: {value}')

# print('##############################################################################################################')
# # 8. Susikurkite du dictionary, dviejų studentų informacijai saugoti. Abiejuose
# # dictionary sudėkite šias savybes su reikšmėmis: vardas ir pavardė, studijų
# # programos pavadinimas, pažymiai.
# def grade_avg (grades):
#     total = sum(grades)
#     count = len(grades)
#     return round(total/count,2)
#
# def print_dict (dict_name):
#     for key, value in dict_name.items():
#         print (f'{key}: {value}')
#
# student1 = {
#     "first_name": "Jonas",
#     "last_name": "Jonaitis",
#     "program": "Computer Science",
#     "grades": [8, 9, 10, 7]
# }
# student2 = {
#     "first_name": "Petras",
#     "last_name": "Petraitis",
#     "program": "Business Administration",
#     "grades": [7, 8, 9, 6, 5, 9]
# }
# # Raskite abiejų studentų pažymių vidurkius.
# student1['grade_avg'] = grade_avg(student1["grades"])
# student2['grade_avg'] = grade_avg(student2["grades"])
# print('st1 avg: ', student1['grade_avg'])
# print('st2 avg: ', student2['grade_avg'])
# print('X'*10)
# # Išveskite abiejų studentų informaciją, bei pažymių vidurkius.
# print_dict(student1)
# print_dict(student2)
# print('X'*10)
# # Raskite ir išveskite, kurio studento pažymių vidurkis yra didesnis ir išveskite jo vardą su pavarde.
# stud_with_max_avg = ''
# if student1['grade_avg'] > student2['grade_avg']:
#     stud_with_max_avg = student1
# elif student1['grade_avg'] < student2['grade_avg']:
#     stud_with_max_avg = student2
# else:
#     print('Vidurkiai vienuodi')
# if stud_with_max_avg != '':
#     print(f'shitas vidurkis didziausia: {stud_with_max_avg['grade_avg']}.\n'
#           f'Studento vardas: {stud_with_max_avg['first_name']} {stud_with_max_avg['last_name']}')
# print('##############################################################################################################')
# # 9. Susikurkite dictionary, kuriame būtų nurodytos prekės ir turimi kiekiai, t.y.
# # raktas yra prekės pavadinimas ir reikšmė yra turimas prekės kiekis, o visa
# # tai saugoma viename dictionary (panašu į 29 pavyzdį). Išveskite visą
# # turimą dictionary informaciją gražiai suformatuotai, pvz: '- Prekės
# # "Pieštukas" liko 132 vnt.' ir tai padaryti atskirose eilutėse. Taip pat, raskite
# # ir išveskite visų prekių bendrą turimą kiekį (sudėti visus turimus kiekius),
# # kiekių vidurkį (kiek vidutiniškai turima prekių). O tos prekės kurios likę
# # mažiausiai vienetų išvesti pavadinimą ir kiekį.
#
# products = dict(
#             orange=25.0,
#             kiwi=88.99,
#             avocado=10.0,
#             tomatos=99.5,
#             banana=150.0,
#             aplle=50.25,
#             carot=10.0 )
# total_count = 0
# min_quantity = min(products.values())
# min_quantity_products = {}
#
# for key, value in products.items():
#     # print(f'{key}: {value}')
#     print(f'- Prekės "{key}" liko {value} vnt.')
#     if value == min_quantity:
#         min_quantity_products[key] = value
#     total_count += value
# print('---'*50)
# print(f'i6viso yra: {total_count}, Vidurkis {round(total_count/len(products),2)}')
# print('---'*50)
# print (f'Maziausiai liko:')
# for key, value in min_quantity_products.items():
#     print (f'\t{key}: {value} vnt')

# # print('##############################################################################################################')
# # 10.Susikurkite dictionary darbuotojo informacijai saugoti. Nurodykite tokias
# # savybes: vardas ir pavardė, telefonas, profesija, etatas, atlyginimas. Taip
# # pat, sukurkite dar vieną darbuotojo dictionary, tačiau nenurodykite 1-os
# # ar 2-ų savybių, pvz, praleiskite profesiją.
# employee1 = {
#     "first_name": "Jonas",
#     "last_name": "Jonaitis",
#     "phone_number": "+37061234567",
#     "profession": "Programuotojas",
#     "position": "Vyresnysis",
#     "salary": 2500,
#     "test": "aaa"
# }
# employee2 = {
#     "first_name": "Petras",
#     "last_name": "Petraitis",
#     "phone_number": "+37069876543",
#     "position": "Projektų vadovas",
#     "salary": 3000
# }
# # Parašykite tokią programą, kuri galėtų išsiaiškinti kurios(-ių) savybių nėra antrame dictionary, kurios yra
# # pirmame, pvz jeigu nėra profesijos, tai programa išsiaiškintų, kad nėra nurodyta profesija antrame dictionary.
# keys_list1 = employee1.keys()
# print(type(keys_list1))
# if(employee1.keys() == employee2.keys()):
#     print ("Yes, employee1 and employee2 are same")
# else:
#     print("No, employee1 and employee2 are not same")
#     not_exist = []
#     for key1 in employee1.keys():
#         print(key1, end='')
#         found = False
#         for key2 in employee2.keys():
#             if key2 == key1:
#                 found = True
#                 break
#         if found:
#             print('\tFound')
#         else:
#             print('\tNot Exist')
#             not_exist.append(key1)
#
# # Padarykite taip, kad vartotojas turėtų galimybę suvesti trūkstamas savybes.
# print ('***'*20)
# if len(not_exist)>0:
#     print("Trūksta:", end=" ")
#     for name in not_exist:
#         print(name, end=" ")
#     print()
#     addAnswer = input('Ar noretumete jos sukurti (t/n)?: ').lower()
#     if addAnswer == 't':
#         for name in not_exist:
#             employee2[name] = input(f'savibes {name} reiksme:')
# print(employee2)


# # # print('##############################################################################################################')
# # 11.Kaimynystėje yra trys kepyklos, apie kiekvieną yra žinoma ši informacija:
# # pavadinimas; darbuotojų kiekis; adresas; praeitos savaitės iškeptų kepinių
# # kiekiai (sąrašas su 7-iais elementais, kur nurodyti atskiri kepinių kiekiai).
# # Susikurkite dictionaries kiekvienai kepyklai.
# bakery1 = {
#     "name": "Duonos Kepyklėlė",
#     "address": "Vilniaus g. 123",
#     "employees": 15,
#     "weekly_baked_goods": [100, 250, 150, 200, 180, 120, 90]
# }
#
# bakery2 = {
#     "name": "Skanaus Kvapas",
#     "address": "Kauno g. 456",
#     "employees": 8,
#     "weekly_baked_goods": [80, 220, 160, 190, 170, 110, 85]
# }
#
# bakery3 = {
#     "name": "Grūdo Namai",
#     "address": "Klaipėdos g. 789",
#     "employees": 12,
#     "weekly_baked_goods": [120, 280, 150, 210, 190, 130, 100]
# }
# # Jeigu vienas kepinys parduodamas už 1.5 euro, raskite kuri kepykla galėjo būti pelningiausia.
# # Taip pat, išsiaiškinkite kiek vidutiniškai kiekviena kepykla per dieną pagamina kepinių, raskite kurios kepyklos vidurkis mažiausias.
# def profit_count (sales):
#     return sum(sales)*1.5
#
# def day_prod_avg_by_week (sales):
#     return sum(sales)/7
#
# bakerys = [bakery1, bakery2, bakery3]
#
# max_week_sales = profit_count(bakery1['weekly_baked_goods'])
# max_week_sales_name = bakery1['name']
#
# min_prod_avg_by_week = day_prod_avg_by_week(bakery1['weekly_baked_goods'])
# min_prod_avg_name= bakery1['name']
#
# for bakery in bakerys:
#     week_profit = profit_count(bakery['weekly_baked_goods'])
#     day_avg = day_prod_avg_by_week(bakery['weekly_baked_goods'])
#     print(f'Kepikla {bakery['name']} pelnas : {week_profit}. dienos gamibos vidurkis: {round(day_avg,2)}')
#     if week_profit >= max_week_sales:
#         max_week_sales = week_profit
#         max_week_sales_name = bakery['name']
#     if day_avg <= min_prod_avg_by_week:
#         min_prod_avg_by_week = day_avg
#         min_prod_avg_name = bakery['name']
#
# print(f'Shios savaites pilningiaus yra kepikla: {max_week_sales_name}')
# print(f'Shios savaites maziausias pagamintas vidurkis yra kepikloje: {min_prod_avg_name}')
12.Susikurkite sąrašą, kuriame būtų saugomos skirtingos knygos (kaip
dictionary elementai). Apie kiekvieną knygą į atskirus knygų dictionary
sudėkite norimą informaciją (bent 3 savybes). Į list įdėkite bent 3 knygas.
Visas šias knygas išsiveskite. Tuomet parodykite pirmą knygą. Antros
knygos kažkurią savybę.
# print('##############################################################################################################')
13.Susikurkite sąrašą, kuriame būtų keletas prekių (kaip dictionary
elementai) ir jį užpildykite pasirinktais duomenimis. Išveskite visų prekių
pavadinimus su kainomis ir dar kokiais nors atributais atskirose eilutėse.
# print('##############################################################################################################')
14.Susikurkite sąrašą, kuriame būtų saugoma informacija apie keletą
automobilių (kaip dictionary elementai) ir užpildykite jį pasirinktais
duomenimis. Išveskite kiekvieno automobilio pavadinimą, metus ir
paskaičiuotą jo amžių (dabartiniai metai - gamybos metai).
# print('##############################################################################################################')
15.Susikurkite sąrašą, kuriame būtų saugoma keleto įmonių duomenys (kaip
dictionary elementai) ir jį užpildykite duomenimis. Išveskite kiekvienos
įmonės informaciją atskirose eilutėse, gražiai suformatuotai (sakinio
pavidalu ar pan.). Taip pat, ką nors paskaičiuokite iš turimų skaitinių
duomenų (pvz.: vidutinis įmonės amžius, darbuotojų kiekis per visas
įmones, bendras pelnas, ar pan.).
# print('##############################################################################################################')
16.Susikurkite sąrašą, kuriame būtų saugoma informacija apie skirtingas
ligonines (kaip dictionary elementai) ir užpildykite jį pasirinktais
duomenimis. Išveskite ligoninių pavadinimus su adresais skirtingose
eilutėse. Suskaičiuokite ką nors iš skaitinių jų duomenų, pvz.: bendrą
lankytojų kiekį, bendrą ar vidutinį darbuotojų kiekį, ar pan.
# print('##############################################################################################################')
17.Susikurkite sąrašą, kuriame būtų saugoma informacija apie keletą
studentų (kaip dictionary elementai), kur apie kiekvieną studentą būtų
žinoma ši informacija: vardas ir pavardė, amžius, pažymiai, studijų
programa, kursas. Kiekvieną studentą išveskite taip: pirmoje eilutėje visi
studento duomenys išskyrus jo pažymius, antroje eilutėje jo pažymiai,
trečioje jo pažymių vidurkis su prierašu 'pažymių vidurkis'. Išvedus visus
studentus dėkite brūkšnį (pvz.: -----) ir išveskite bendrą visų studentų
pažymių vidurkį.
# print('##############################################################################################################')
18.Susikurkite parduotuvės dictionary, kuriame būtų ši informacija:
pavadinimas, adresas, darbuotojų kiekis, prekių sąrašas (kiekviena kaip
dictionary elementas). Apie kiekvieną prekę parduotuvėje žinoma ši
informacija: pavadinimas; kodas; kaina; savikaina; turimas kiekis. Išveskite
parduotuvės bendrą informaciją, tuomet užrašą "prekės" ir atskirose
eilutėse turimas prekes su kuria nors jų informacija (pvz.: pavadinimai,
kainos ir turimi kiekiai). Galiausiai paskaičiuokite kiek iš viso parduotuvė
turi visų prekių (sudėkite jų kiekius). Raskite ir išveskite kurios prekės
turima daugiausiai, o kurios mažiausiai.
# print('##############################################################################################################')
19.Sukurkite norimą sąrašą iš dictionary elementų su norimais duomenimis.
Atlikite išvedimus ir pasirinktus skaičiavimus.