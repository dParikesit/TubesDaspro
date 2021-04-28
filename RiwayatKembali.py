from load import load_data
from datetime import datetime

user=[]
gadget = []
gadget_borrow = []
gadget_return = []

header_user = []
header_gadget = []
header_gadget_borrow = []
header_gadget_return = []

load_data(gadget, header_gadget, './file_csv/gadget.csv')
load_data(gadget_return, header_gadget_return, './file_csv/gadget_return_history.csv')
load_data(gadget_borrow, header_gadget, './file_csv/gadget_borrow_history.csv')
load_data(user, header_user, './file_csv/user.csv')

gadget_return = sorted(gadget_return, key=lambda x:x[2], reverse=True)

# print(gadget_return)

def riwayatpinjam():
      if (len(gadget_return)>=5):
            for z in range(5):  
              
              namagadget = 0

              for i in range(len(gadget)):
                    if (gadget[i][0] == gadget_return[z][1]):
                          namagadget = i

              print("")
              print("ID Pengembalian      :", gadget_return[z][0])
              print("Nama Pengambil       :", user[z][gadget_return[1][1]])
              print("Nama Gadget          :", gadget[namagadget][1])
              print("Tanggal Peminjaman   :", gadget_return[z][3])
              print("Jumlah               :", gadget_return[z][4])
              
            z += 1
            nomorlooping = z
            sisalooping = len(gadget_return) - nomorlooping 
            
            while nomorlooping < len(gadget_return):
              print("")
              lanjut = input("Apakah mau menampilkan data lebih lanjut? (Y/N) : ")
              if lanjut == "Y":
                if (sisalooping>=5):
                  for z in range(5):  
                    namagadget = 0
                    for i in range(len(gadget)):
                            if (gadget[i][0] == gadget_return[nomorlooping][1]):
                                namagadget = i
                    namauser = 0
                    for i in range(len(user)):
                            if (user[i][0] == gadget_return[nomorlooping][1]):
                                namauser = i

                    print("")
                    print("ID Pengembalian      :", gadget_return[nomorlooping][0])
                    print("Nama Pengambil       :", user[namauser][gadget_return[1][1]])
                    print("Nama Gadget          :", gadget[namagadget][1])
                    print("Tanggal Peminjaman   :", gadget_return[nomorlooping][3])
                    print("Jumlah               :", gadget_return[nomorlooping][4])

                    nomorlooping += 1
                else:
                  for z in range(sisalooping): 
                    namagadget = 0
                    for i in range(len(gadget)):
                            if (gadget[i][0] == gadget_return[nomorlooping][1]):
                                namagadget = i
                    namauser = 0
                    for i in range(len(user)):
                            if (user[i][0] == gadget_return[nomorlooping][1]):
                                namauser = i

                    print("")
                    print("ID Pengembalian      :", gadget_return[nomorlooping][0])
                    print("Nama Pengambil       :", user[namauser][gadget_return[1][1]])
                    print("Nama Gadget          :", gadget[namagadget][1])
                    print("Tanggal Peminjaman   :", gadget_return[nomorlooping][3])
                    print("Jumlah               :", gadget_return[nomorlooping][4])
                    nomorlooping += 1
                print("")
              else:
                break            
      else:
            for z in range(len(gadget_return)):  
                    namagadget = 0
                    for i in range(len(gadget)):
                            if (gadget[i][0] == gadget_return[z][1]):
                                namagadget = i
                    namauser = 0
                    for i in range(len(user)):
                            if (user[i][0] == gadget_return[z][1]):
                                namauser = i

                    print("")
                    print("ID Pengembalian      :", gadget_return[z][0])
                    print("Nama Pengambil       :", user[namauser][gadget_return[0][0]])
                    print("Nama Gadget          :", gadget[namagadget][1])
                    print("Tanggal Peminjaman   :", gadget_return[z][3])
                    print("Jumlah               :", gadget_return[z][4])
      print("")

riwayatpinjam()
