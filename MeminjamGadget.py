from datetime import datetime

global user
global gadget
global gadget_borrow
global gadget_return
global header_user
global header_gadget
global header_gadget_borrow
global header_gadget_return


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
      datetime.strptime(Tanggal, '%d/%m/%Y')
      return True
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
    if len(gadget_borrow) == 0 :
        return True
    else :
        for i in range (len(gadget_borrow)) :
          if gadget_borrow[i][2] == Item and gadget_borrow[i][5] == False :
              found = found + 1
    
        if found > 0 :
            return False
        else :
            return True

def write_gadget_borrow_history(Item, Tanggal, Jumlah, id_user, id_item, gadget_borrow, gadget):
    # Mengubah jumlah gadget di gadget.csv
    (gadget[id_item][3]) = (gadget[id_item][3]) - Jumlah

    # Menulis riwayat peminjaman gadget
    arr = [0 for i in range (6)]
    if len(gadget_borrow) == 0 : 
        arr[0] = 1
    else : 
        index = (len(gadget_borrow)) - 1
        arr[0] = (gadget_borrow[index][0]) + 1

    arr[1] = id_user
    arr[2] = Item
    arr[3] = datetime.strptime(Tanggal, '%d/%m/%Y')
    arr[4] = Jumlah
    arr[5] = False
    gadget_borrow.append(arr)

def pesan_kesalahan(Item, Tanggal, Jumlah) :
    if (validasi_item(Item)) == False :
        print('ID item yang Anda masukan tidak ada dalam Inventory.')
        if (validasi_tanggal(Tanggal)) == False :
            print('Tanggal yang Anda masukan tidak sesuai.')
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')
                print()
        else :
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')
                print()
    else :
        if (validasi_tanggal(Tanggal)) == False :
            print('Tanggal yang Anda masukan tidak sesuai.')
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')
                print()
        else :
            if (validasi_jumlah(Jumlah)) == False :
                print('Jumlah yang Anda masukan tidak sesuai.')
                print()

# ALGORITMA UTAMA

def pinjam(user_now, gadget, gadget_borrow) :
  id_user = user_now['id']
  if validasi_role(user_now) :
      Item = input("Masukkan ID item : ")
      Tanggal = str(input("Tanggal peminjaman : "))
      Jumlah = int(input("Jumlah peminjaman : "))
      print()
       
      if (validasi_item(Item)) and (validasi_tanggal(Tanggal)) and (validasi_jumlah(Jumlah)) :
          id_item = 0
          for i in range (len(gadget)) :
              if gadget[i][0] == Item :
                  id_item = i

          if cek_peminjaman(Item) :
              if ((gadget[id_item][3]) >= Jumlah) :
                  print("Item", gadget[id_item][1], "(x"+str(Jumlah)+") berhasil dipinjam!")
                  
                  write_gadget_borrow_history(Item, Tanggal, Jumlah, id_user, id_item, gadget_borrow, gadget)
              else :
                  print("Item", gadget[id_item][1], "hanya tersisa", gadget[id_item][3], "buah.")

          else :
              print("Item", gadget[id_item][1], "sudah Anda pinjam.")
              print("Anda tidak dapat meminjam lagi pada saat ini")
      else :
          pesan_kesalahan(Item, Tanggal, Jumlah)
  else :
      print("Anda tidak dapat mengakses bagian ini")