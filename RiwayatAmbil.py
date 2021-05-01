from load import load_data
from datetime import datetime

user=[]
gadget = []
consumable_history = []
gadget_return = []
consumable = []
consumable_history = []


header_user = []
header_gadget = []
header_consumable_history = []
header_gadget_return = []
header_consumable = []
header_consumable_history = []

load_data(gadget, header_gadget, './file_csv/gadget.csv')
load_data(consumable_history, header_consumable_history, './file_csv/consumable_history.csv')
load_data(gadget_return, header_gadget, './file_csv/gadget_return_history.csv')
load_data(user, header_user, './file_csv/user.csv')
load_data(consumable, header_consumable, './file_csv/consumable.csv')

def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False

consumable_history = sorted(consumable_history, key=lambda x: x[3], reverse=True)

def riwayatambil(user_now):
    if validasi_role(user_now) :
        if (len(consumable_history)>=5):
              for z in range(5):  
                    namaconsumable = 0
                    for i in range(len(consumable)):
                          if (consumable[i][0] == consumable_history[z][2]):
                                namaconsumable = i
                    namauser = 0
                    for i in range(len(user)):
                          if (user[i][0] == consumable_history[z][1]):
                                namauser = i
                    print("")
                    print("ID Pengambilan        :", consumable_history[z][0])
                    print("Nama Pengambil        :", user[namauser][2])
                    print("Nama Consumable       :", consumable[namaconsumable][1])
                    print("Tanggal Pengambilan   :", consumable_history[z][3])
                    print("Jumlah                :", consumable_history[z][4])
                    
                    print("")
                    print(z)
              z += 1
              nomorlooping = z
              sisalooping = len(consumable_history) - nomorlooping 
              
              while nomorlooping < len(consumable_history):
                    print("")
                    lanjut = input("Apakah mau menampilkan data lebih lanjut? (Y/N) : ")
                    if lanjut == "Y":
                          if (sisalooping>=5):
                                for z in range(5):  
                                      namaconsumable = 0
                                      for i in range(len(consumable)):
                                            if (consumable[i][0] == consumable_history[nomorlooping][2]):
                                                  namaconsumable = i
                                      namauser = 0
                                      for i in range(len(user)):
                                            if (user[i][0] == consumable_history[nomorlooping][1]):
                                                  namauser = i

                                      print("")
                                      print("ID Pengambilan       :", consumable_history[nomorlooping][0])
                                      print("Nama Pengambil       :", user[namauser][2])
                                      print("Nama Consumable      :", consumable[namaconsumable][1])
                                      print("Tanggal Pengambilan  :", consumable_history[nomorlooping][3])
                                      print("Jumlah               :", consumable_history[nomorlooping][4])

                                      print("")
                                      print(nomorlooping)

                                      nomorlooping += 1

                          else:
                                for z in range(sisalooping): 
                                      namaconsumable = 0
                                      for i in range(len(consumable)):
                                            if (consumable[i][0] == consumable_history[nomorlooping][2]):
                                                  namaconsumable = i
                                      namauser = 0
                                      for i in range(len(user)):
                                            if (user[i][0] == consumable_history[nomorlooping][1]):
                                                  namauser = i

                                      print("")
                                      print("ID Pengambilan       :", consumable_history[nomorlooping][0])
                                      print("Nama Pengambil       :", user[namauser][2] )
                                      print("Nama Consumable      :", consumable[namaconsumable][1])
                                      print("Tanggal Pengambilan  :", consumable_history[nomorlooping][3])
                                      print("Jumlah               :", consumable_history[nomorlooping][4])
                  
                                      nomorlooping += 1
                                print("")

                          sisalooping = len(consumable_history) - nomorlooping 
                    else:
                          break            
        else:
              for z in range(len(consumable_history)):  
                      namaconsumable = 0
                      for i in range(len(consumable)):
                              if (consumable[i][0] == consumable_history[z][2]):
                                  namaconsumable = i
                      namauser = 0
                      for i in range(len(user)):
                              if (user[i][0] == consumable_history[z][1]):
                                  namauser = i

                      print("")
                      print("ID Pengambilan        :", consumable_history[z][0])
                      print("Nama Pengambil        :", user[namauser][2] )
                      print("Nama Consumable       :", gadget[namaconsumable][1])
                      print("Tanggal Pengambilan   :", consumable_history[z][3])
                      print("Jumlah                :", consumable_history[z][4])
        print("")
    else :
        print("Anda tidak dapat mengakses bagian ini.")
