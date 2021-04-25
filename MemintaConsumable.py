from load import load_data
import datetime

consumable = []
consumable_history = []
header_consumable = []
header_consumable_history = []

load_data(consumable, header_consumable, './file_csv/gadget.csv')
load_data(consumable_history, header_consumable_history, './file_csv/gadget_borrow_history.csv')

def validasi_item(Item) :
    if Item[0] == "C" :
      return True
    else :
      return False

def write_consumable_history(Item, Tanggal, Jumlah, id_user) :
    Tanggal_datetime = datetime.strptime(Tanggal, '%d/%m/%Y')
    arr = [0 for i in range (5)]
    arr[0] = (consumable_history[len(consumable_history)][0]) + 1
    arr[1] = id_user
    arr[2] = Item
    arr[3] = Tanggal_datetime
    arr[4] = Jumlah
    consumable_history.append(arr)

def validasi_role(user_now) :
    if user_now['role'] == "User" :
      return True
    else :
      return False

def validasi_jumlah(Jumlah) :
  if Jumlah > 0 :
    return True
  else :
    return False

def validasi_tanggal(Tanggal):
    try:
      datetime.datetime.strptime(Tanggal, '%d/%m/%Y')
    except ValueError :
      return False

def validasi_input(Item,Tanggal,Jumlah) :
  if validasi_item(Item) and validasi_tanggal(Tanggal) and validasi_jumlah(Jumlah) :
      return True
  else :
      return False

# ALGORITMA UTAMA

def minta(user_now) :
  id_user = user_now['id']
  if validasi_role(user_now) :
    Item = str(input("Masukan id item : "))
    Jumlah = int(input("Jumlah : "))
    Tanggal = str(input("Tanggal permintaan :"))

    while (not(validasi_input(Item, Jumlah, Tanggal))) :
      print("Masukan tidak sesuai. Ulangi!")
      Item = str(input("Masukan id item : "))
      Jumlah = int(input("Jumlah : "))
      Tanggal = str(input("Tanggal permintaan :"))

    IdItem = 0
    for i in range (len(consumable)) :
        if consumable[i][0] == Item :
            IdItem = i

    if consumable[IdItem][3] >= Jumlah :
        consumable[IdItem][3] = (consumable[IdItem][3]) - Jumlah

        print("Item", consumable[IdItem][1], "(x"+str(Jumlah)+") telah berhasil diambil!")

        write_consumable_history(Item, Tanggal, Jumlah, id_user)
    elif consumable[IdItem][3] == "infinity" :
        print("Item", consumable[IdItem][1], "(x"+str(Jumlah)+") telah berhasil diambil!")

        write_consumable_history(Item, Tanggal, Jumlah, id_user)
    else :
        if consumable[IdItem][3] == 0 :
            print("Item", consumable[IdItem][1], "telah habis :(.")
        else :
            print("Item", consumable[IdItem][1], "hanya tersisa", consumable[IdItem][3], "buah.")
    
  else :
    print("Anda tidak dapat mengakses bagian ini")