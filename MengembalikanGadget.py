from datetime import datetime

global gadget
global gadget_borrow
global gadget_return
global header_gadget
global header_gadget_borrow
global header_gadget_return


def validasi_role(user_now):
    if user_now['role'] == "User":
        return True
    else:
        return False

def validasi_tanggal(Tanggal):
    try:
        datetime.strptime(Tanggal, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validasi_jumlah(Jumlah, id_peminjaman, gadget_return, gadget_borrow):
    Jumlah_kembali = 0
    for i in range(len(gadget_return)):
        if id_peminjaman == gadget_return[i][1]:
            Jumlah_kembali = Jumlah_kembali + gadget_return[i][3]

    Jumlah_pinjam = 0
    for i in range(len(gadget_borrow)):
        if id_peminjaman == gadget_borrow[i][0]:
            Jumlah_pinjam = gadget_borrow[i][4]
    
    if Jumlah > 0 and Jumlah <= (Jumlah_pinjam - Jumlah_kembali):
        return True
    else:
        return False


def validasi_no_item(Item_nomor, arr_id_peminjaman):
    if Item_nomor > 0 and Item_nomor <= (len(arr_id_peminjaman)):
        return True
    else:
        return False


def id_peminjaman_user(id_user, gadget_borrow):
    arr_id_peminjaman_raw = [0 for i in range(len(gadget_borrow))]
    arr = []
    for i in range(len(gadget_borrow)):
        if gadget_borrow[i][1] == id_user and gadget_borrow[i][5] == False:
            arr_id_peminjaman_raw[i] = gadget_borrow[i][0]
        else:
            arr_id_peminjaman_raw[i] = 0

    for i in range(len(arr_id_peminjaman_raw)):
        if arr_id_peminjaman_raw[i] != 0:
            arr.append(arr_id_peminjaman_raw[i])

    return arr


def id_item_user(id_user, gadget_borrow):
    arr_id_item_raw = [0 for i in range(len(gadget_borrow))]
    arr = []
    for i in range(len(gadget_borrow)):
        if gadget_borrow[i][1] == id_user and gadget_borrow[i][5] == False:
            arr_id_item_raw[i] = gadget_borrow[i][2]
        else:
            arr_id_item_raw[i] = 0

    for i in range(len(arr_id_item_raw)):
        if arr_id_item_raw[i] != 0:
            arr.append(arr_id_item_raw[i])

    return arr


def tulis_item(Item, i):
    for k in range(len(gadget)):
        if gadget[k][0] == Item:
            IdItem = k
    print(str(i + 1) + ".", gadget[IdItem][1])


def write_gadget_return_history(id_peminjaman, Tanggal, Jumlah, gadget_return):
    arr = [0 for i in range(4)]

    if len(gadget_return) == 0 : 
        arr[0] = 1
    else : 
        index = (len(gadget_return)) - 1
        arr[0] = (gadget_return[index][0]) + 1

    arr[1] = id_peminjaman
    arr[2] = datetime.strptime(Tanggal, '%d/%m/%Y')
    arr[3] = Jumlah
    gadget_return.append(arr)


def ubah_data(Item, Jumlah, id_peminjaman, gadget_borrow, gadget):
    # Mengubah jumlah gadget pada data gadget.csv
    for i in range(len(gadget)):
        if gadget[i][0] == Item:
            gadget[i][3] = gadget[i][3] + Jumlah

    # Mengubah is_returned pada data gadget_borrow_history.csv
    Index = 0
    for i in range(len(gadget_borrow)):
        if gadget_borrow[i][0] == id_peminjaman:
            Index = i

    Jumlah_kembali = Jumlah
    for i in range(len(gadget_return)):
        if gadget_return[i][1] == id_peminjaman:
            Jumlah_kembali = Jumlah_kembali + gadget_return[i][3]

    if Jumlah_kembali == gadget_borrow[Index][4]:
        gadget_borrow[Index][5] = True


def pesan_kesalahan(Tanggal, Jumlah,id_peminjaman, gadget_return, gadget_borrow):
    if (validasi_tanggal(Tanggal)) == False:
        print('Tanggal yang Anda masukan tidak sesuai.')
        if (validasi_jumlah(Jumlah, id_peminjaman, gadget_return, gadget_borrow)) == False:
            print('Jumlah yang Anda masukan tidak sesuai.')
        else:
            if (validasi_jumlah(Jumlah, id_peminjaman, gadget_return, gadget_borrow)) == False:
                print('Jumlah yang Anda masukan tidak sesuai.')
    else:
        if (validasi_jumlah(Jumlah, id_peminjaman,gadget_return, gadget_borrow)) == False:
            print('Jumlah yang Anda masukan tidak sesuai.')

# ALGORITMA UTAMA


def kembalikan(user_now, gadget, gadget_return, gadget_borrow):
    id_user = user_now['id']

    if validasi_role(user_now):

        arr_id_peminjaman = id_peminjaman_user(id_user, gadget_borrow)
        arr_id_item = id_item_user(id_user, gadget_borrow)

        if len(arr_id_peminjaman) == 0:
            print("Anda tidak meminjam barang apapun.")
        else:
            print('===== ITEM YANG DIPINJAM =====')
            for i in range(len(arr_id_item)):
                Item = arr_id_item[i]
                tulis_item(Item, i)

            Item_nomor = int(input("Masukan nomor peminjaman : "))
            Tanggal = str(input("Tanggal pengembalian : "))
            Jumlah = int(input("Jumlah : "))

            if (validasi_no_item(Item_nomor, arr_id_peminjaman)) :
                id_peminjaman = arr_id_peminjaman[Item_nomor - 1]

                if (validasi_tanggal(Tanggal)) and (validasi_jumlah(Jumlah, id_peminjaman, gadget_return, gadget_borrow)):

                    Item = arr_id_item[Item_nomor - 1]

                    write_gadget_return_history(id_peminjaman, Tanggal, Jumlah, gadget_return)
                    
                    ubah_data(Item, Jumlah, id_peminjaman, gadget_borrow, gadget)

                    for i in range(len(gadget)):
                        if Item == gadget[i][0]:
                            Nama = gadget[i][1]

                    print("Item " + str(Nama) + "(x" + str(Jumlah) +
                          ") telah dikembalikan.")
                else:
                    pesan_kesalahan(Tanggal, Jumlah, id_peminjaman, gadget_return, gadget_borrow)
            else :
                print('Nomor peminjaman yang Anda masukan tidak sesuai.')

    else:
        print("Anda tidak dapat mengakses bagian ini.")
