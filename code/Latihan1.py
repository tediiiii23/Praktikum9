txt = 'Hello World'

# Hitung jumlah karakternya
print("Jumlah karakter:", len(txt))

# Ambil karakter terakhir
print("Karakter terakhir:", txt[-1])

# Ambil karakter index ke-2 sampai index ke-4 (llo)
print("Index ke-2 sampai ke-4:", txt[2:5])

# Hilangkan spasi pada text tersebut (HelloWorld)
print("Tanpa spasi:", txt.replace(" ", ""))

# Ubah text menjadi huruf besar
print("Huruf besar:", txt.upper())

# Ubah text menjadi huruf kecil
print("Huruf kecil:", txt.lower())

# Ganti karakter H dengan karakter J
print("Ganti H dengan J:", txt.replace("H", "J"))
