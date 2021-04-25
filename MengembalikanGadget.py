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

def id_peminjaman_user(id_user):
    arr_id_peminjaman = []
    for i in range (len(gadget_borrow)) :
      if gadget_borrow[i][1] == id_user and gadget_borrow[i][5] == False :
          arr_id_peminjaman[i] = gadget_borrow[i][0]

    return arr_id_peminjaman

def id_item(id_user) :
    arr_id_item = []
    for i in range (len(gadget_borrow)) :
      if gadget_borrow[i][1] == id_user and gadget_borrow[i][5] == False :
        arr_id_item[i] = gadget_borrow[i][2]
    
    return arr_id_item
  
def tulis_item(Item, i) :
    for k in range (len(gadget)) :
      if gadget[k][0] == Item :
          IdItem = k
    print(str(i+1)+".", gadget[IdItem][1])

def write_gadget_return_history(Item, Tanggal, Jumlah) :
    Tanggal_datetime = datetime.strptime(Tanggal, '%d/%m/%Y')
    arr = [0 for i in range (5)]
    arr[0] = gadget_return[len(gadget_return)][0] + 1
    arr[1] = id_peminjaman
    arr[2] = Tanggal_datetime
    arr[3] = Jumlah
    gadget_return.append(arr) 

def ubah_data(Item, Jumlah, id_peminjaman) :
    # Mengubah jumlah gadget pada data gadget.csv
    for i in range (len(gadget)) :
      if gadget[i][0] == Item :
          gadget[i][3] = gadget[i][3] + Jumlah   

    # Mengubah is_returned pada data gadget_borrow_history.csv
    Index = 0
    for i in range (len(gadget_borrow)) :
      if gadget_borrow[i][0] == id_peminjaman :
            Index = i

    Jumlah_kembali = Jumlah
    for i in range (len(gadget_return)) : 
      if gadget_return[i][1] == id_peminjaman :
          Jumlah_kembali = Jumlah_kembali + gadget_return[i][4]

    if Jumlah_kembali == gadget_borrow[Index][4] :
        gadget_borrow[Index][5] = True

# ALGORITMA UTAMA

def kembalikan(user_now):
  if validasi_role(user_now['role']) :
    id_user = user_now['id']

    arr_id_peminjaman= id_peminjaman_user(id_user)
    arr_id_item = id_item(id_user)

    for i in range (len(arr_id_item)) :
      Item = arr_id_item[i]
      tulis_item(Item)

    Item_nomor = int(input("Masukan nomor peminjaman : "))
    Tanggal = str(input("Tanggal pengembalian : "))
    Jumlah = int(input("Jumlah : "))

    while (not(validasi_input(Tanggal, Jumlah))):
      print("Masukan tidak sesuai. Ulangi!")
      Tanggal = str(input("Tanggal pengembalian : "))
      Jumlah = int(input("Jumlah : "))

    Item = arr_id_item[Item_nomor - 1]
    id_peminjaman = arr_id_peminjaman[Item_nomor - 1]

    write_gadget_return_history(id_peminjaman, Tanggal, Jumlah)
    ubah_data(Item, Jumlah)

    for i in range (len(gadget)) :
      if Item == gadget[i][0] :
          Nama = gadget[i][1]

    print("Item "+str(Nama)+"(x"+str(Jumlah)+") telah dikembalikan")

  else :
    print("Anda tidak dapat mengakses bagian ini")