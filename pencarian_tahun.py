from load import load_data

gadget = []
header_gadget = []
load_data(gadget, header_gadget,'./file_csv/gadget.csv')

tahun = int(input("Masukkan tahun: "))
kategori = input("Masukkan kategori: ")

idx = 0
# Kalau ada yang sesuai dengan dengan looping di bawah, outputnya gini    
def printHasilPencarian():
    if (idx == 0):
        for i in range(len(gadget)):
            print("Hasil pencarian :")
            print("Nama            : ", gadget[i][1])
            print("Deskripsi       : ", gadget[i][2])
            print("Jumlah          : ", gadget[i][3])
            print("Rarity          : ", gadget[i][4])
            print("Tahun Ditemukan : ", gadget[i][5])
        return
    else:
        print("Hasil pencarian: ")
        print("Tidak ada gadget yang ditemukan")
        return

# Ini membandingkan antara tahun dengan tahun di file gadget
for data in gadget:
    if(data[5] == tahun and kategori == "="):
        idx == 0
    elif(data[5] > tahun and kategori == ">"):
        idx == 0
    elif(data[5] < tahun and kategori == "<"):
        idx == 0
    elif(data[5] >= tahun and kategori == ">="):
        idx == 0
    elif(data[5] <= tahun and kategori == "<="):
        idx == 0
    else:
        idx += 1

printHasilPencarian()