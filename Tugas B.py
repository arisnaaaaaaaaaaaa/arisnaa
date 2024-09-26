def check_password():
    password_benar = "0000"
    password = input("Masukkan password: ")

    if password == password_benar:
        print("Selamat datang yang mulia")
    else:
        print("Password salah, akses ditolak!")


if __name__ == "__main__":
    check_password()
