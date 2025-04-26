import re

def cek_anagram(kata_pertama, kata_kedua):
    kata_pertama = re.sub(r'[^a-zA-Z]', '', kata_pertama).lower()
    kata_kedua = re.sub(r'[^a-zA-Z]', '', kata_kedua).lower()
    return sorted(kata_pertama) == sorted(kata_kedua)

kata_1 = input("Masukkan kata pertama: ")
kata_2 = input("Masukkan kata kedua: ")

if cek_anagram(kata_1, kata_2):
    print(f"'{kata_1}' dan '{kata_2}' adalah anagram.")
else:
    print(f"'{kata_1}' dan '{kata_2}' bukan anagram.")

