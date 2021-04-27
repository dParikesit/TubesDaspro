from load import load_data

gadget = []
header_gadget = []
consumable = []
header_consumable = []
load_data(gadget, header_gadget,'./file_csv/gadget.csv')
load_data(consumable, header_consumable, './file_csv/consumable.csv')

ID = input("Masukkan ID item: ")
s = ID
list(s)
idx = 0

def cekPilihan():
  pilihan = input()
  if(pilihan == "Y"):
    print("Item telah berhasil dihapus dari database")
  return pilihan

if s[0] != "G" and s[0] != "C":
  idx = 0 
else:
  if (s[0] == "G"):
    for i in range(len(gadget)):
      if gadget[i][0] == ID:
        print("Apakah anda yakin ingin menghapus", gadget[i][1], "(Y/N)?")
        idx += 1
  elif (s[0] == "C"):
    for i in range (len(consumable)):
      if consumable[i][0] == ID:
        print("Apakah anda yakin ingin menghapus", consumable[i][1], "(Y/N)?")
        idx += 1

if (idx == 1):
  cekPilihan()
else:
  print("Tidak ada item dengan ID tersebut")
