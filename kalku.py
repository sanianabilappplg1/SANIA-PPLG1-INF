
print("a. Pertambahan")
print("b. Perkalian")
print("c. Pengurangan")
print("d. Pembagian")

sania = 25
nabila = 5

pilih = input("Pilih operator (a-d): ")

if pilih == "a":
    hasil = sania + nabila
elif pilih == "b":
    hasil = sania * nabila
elif pilih == "c":
    hasil = sania - nabila
elif pilih == "d":
    hasil = sania / nabila

print("Hasil:", hasil)