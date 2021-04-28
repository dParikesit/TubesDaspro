from load import load_data

gadget = []
header_gadget = []
load_data(gadget, header_gadget,'./file_csv/gadget.csv')
def carirarity(gadget) :
  rar = input("Masukkan rarity: ")
  print("")

  print("Hasil pencarian: ")
  print("")

  for i in range (len(gadget)):
      if (gadget[i][4] == rar):
          print("Nama            : ", gadget[i][1])
          print("Deskripsi       : ", gadget[i][2])
          print("Jumlah          : ", gadget[i][3])
          print("Rarity          : ", gadget[i][4])
          print("Tahun Ditemukan : ", gadget[i][5],"\n")  