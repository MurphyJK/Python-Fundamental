"""
Semua sistaksis dasar pemograman terdiri dari :
1. Sequential   : Langkah berurutan
2. Percabangan  : Langkah melompat jika kondisi terpenuhi
3. Perulangan   : Mengulang langkah yang sama berkali - kali selama/sampai kondisi terpenuhi
 *: dibaca maka
"""
# Sequential
print("Ibu berkata,\"pergi ke toko\"")
print("Budi menjawab, \"Baik bu, apa yang saya harus lakukan di toko ?\"")
print("Ibu menjawab, \"Beli 1 botol susu\"")
print("Maka Budi berangkat ke toko")
print("dan mulai belanja")



# Branching
"""
-Variable = tempat dalam bahasa pemograman, dimana kamu menyimpan data. 
-Data itu bisa berupa : 1. Teks (string)
                       2. Angka
                       3. Kondisi benar/salah
"""

jumlah_susu_botol = 0
if jumlah_susu_botol > 0 :
    print("Budi memeriksa harganya dan ternyata uang nya cukup.")
    print("Budi membeli 1 botol susu")
else :
    print("Anak tidak jadi beli susu")

print("Anak pulang lalu menyampaikan hasilnya kepada ibu")