global gadget
global header_gadget

def carirarity(gadget) :
  rarity = input("Masukkan rarity: ")
  print("")

  if rarity == 'A' or rarity == 'B' or rarity == 'C' or rarity == 'S' :
      print("Hasil pencarian: ")
      print("")

      for i in range (len(gadget)):
          if (gadget[i][4] == rarity):
              print("Nama            : ", gadget[i][1])
              print("Deskripsi       : ", gadget[i][2])
              print("Jumlah          : ", gadget[i][3])
              print("Rarity          : ", gadget[i][4])
              print("Tahun Ditemukan : ", gadget[i][5],"\n")
            