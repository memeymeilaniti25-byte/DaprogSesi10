def estimasi_tiba (jarak_km, kondisi_cuaca):
    waktu_dasar = jarak_km * 3

    if kondisi_cuaca.lower() == "hujan":
        total_estimasi = waktu_dasar + 10
    else:
        total_estimasi= waktu_dasar

    return  total_estimasi 
print(estimasi_tiba(2, "hujan"))