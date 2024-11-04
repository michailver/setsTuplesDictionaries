pirmas = set({8, 2, 3, 5, 1})
antras = {8, 2, 3, 5, 1}

print('pirmas', pirmas)
print('antras', antras)
print (type(pirmas))
print (type(antras))

# 1. Įsivaizduokite, kad sukūrėte balsavimo formą, kurioje žmogus galėjo
# rinktis 1 iš kelių galimų variantų (ar įrašyti savo) ir turite sąraše visus tuos
# balsavimo duomenis (pvz: balsavimui panaudotas klausimas
# “labiausiai patinkanti kalba:”, o atsakymai [‘c++’, ‘python’,
# ‘python’, ‘javascript’, ‘python’, ‘c#’, ‘javascript’]).
# Atrinkite visus skirtingus atsakymų variantus į atskirą sąrašą (būtų
# [‘c++’, ‘python’, ‘javascript’, ‘c#’]).
list =  ['c++', 'python','python', 'javascript', 'python', 'c#', 'javascript']
print(list)
list_to_set = set(list)
print(list_to_set)
# ‘python’, ‘javascript’, ‘python’, ‘c#’, ‘javascript’]
# 2. Savo nuožiūra atlikite dar bent vieną analogišką užduotį.
list_A = ["Anna", "Boris", "Victor", "Galina", "Dmitry", "Elena", "Anna", "Igor", "Galina"]
list_B = ["Boris", "Victor", "Elena", "Zoe", "Igor", "Leonid", "Anna"]
set_a = set(list_A)
set_b = set(list_B)
# print(f'list_A: ', list_A)
# print(f'set_A: ', set_a)
# print(f'list_B: ', list_B)
# print(f'set_B: ', set_b)
print(set_a - set_b)  # Registered but didn't attend
print(set_b - set_a)  # Attended without registration
print(set_a & set_b)  # Both registered and attended
print(set_a | set_b)


# or | arba visus unikalius
# and & grazina besikartojan2ius