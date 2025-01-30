#----------- - Paskaita: try-except – Exceptionų (klaidų) suvaldymas - - - - - - - - -
print(' - - - - - - -Pagrindinis try-except pavyzdys - - - -- - - - - - - - ')

ivestis = '4'
try:
    skaicius = int(ivestis)
    res = skaicius / 0  # šis veiksmas sukels klaidą
except Exception as e:
    print("Mes crashinom, tačiau suvaldėm crashą")
    print(e.__class__)  # išspausdina klaidos klasę
    print(e)  # išspausdina klaidos pranešimą

print("Programa tęsia darbą")


