from load import load_data

gadget = []
header_gadget = []
load_data(gadget, header_gadget,'./file_csv/gadget.csv')

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