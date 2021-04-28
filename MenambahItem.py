from load import load_data
from datetime import datetime

gadget=[]
consumable = []
header_gadget = []
header_consumable = []
load_data(gadget, header_gadget,'./file_csv/gadget.csv')
load_data(consumable, header_consumable, './file_csv/consumable.csv')

ID = input("Masukkan ID: ")
s = ID
list(s)

def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False

def validasi_ID(data, ID):
    for i in range (len(data)):
        if(data[i][0] == ID):
            return True

def validasi_rarity(rar):
    if rar != "A" and rar != "B" and rar != "C" and rar != "S":
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

def write_new_item(s, nama, deskripsi, jumlah, rar, tahun, gadget, consumable) :
    if s[0] == "G" :
      arr = [0 for i in range (6)]

      arr[0] = s
      arr[1] = nama
      arr[2] = deskripsi
      arr[3] = jumlah
      arr[4] = rar
      arr[5] = tahun
      gadget.append(arr)

    else :
      arr = [0 for i in range (5)]

      arr[0] = s
      arr[1] = nama
      arr[2] = deskripsi
      arr[3] = jumlah
      arr[4] = rar
      consumable.append(arr)

# ALGORITMA UTAMA

def tambahitem(user_now, gadget, consumable) :
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
                rar = input("Masukkan Rarity: ")
                tahun = input("Masukkan tahun ditemukan: ")
                if validasi_rarity(rar) or validasi_jumlah(jumlah) or (is_datetime(tahun) == False):
                    print("Input tidak valid")
                else:
                    write_new_item(s, nama, deskripsi, jumlah, rar, tahun, gadget, consumable)
                    print("Input telah berhasil ditambahkan ke database")
        elif s[0] == "C":
            if validasi_ID(consumable, ID):
                print("Gagal menambahkan item karena ID sudah ada")
            else: 
                nama = input("Masukkan Nama: ")
                deskripsi = input("Masukkan Deskripsi: ")
                jumlah = int(input("Masukkan Jumlah: "))
                rar = input("Masukkan Rarity: ")
                if validasi_rarity(consumable) or validasi_jumlah(consumable):
                    print("Input tidak valid")
                else:
                    write_new_item(s, nama, deskripsi, jumlah, rar, tahun, gadget, consumable)
                    print("Input telah berhasil ditambahkan ke database")
  else :
    print("Anda tidak dapat mengakses bagian ini")