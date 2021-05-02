
def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False

def hapus_gadget(gadget,ID):
    count = 0
    for i in range (len(gadget)):
      if gadget[i][0] == ID:
        print("Apakah anda yakin ingin menghapus", gadget[i][1], "(Y/N)?")
        pilihan = input()
        if(pilihan == "Y"):
            print("Item telah berhasil dihapus dari database")
            gadget.pop(i)
            count += 1
    if count == 0:
        print("Tidak ada item dengan ID tersebut")

def hapus_consumable(consumable,ID):
    count = 0
    for i in range (len(consumable)):
      if consumable[i][0] == ID:
        print("Apakah anda yakin ingin menghapus", consumable[i][1], "(Y/N)?")
        pilihan = input()
        if(pilihan == "Y"):
            print("Item telah berhasil dihapus dari database")
            consumable.pop(i)
            count += 1
    if count == 0:
        print("Tidak ada item dengan ID tersebut")

def hapusitem(user_now, gadget, consumable) :
  if validasi_role(user_now):
      ID = input("Masukkan ID item: ")
      s = ID
      list(s)
      
      if s[0] != "G" and s[0] != "C":
          print("Tidak ada item dengan ID tersebut")
      else:
          if s[0] == "G":
              hapus_gadget(gadget,ID)
          elif s[0] == "C":
              hapus_consumable(consumable,ID)
  else :
    print("Anda tidak dapat mengakses bagian ini.")