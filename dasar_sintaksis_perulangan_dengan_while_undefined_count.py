"""
# Program pengulangan membaca buku dengan while sampai paham
"""
jumlah_buku = 10
print("Ibu berkata, \"Baca semua buku mu\"")
total_jumlah_baca = 0
jumlah_paham = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_paham == 9:
        print(f"Buku ke {jumlah_paham + 1} belum paham")
    else :
        jumlah_paham = jumlah_paham + 1
        print(f"Buku ke {jumlah_paham} sudah dibaca dan dipahami")


print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}")
if jumlah_paham == jumlah_buku :
    print("\"Bu, semua buku sudah dibaca dan dipahami\"")
else:
    print(f"\"Tidak semua buku bisa dipahami\". Saya hanya bisa memahami {jumlah_paham} buku")