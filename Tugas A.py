def mulai_belanja():
    total_belanja = 0
    while True:
        try:
            harga_item = float(input("Masukkan harga item: "))
            total_belanja += harga_item

            if total_belanja > 100000:
                print(f"Total belanja: Rp{total_belanja:.2f}")
                print("Selamat! Anda mendapatkan hadiah.")
                break
            else:
                lanjut_belanja = input("Ingin menambah item lagi? (ya/tidak): ").lower()
                if lanjut_belanja != "ya":
                    print(f"Total belanja: Rp{total_belanja:.2f}")
                    print("Terimakasih telah berbelanja")
                    break
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.")

mulai_belanja()
