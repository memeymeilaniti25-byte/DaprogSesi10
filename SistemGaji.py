def hitungGajiLembur (gaji_pokok, total_jamKerja):
    lembur = 50000
    if total_jamKerja > 40:
        kelebihan_jamnya = total_jamKerja - 40
        uang_lembur = kelebihan_jamnya * lembur
        gaji_akhir = gaji_pokok + uang_lembur
    else:
        gaji_akhir = gaji_pokok    

    return gaji_akhir
print(hitungGajiLembur(2000000, 30))
print(hitungGajiLembur(2000000,45))
    