# Program Validasi Form Input

# Input data
nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

# Variabel penanda validasi
valid = True

# Validasi nama (hanya huruf dan spasi)
if not nama.replace(" ", "").isalpha():
    print("Error: Nama lengkap harus hanya berisi huruf.")
    valid = False

# Validasi nomor telepon (hanya angka)
if not telepon.isdigit():
    print("Error: Nomor telepon harus hanya berisi angka.")
    valid = False

# Validasi email (harus mengandung @ dan .)
if "@" not in email or "." not in email:
    print("Error: Email harus mengandung karakter '@' dan '.'.")
    valid = False

# Hasil akhir
if valid:
    print("Data pendaftaran valid.")
