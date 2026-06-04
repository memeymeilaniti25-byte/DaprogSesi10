def split_bill(total_nota, jumlah_orang, persen_tips):
    jumlah_tips = total_nota * (persen_tips / 100)
    final_bayar = total_nota + jumlah_tips
    bayar_perOrng = final_bayar / jumlah_orang

    return bayar_perOrng
print(split_bill(3000000, 4, 10))
    
