from variabel import choice,user,gadget,gadget_borrow,gadget_return,consumable,consumable_history,header_user,header_gadget,header_gadget_borrow,header_gadget_return,header_consumable,header_consumable_history,user_now

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
            