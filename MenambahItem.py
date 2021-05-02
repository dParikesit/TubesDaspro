from datetime import datetime

global gadget
global consumable
global header_gadget
global header_consumable


def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False

def validasi_ID(data, ID):
    for i in range (len(data)):
        if(data[i][0] == ID):
            return True

def validasi_rarity(rarity):
    if rarity != "A" and rarity != "B" and rarity != "C" and rarity != "S":
        return True

def validasi_jumlah(jumlah):
    if jumlah < 0:
        return True

def is_datetime(tahun):
    try:
        datetime.strptime(tahun, '%Y')
        return True
    except ValueError:
        return False

def write_new_item_gadget(s, nama, deskripsi, jumlah, rarity, tahun, gadget) :
    arr = [0 for i in range (6)]

    arr[0] = s
    arr[1] = nama
    arr[2] = deskripsi
    arr[3] = jumlah
    arr[4] = rarity
    arr[5] = tahun
    gadget.append(arr)

def write_new_item_consumable(s, nama, deskripsi, jumlah, rarity,consumable) :
    arr = [0 for i in range (5)]

    arr[0] = s
    arr[1] = nama
    arr[2] = deskripsi
    arr[3] = jumlah
    arr[4] = rarity
    consumable.append(arr)

# ALGORITMA UTAMA

def tambahitem(user_now, gadget, consumable) :
  ID = input("Masukkan ID: ")
  s = ID
  list(s)
  
  if validasi_role(user_now) :
    if s[0] != "G" and s[0] != "C":
        print("Gagal menambahkan item karena ID tidak valid")
    else:
        if s[0] == "G":
            if validasi_ID(gadget, ID):
                print("Gagal menambahkan item karena ID sudah ada")
            else: 
                nama = input("Masukkan Nama: ")
                deskripsi = input("Masukkan Deskripsi: ")
                jumlah = int(input("Masukkan Jumlah: "))
                rarity = input("Masukkan Rarity: ")
                tahun = input("Masukkan tahun ditemukan: ")
                if validasi_rarity(rarity) or validasi_jumlah(jumlah) or (is_datetime(tahun) == False):
                    print("Input tidak valid")
                else:
                    write_new_item_gadget(s, nama, deskripsi, jumlah, rarity, tahun, gadget)
                    print("Input telah berhasil ditambahkan ke database")
        elif s[0] == "C":
            if validasi_ID(consumable, ID):
                print("Gagal menambahkan item karena ID sudah ada")
            else: 
                nama = input("Masukkan Nama: ")
                deskripsi = input("Masukkan Deskripsi: ")
                jumlah = int(input("Masukkan Jumlah: "))
                rar = input("Masukkan Rarity: ")
                if validasi_rarity(rar) or validasi_jumlah(jumlah):
                    print("Input tidak valid")
                else:
                    write_new_item_consumable(s, nama, deskripsi, jumlah, rar, consumable)
                    print("Input telah berhasil ditambahkan ke database")
  else :
    print("Anda tidak dapat mengakses bagian ini")

# Ok. Makasih
# ver kalo mau nyobo ketik di shell python3 kantongajaib.py file_csv login pake nobite45 password nobyte habis itu register buat user baru
# soalnya kalo gini yang lain mau nyoba gak bisa ada error

# oiya sama yang pencarian rarity, raritynya belum di validasi

# Kata si Dimas ga usah. Karena admin dan usernya bisa pakai