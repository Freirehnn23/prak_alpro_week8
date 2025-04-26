import re
import random
import string

def generate_random_password(length=8):
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for _ in range(length))

def process_emails(teks):
    polaEmail = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    emails = re.findall(polaEmail, teks)
    hasil = []
    for email in emails:
        username = email.split('@')[0]
        password = generate_random_password()
        hasil.append(f"{email} username: {username} , password: {password}")
    return "\n".join(hasil)

teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

output = process_emails(teks)
print(output)