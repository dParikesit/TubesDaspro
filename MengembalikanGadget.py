from load import load_data
import datetime

gadget = []
gadget_borrow = []
gadget_return = []
header_gadget = []
header_gadget_borrow = []
header_gadget_return = []

load_data(gadget, header_gadget, './file_csv/gadget.csv')
load_data(gadget_borrow, header_gadget_borrow, './file_csv/gadget_borrow_history.csv')
load_data(gadget_return, header_gadget, './file_csv/gadget_return_history')

def validasi_tanggal(Tanggal):
    try:
      datetime.datetime.strptime(Tanggal, '%d/%m/%Y')
    except ValueError :
      return False

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

def validasi_input(Tanggal,Jumlah) :
  if validasi_tanggal(Tanggal) and validasi_jumlah(Jumlah) :
      return True
  else :
      return False
def item_yang_dipinjam(id_user) :
  Count_Item = 0
  for i in range (len(gadget_borrow)) :
      if (gadget_borrow[i][1]) == id_user :
          Count_Item = Count_Item + 1
  
  arr = [0 for i in range (len(gadget_borrow))]
  arr_id = [0 for i in range (Count_Item)]
  arr_id_final = []

  for i in range (len(gadget_borrow)) :
      if (gadget_borrow[i][1]) == id_user :
          arr[i] = (gadget_borrow[i][2]) 
      else :
          arr[i] = 0  
    
  for i in range (len(arr)) :
      if arr[i] != 0 :
          arr_id.append(arr[i])
             
  arr_id_raw = arr_id[((len(arr_id)) - Count_Item):(len(arr_id))]
  arr_id_unique = list(set(arr_id_raw))

  for i in range (len(arr_id_unique)):
    Item = arr_id_unique[i]
    Jumlah_pinjam = 0
    Jumlah_kembali = 0
    for j in range (len(gadget_borrow)) :
      if gadget_borrow[j][1] == id_user and gadget_borrow[j][2] == Item:
        Jumlah_pinjam = Jumlah_pinjam + (gadget_borrow[j][4])

    for j in range (len(gadget_return)) :
      if gadget_return[j][1] == id_user and gadget_return[j][2] == Item :
        Jumlah_kembali = Jumlah_kembali + (gadget_return[j][4])

    if Jumlah_pinjam > Jumlah_kembali :
        arr_id_final.append(Item)
  
  return arr_id_final

def tulis_item(Item, i) :
    for k in range (len(gadget)) :
      if gadget[k][0] == Item :
          IdItem = k
    print(str(i+1)+".", gadget[IdItem][1])

def write_gadget_return_history(Item, Tanggal, Jumlah, id_user) :
    arr = [0 for i in range (5)]
    arr[0] = (gadget_return[len(gadget_return)][0]) + 1
    arr[1] = id_user
    arr[2] = Item
    arr[3] = Tanggal
    arr[4] = Jumlah
    gadget_return.append(arr) 

def ubah_jumlah(Item, Jumlah) :
    for i in range (len(gadget)) :
      if gadget[i][0] == Item :
          gadget[i][3] = gadget[i][3] + Jumlah 

# ALGORITMA UTAMA
def kembalikan(user_now):
  if validasi_role(user_now['role']) :
    id_user = user_now['id']

    arr = item_yang_dipinjam(id_user)

    for i in range (len(arr)) :
      Item = arr[i]
      tulis_item(Item)

    Item_nomor = int(input("Masukan nomor peminjaman : "))
    Tanggal = str(input("Tanggal pengembalian : "))
    Jumlah = int(input("Jumlah : "))

    while (not(validasi_input(Tanggal, Jumlah))):
      print("Masukan tidak sesuai. Ulangi!")
      Tanggal = str(input("Tanggal pengembalian : "))
      Jumlah = int(input("Jumlah : "))

    Item = arr[Item_nomor-1]

    write_gadget_return_history(Item, Tanggal, Jumlah, id_user)
    ubah_jumlah(Item, Jumlah)

    for i in range (len(gadget)) :
      if Item == gadget[i][0] :
          Nama = gadget[i][1]

    print("Item "+str(Nama)+"(x"+str(Jumlah)+") telah dikembalikan")

  else :
    print("Anda tidak dapat mengakses bagian ini")