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


def validasi_item(Item) :
    if Item[0] == "G" :
      return True
    else :
      return False

def validasi_tanggal(Tanggal):
    try:
      datetime.datetime.strptime(Tanggal, '%d/%m/%Y')
    except ValueError :
      return False

def validasi_riwayat(id_user, Item) :
    found = 0
    Jumlah_pinjam = 0
    Jumlah_kembali = 0
    for i in range (len(gadget_borrow)) :
      if gadget_borrow[i][1]== id_user and gadget_borrow[i][2] == Item:
         found = found + 1
         Jumlah_pinjam = Jumlah_pinjam + (gadget_borrow[i][4])

    for i in range (len(gadget_return)) :
      if gadget_return[i][1]== id_user and gadget_return[i][1] == Item :
         Jumlah_kembali = Jumlah_kembali + (gadget_return[i][4])

    if found > 0 :
        if Jumlah_pinjam == Jumlah_kembali :
            return True
        else :
            return False
    else :
        return True

def write_gadget_borrow_history(Item, Tanggal, Jumlah, id_user) :
    arr = [0 for i in range (5)]
    arr[0] = gadget_borrow[len(gadget_borrow)][0] + 1
    arr[1] = id_user
    arr[2] = Item
    arr[3] = Tanggal
    arr[4] = Jumlah
    gadget_borrow.append(arr)

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

def validasi_input(Item,Tanggal,Jumlah) :
  if validasi_item(Item) and validasi_tanggal(Tanggal) and validasi_jumlah(Jumlah) :
      return True
  else :
      return False

# ALGORITMA UTAMA

def pinjam(user_now) :
  id_user = user_now['id']
  if validasi_role(user_now) :
    Item = str(input("Masukkan ID item : "))
    Tanggal = str(input("Tanggal peminjaman : "))
    Jumlah = int(input("Jumlah peminjaman : "))

    while (not(validasi_input)) :
      print("Masukan tidak sesuai. Ulangi!")
      Item = input("Masukkan ID item : ")
      Tanggal = str(input("Tanggal peminjaman : "))
      Jumlah = int(input("Jumlah peminjaman : "))

    IdItem = 0
    # Mengecek apakah gadget sudah di pinjam
    if validasi_riwayat(id_user, Item) :
        # Mencari Index
        for i in range (len(gadget)) :
            if gadget[i][0] == Item :
                IdItem = i

        if ((gadget[IdItem][3]) >= Jumlah) :
            print("Item", gadget[IdItem][1], "(x"+str(Jumlah)+") berhasil dipinjam!")
            (gadget[IdItem][3]) = (gadget[IdItem][3]) - Jumlah

            write_gadget_borrow_history(Item, Tanggal, Jumlah, id_user)
        else :
            print("Gadget", gadget[IdItem][1], "hanya tersisa", gadget[IdItem][3], "buah.")

    else :
        print("Gadget", gadget[IdItem][1], "sudah Anda dipinjam,")
        print("Anda tidak dapat meminjam lagi pada saat yang sama")
  else :
    print("Anda tidak dapat mengakses bagian ini")