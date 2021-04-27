from load import load_data
from datetime import datetime

gadget = []
gadget_borrow = []
gadget_return = []
header_gadget = []
header_gadget_borrow = []
header_gadget_return = []

load_data(gadget, header_gadget, './file_csv/gadget.csv')
load_data(gadget_borrow, header_gadget_borrow, './file_csv/gadget_borrow_history.csv')
load_data(gadget_return, header_gadget, './file_csv/gadget_return_history.csv')

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

def validasi_jumlah(Jumlah, id_peminjaman) :
    Jumlah_kembali = 0
    for i in range (len(gadget_return)) :
      if id_peminjaman == gadget_return[i][1] :
          Jumlah_kembali = Jumlah_kembali + gadget_return[i][3]

    for i in range (len(gadget_borrow)) :
      if id_peminjaman == gadget_borrow[i][0] :
        Jumlah_pinjam = gadget_borrow[i][4]

    if Jumlah > 0 and Jumlah <= (Jumlah_pinjam - Jumlah_kembali):
      return True
    else :
      return False

def validasi_no_item(Item_nomor, arr_id_peminjaman) :
  if Item_nomor > 0 and Item_nomor <= (len(arr_id_peminjaman)):
      return True
  else :
      return False    

def validasi_input(Tanggal,Jumlah,Item_nomor, arr_id_peminjaman, id_peminjaman) :
    if validasi_tanggal(Tanggal) == False or (not(validasi_jumlah(Jumlah, id_peminjaman))) or not(validasi_no_item(Item_nomor, arr_id_peminjaman)) :
        return False
    else :
        return True

def id_peminjaman_user(id_user):
    arr_id_peminjaman = []
    for i in range (len(gadget_borrow)) :
      if gadget_borrow[i][1] == id_user and gadget_borrow[i][5] == False :
          arr_id_peminjaman[i] = gadget_borrow[i][0]

    return arr_id_peminjaman

def id_item_user(id_user) :
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

def write_gadget_return_history(id_peminjaman, Tanggal, Jumlah) :
    arr = [0 for i in range (5)]
    arr[0] = gadget_return[len(gadget_return)][0] + 1
    arr[1] = id_peminjaman
    arr[2] = Tanggal #datetime.strptime(Tanggal, '%d/%m/%Y')
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

def pesan_kesalahan(Item_nomor, Tanggal, Jumlah, arr_id_peminjaman) :
    if (validasi_no_item(Item_nomor, arr_id_peminjaman)) == False :
        print('Nomor peminjaman yang Anda masukan tidak sesuai.')
        if (validasi_tanggal(Tanggal)) == False :
            print('Tanggal yang Anda masukan tidak sesuai.')
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')
        else :
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')
    else :
        if (validasi_tanggal(Tanggal)) == False :
            print('Tanggal yang Anda masukan tidak sesuai.')
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')
        else :
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')

# ALGORITMA UTAMA

def kembalikan(user_now):
  if validasi_role(user_now) :
    id_user = user_now['id']

    arr_id_peminjaman= id_peminjaman_user(id_user)
    arr_id_item = id_item_user(id_user)
    print('===== ITEM YANG DIPINJAM =====')
    for i in range (len(arr_id_item)) :
      Item = arr_id_item[i]
      tulis_item(Item)

    Item_nomor = int(input("Masukan nomor peminjaman : "))
    Tanggal = str(input("Tanggal pengembalian : "))
    Jumlah = int(input("Jumlah : "))
    id_peminjaman = arr_id_peminjaman[Item_nomor - 1]
    print()
    pesan_kesalahan(Item_nomor, Tanggal, Jumlah, arr_id_peminjaman)
    print()

    while (not(validasi_input(Tanggal, Jumlah, Item_nomor, arr_id_peminjaman))):
      Item_nomor = int(input("Masukan nomor peminjaman : "))
      Tanggal = str(input("Tanggal pengembalian : "))
      Jumlah = int(input("Jumlah : "))
      id_peminjaman = arr_id_peminjaman[Item_nomor - 1]
      print()
      pesan_kesalahan(Item_nomor, Tanggal, Jumlah, arr_id_peminjaman)
      print()

    Item = arr_id_item[Item_nomor - 1]

    write_gadget_return_history(id_peminjaman, Tanggal, Jumlah)
    ubah_data(Item, Jumlah)

    for i in range (len(gadget)) :
      if Item == gadget[i][0] :
          Nama = gadget[i][1]

    print("Item "+str(Nama)+"(x"+str(Jumlah)+") telah dikembalikan")

  else :
    print("Anda tidak dapat mengakses bagian ini")