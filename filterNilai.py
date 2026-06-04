def apakah_lulus (nilai_siswa, nilai_kkm):
    if nilai_siswa >= nilai_kkm:
        return True
    else:
        return False
print(apakah_lulus(80, 96))    
print(apakah_lulus(60,75))