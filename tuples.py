# 1. Susikurkite tuple iš studijų programos modulių pavadinimų.
# Atspausdinkite šiuos pavadinimus sąraše, prieš kiekvieną pavadinimą
# išvedant brūkšniuką. Raskite ilgiausią modulio pavadinimą.
moduliai = ("Programavimo pagrindai", "Matematika pagrindai", "Fizika - visu mokslu motiana", "Anglų kalba")

max_modul_len=len(moduliai[0])
longest_modul_name = moduliai[0]
for modulis in moduliai:
    print("-", len(modulis), modulis)
    if max_modul_len < len(modulis):
        max_modul_len = len(modulis)
        longest_modul_name = modulis
print (f'ilgiausiai pavadinimas: {longest_modul_name}, su {max_modul_len} simboliu.')
print('##############################################################################################################')

# 2. Susikurkite tuple iš mėnesių pavadinimų. Susikurkite kitus tuples
# sezonams apibūdinti: žiema, pavasaris, vasara, ruduo. Panaudokite slicing
# [start:end], kad atitinkamus mėnesius sudėtumėte į atitinkamus sezonų
# tuples. Šį priskyrimą turite atlikti kuriant individualius sezonų tuples, kitaip
# išmes klaidą, kad jo negalite modifikuoti.
menesiai = ('sausis', 'vasaris', 'kovas','balandis', 'geguze', 'birzelis', 'liepa','rugpjutis', 'rugsejis', 'spalis', 'lapkritis','gruodis')

ziema = (menesiai[11],) + menesiai[0:2]
print('ziema: ',ziema)
pavasaris = menesiai[2:5]
print('pavasaris: ',pavasaris)
vasara = menesiai[5:8]
print('vasara: ',vasara)
ruduo = menesiai[8:11]
print('ruduo: ',ruduo)