from datetime import datetime 
from variabel import consumable

def validasi_item(Item) :
    found = False
    for i in range (len(consumable)) :
      if consumable[i][0] == Item :
          found = True

    if Item[0] == "C" and found == True :
      return True
    else :
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

def validasi_tanggal(Tanggal):
    try:
      datetime.strptime(Tanggal, '%d/%m/%Y')
      return True
    except ValueError :
      return False

def write_consumable_history(Item, Tanggal, Jumlah, id_user, id_item, consumable, consumable_history) :
    consumable[id_item][3] = (consumable[id_item][3]) - Jumlah
    
    # Menulis riwayat pemakaian consumable
    arr = [0 for i in range (5)]

    if len(consumable_history) == 0 : 
        arr[0] = 1
    else : 
        index = (len(consumable_history)) - 1
        arr[0] = consumable_history[index][0] + 1
  
    arr[1] = id_user
    arr[2] = Item
    arr[3] = datetime.strptime(Tanggal, '%d/%m/%Y')
    arr[4] = Jumlah
    consumable_history.append(arr)


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

def minta(user_now, consumable, consumable_history) :
  id_user = user_now['id']

  if validasi_role(user_now) :
      Item = str(input("Masukan id item : "))
      Jumlah = int(input("Jumlah : "))
      Tanggal = str(input("Tanggal permintaan :"))
      print()

      if (validasi_item(Item)) and (validasi_jumlah(Jumlah)) and (validasi_tanggal(Tanggal)) :
          id_item = 0
          for i in range (len(consumable)) :
              if consumable[i][0] == Item :
                  id_item = i

          if consumable[id_item][3] >= Jumlah :
              print("Item", consumable[id_item][1], "(x"+str(Jumlah)+") telah berhasil diambil!")

              write_consumable_history(Item, Tanggal, Jumlah, id_user, id_item,consumable, consumable_history)
          else :
              if consumable[id_item][3] == 0 :
                  print("Item", consumable[id_item][1], "telah habis :(.")
              else :
                  print("Item", consumable[id_item][1], "hanya tersisa", consumable[id_item][3], "buah.")
      else :
          pesan_kesalahan(Item, Tanggal, Jumlah)
    
  else :
      print("Anda tidak dapat mengakses bagian ini")