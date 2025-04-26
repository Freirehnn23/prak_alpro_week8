import re
from datetime import datetime

def cari_dan_hitungan_selisih(teks):
    list_tanggal = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', teks)
    sekarang = datetime.now()

    for tgl_str in list_tanggal:
        tgl_obj = datetime.strptime(tgl_str, "%Y-%m-%d")
        selisih = (sekarang - tgl_obj).days
        print(f"{tgl_obj} selisih {selisih} hari")

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""

cari_dan_hitungan_selisih(teks)
