from variabel import choice,user,gadget,gadget_borrow,gadget_return,consumable,consumable_history,header_user,header_gadget,header_gadget_borrow,header_gadget_return,header_consumable,header_consumable_history,user_now

def equal(tahun, gadget):
    count = 0
    for i in range(len(gadget)):
        if(gadget[i][5] == tahun):
            print("Nama             : ", gadget[i][1])
            print("Deskripsi        : ", gadget[i][2])
            print("Jumlah           : ", gadget[i][3])
            print("Rarity           : ", gadget[i][4])
            print("Tahun Ditemukan  : ", gadget[i][5],"\n")
            count += 1
    if count == 0:
        print("Tidak ada data yang ditemukan")

def morethan(tahun, gadget):
    count = 0
    for i in range(len(gadget)):
        if(gadget[i][5] > tahun):
            print("Nama             : ", gadget[i][1])
            print("Deskripsi        : ", gadget[i][2])
            print("Jumlah           : ", gadget[i][3])
            print("Rarity           : ", gadget[i][4])
            print("Tahun Ditemukan  : ", gadget[i][5],"\n")
            count += 1
    if count == 0:
        print("Tidak ada data yang ditemukan")

def lessthan(tahun, gadget):
    count = 0
    for i in range(len(gadget)):
        if(gadget[i][5] < tahun):
            print("Nama             : ", gadget[i][1])
            print("Deskripsi        : ", gadget[i][2])
            print("Jumlah           : ", gadget[i][3])
            print("Rarity           : ", gadget[i][4])
            print("Tahun Ditemukan  : ", gadget[i][5],"\n")
            count += 1
    if count == 0:
        print("Tidak ada data yang ditemukan")

def moreequal(tahun, gadget):
    count = 0
    for i in range(len(gadget)):
        if(gadget[i][5] >= tahun):
            print("Nama             : ", gadget[i][1])
            print("Deskripsi        : ", gadget[i][2])
            print("Jumlah           : ", gadget[i][3])
            print("Rarity           : ", gadget[i][4])
            print("Tahun Ditemukan  : ", gadget[i][5],"\n")
            count += 1
    if count == 0:
        print("Tidak ada data yang ditemukan")

def lessequal(tahun, gadget):
    count = 0
    for i in range(len(gadget)):
        if(gadget[i][5] <= tahun):
            print("Nama             : ", gadget[i][1])
            print("Deskripsi        : ", gadget[i][2])
            print("Jumlah           : ", gadget[i][3])
            print("Rarity           : ", gadget[i][4])
            print("Tahun Ditemukan  : ", gadget[i][5],"\n")
            count += 1
    if count == 0:
        print("Tidak ada data yang ditemukan")

def caritahun(gadget) :
  tahun = int(input("Masukkan tahun: "))
  kategori = input("Masukkan kategori: ")

  print("Hasil pencarian: ")
  if(kategori == "="):
      equal(tahun, gadget)
  elif(kategori == ">"):
      morethan(tahun, gadget)
  elif(kategori == "<"):
      lessthan(tahun, gadget)
  elif(kategori == ">="):
      moreequal(tahun, gadget)
  elif(kategori == "<="):
      lessequal(tahun, gadget)
  else :
      print("Masukan tidak valid.")