def buat_username (nama_lengkap, tahun_lahir):
    kata_pertama = nama_lengkap.split()[0].lower()
    dua_angka_terakhir = str(tahun_lahir)[-2:]
    username = kata_pertama + dua_angka_terakhir
    
    return username
print(buat_username("Aldi Mulyadi Lubis", 2005))