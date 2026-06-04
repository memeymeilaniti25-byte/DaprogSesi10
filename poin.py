def hitung_poin_belanja (total_transaksi, status_member):
    if status_member == "FALSE":
        return 0
    jumlah_poin = total_transaksi // 20000
    return jumlah_poin
print(hitung_poin_belanja(100000, False))
print(hitung_poin_belanja(55000, True ))
