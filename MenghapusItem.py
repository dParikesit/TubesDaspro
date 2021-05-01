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

def hapus_gadget(gadget,ID):
    count = 0
    for data in gadget:
      if data[0] == ID:
        print("Apakah anda yakin ingin menghapus", data[1], "(Y/N)?")
        pilihan = input()
        if(pilihan == "Y"):
            print("Item telah berhasil dihapus dari database")
            gadget.remove(data)
            count += 1
    if count == 0:
        print("Tidak ada item dengan ID tersebut")

def hapus_consumable(consumable,ID):
    count = 0
    for data in consumable:
      if data[0] == ID:
        print("Apakah anda yakin ingin menghapus", data[1], "(Y/N)?")
        pilihan = input()
        if(pilihan == "Y"):
            print("Item telah berhasil dihapus dari database")
            consumable.remove(data)
            count += 1
    if count == 0:
        print("Tidak ada item dengan ID tersebut")

def hapusitem(user_now, gadget, consumable) :
  if validasi_role(user_now) :

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