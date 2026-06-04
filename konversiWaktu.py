def konversi_menit (jumlah_episode, durasi_per_episode):
    total_menit = jumlah_episode * durasi_per_episode
    jam = total_menit // 60
    menit = total_menit % 60

    return jam, menit
hasil_jam, hasil_menit = konversi_menit (5,50)
print(f"{hasil_jam} jam, {hasil_menit} menit")
print(konversi_menit(5, 50))

