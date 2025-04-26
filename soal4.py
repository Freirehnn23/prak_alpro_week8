import re

def cari_kata_terpendek_terpanjang(kalimat):
    kata_kata = re.findall(r'\b\w+\b', kalimat)

    if not kata_kata:
        return None, None  # Tidak ada kata ditemukan
    kata_pendek = kata_panjang = kata_kata[0]

    for kata in kata_kata:
        if len(kata) < len(kata_pendek):
            kata_pendek = kata
        if len(kata) > len(kata_panjang):
            kata_panjang = kata

    return kata_pendek, kata_panjang

kalimat = input("Masukan kalimat yang ingin anda cek: ") #"red snakes and a black frog in the pool"
terpendek, terpanjang = cari_kata_terpendek_terpanjang(kalimat)

print(f"Terpendek: {terpendek}")
print(f"Terpanjang: {terpanjang}")
