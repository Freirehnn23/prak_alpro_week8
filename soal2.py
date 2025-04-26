import re

def hitung_kata(teks, kata_dicari):
    teks = re.sub(r'[^\w\s]', '', teks).lower()
    kata_dicari = kata_dicari.lower()
    daftar_kata = teks.split()
    jumlah = daftar_kata.count(kata_dicari)
    return jumlah

kalimat = input("Masukan kalimat yang diinginkan: ")
kata = input("Masukkan kata yang ingin dihitung: ")

frekuensi = hitung_kata(kalimat, kata)
print(f"'{kata}' ada {frekuensi} buah.")
