def hitung_gaji(nama, golongan, jam_kerja):
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        return "Golongan tidak valid!"

    if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
    else:
        uang_lembur = 0

    gaji_total = (jam_kerja * upah_per_jam) + uang_lembur
    
    return f"Nama: {nama}\nGaji Mingguan: Rp {gaji_total}"

nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan (A/B/C/D): ")
jam_kerja = int(input("Masukkan jam kerja: "))

gaji = hitung_gaji(nama, golongan, jam_kerja)
print(gaji)
