import re

def hapus_spasi_berlebih(teks):
    teks = re.sub(r'\s+', ' ', teks)
    teks = teks.strip()
    return teks

kalimat = input("masukan kalimat yang ingin dihapus spasi yang berlebih: ")
hasil = hapus_spasi_berlebih(kalimat)
print(f"Hasil: '{hasil}'")
