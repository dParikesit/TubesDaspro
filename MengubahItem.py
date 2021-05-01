from load import load_data

gadget = []
header_gadget = []
consumable = []
header_consumable = []
load_data(gadget, header_gadget,'./file_csv/gadget.csv')
load_data(consumable, header_consumable, './file_csv/consumable.csv')

def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False

def add_gadget(gadget, ID):
    count = 0
    for i in range (len(gadget)):
        if gadget[i][0] == ID:
            jumlah = int(input("Masukkan jumlah: "))
            if jumlah >= 0:
              gadget[i][3] = gadget[i][3] + jumlah
              print(jumlah, gadget[i][1], "berhasil ditambahkan. Stok sekarang:", gadget[i][3])
              count += 1
            else:
                hasil = gadget[i][3] + jumlah
                total = -1*jumlah
                if(hasil >= 0):
                  gadget[i][3] = hasil
                  print(total, gadget[i][1], "berhasil dibuang. Stok sekarang:", gadget[i][3])
                  count += 1
                else:
                    print(total, gadget[i][1], "gagal dibuang karena stok kurang. Stok sekarang:", gadget[i][3])
                    count += 1
    if count == 0:
        print("Tidak ada item dengan ID tersebut")

def add_consumable(consumable, ID):
    count = 0
    for i in range (len(consumable)):
        if consumable[i][0] == ID:
            jumlah = int(input("Masukkan jumlah: "))
            if jumlah >= 0:
                consumable[i][3] = consumable[i][3] + jumlah
                print(jumlah, consumable[i][1], "berhasil ditambahkan. Stok sekarang:", consumable[i][3])
                count += 1
            else:
                hasil = consumable[i][3] + jumlah
                total = -1*jumlah
                if(hasil >= 0):
                    consumable[i][3] = hasil
                    print(total, consumable[i][1], "berhasil dibuang. Stok sekarang:", consumable[i][3])
                    count += 1
                else:
                    print(total, consumable[i][1], "gagal dibuang karena stok kurang. Stok sekarang:", consumable[i][3])
                    count += 1
    if count == 0:
        print("Tidak ada item dengan ID tersebut")

# ALGORITMA UTAMA

def ubahjumlah(user_now, gadget, consumable) :
  if validasi_role(user_now) :

    ID = input("Masukkan ID: ")
    s = ID
    list(s)

    if s[0] != "G" and s[0] != "C":
        print("Tidak ada item dengan ID tersebut")
    else:
        if s[0] == "G":
            add_gadget(gadget, ID)
        elif s[0] == "C":
            add_consumable(consumable, ID)
  else :
    print("Anda tidak dapat mengakses bagian ini.")