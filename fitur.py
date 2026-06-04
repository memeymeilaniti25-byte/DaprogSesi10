def validasi_tweet(teks_input):
    if len (teks_input) <= 140:
        return teks_input
    else:
        teks_terpotong = teks_input[:140] + "..."
        return teks_terpotong
print(validasi_tweet("Halo everyone! Good Morning and Have a Nice Day."))
tweet_panjang = "A" * 145
print(validasi_tweet(tweet_panjang))
