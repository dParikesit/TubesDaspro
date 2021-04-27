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
load_data(gadget_return, header_gadget, './file_csv/gadget_return_history.csv')


def validasi_item(Item) :
    found = False
    for i in range (len(gadget)) :
      if gadget[i][0] == Item :
          found = True

    if Item[0] == "G" and found == True :
      return True
    else :
      return False

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

def cek_peminjaman(Item) :
    found = 0
    if len(gadget_borrow) == 1 :
        return True
    else :
      for i in range(len(gadget_borrow)) :
        if gadget_borrow[i][2] == Item and gadget_borrow[i][5] == False :
          found = found + 1
    
    if found > 0 :
        return False
    else :
        return True

def write_gadget_borrow_history(Item, Tanggal, Jumlah, id_user, id_item):
    # Mengubah jumlah gadget di gadget.csv
    (gadget[id_item][3]) = (gadget[id_item][3]) - Jumlah

    # Menulis riwayat peminjaman gadget
    arr = [0 for i in range (6)]
    if len(gadget_borrow) == 1 : 
        arr[0] = 1
    else : 
        arr[0] = gadget_borrow[len(gadget_borrow)-1][0] + 1

    arr[1] = id_user
    arr[2] = Item
    arr[3] = Tanggal #datetime.datetime.strptime(Tanggal, '%d/%m/%Y')
    arr[4] = Jumlah
    arr[5] = False
    gadget_borrow.append(arr)

def pesan_kesalahan(Item, Tanggal, Jumlah) :
    if (validasi_item(Item)) == False :
        print('ID item yang Anda masukan tidak ada dalam Inventory')
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

def pinjam(user_now) :
  id_user = user_now['id']
  if validasi_role(user_now) :
      Item = input("Masukkan ID item : ")
      Tanggal = str(input("Tanggal peminjaman : "))
      Jumlah = int(input("Jumlah peminjaman : "))
      print()
      pesan_kesalahan(Item, Tanggal, Jumlah)

      while (not(validasi_item(Item)) or (validasi_tanggal(Tanggal) == False) or not(validasi_jumlah(Jumlah))) :
        print()
        Item = input("Masukkan ID item : ")
        Tanggal = str(input("Tanggal peminjaman : "))
        Jumlah = int(input("Jumlah peminjaman : "))
        print()
        pesan_kesalahan(Item, Tanggal, Jumlah)

      id_item = 0
      for i in range (len(gadget)) :
          if gadget[i][0] == Item :
              id_item = i

      if cek_peminjaman(Item) :
          if ((gadget[id_item][3]) >= Jumlah) :
              print("Item", gadget[id_item][1], "(x"+str(Jumlah)+") berhasil dipinjam!")
              
              write_gadget_borrow_history(Item, Tanggal, Jumlah, id_user, id_item)
          else :
              print("Gadget", gadget[id_item][1], "hanya tersisa", gadget[id_item][3], "buah.")

      else :
          print("Gadget", gadget[id_item][1], "sudah Anda dipinjam,")
          print("Anda tidak dapat meminjam lagi pada saat yang sama")
  else :
    print("Anda tidak dapat mengakses bagian ini")