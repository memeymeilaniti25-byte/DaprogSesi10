def cek_diskon (total_harga, jumlah_tiket, kode_kupon):
    if kode_kupon == "NONTONSERU" and jumlah_tiket >= 2 :
        harga_akhir = total_harga - 15000
    else:
        harga_akhir = total_harga

    return harga_akhir
print(cek_diskon(200000, 5, "NONTONSERU"))    
print(cek_diskon(50000, 1, "NONTONSERU"))
print(cek_diskon(150000, 3, "MEMEYCANTIK"))