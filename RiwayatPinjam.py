from datetime import datetime

def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False


def cariNamaPengambil(id_peminjam):
  nama=''
  for item in user:
    if item[0]==id_peminjam:
      nama=item[2]
  
  return nama

def cariSatu(satu):
  nama = cariNamaPengambil(satu[1])

  print(nama)

# for i in range (len(gadget_borrow)):
#   cariSatu(gadget_borrow[i])

def riwayatpinjam(user_now):
  global user
  global gadget
  global gadget_return
  global gadget_borrow

  global header_user
  global header_gadget
  global header_gadget_return
  global header_gadget_borrow

  gadget_borrow = sorted(gadget_borrow, key=lambda x:x[3], reverse=True)

  if validasi_role(user_now):
        if (len(gadget_borrow)>=5):
              for z in range(5):

                    # namaconsumable = 0
                    # for i in range(len(consumable)):
                    #       if (consumable[i][0] == consumable_history[z][2]):
                    #             namaconsumable = i

                    namagadget = 0
                    for i in range(len(gadget)):
                          if (gadget[i][0] == gadget_borrow[z][2]):
                                namagadget = i
                    print("")
                    print("ID Peminjaman        :", gadget_borrow[z][0])
                    print("Nama Pengambil       :", cariNamaPengambil(gadget_borrow[z][1]))
                    print("Nama Gadget          :", gadget[namagadget][1])
                    print("Tanggal Peminjaman   :", datetime.strftime(gadget_borrow[z][3], '%d/%m/%Y'))
                    print("Jumlah               :", gadget_borrow[z][4])
                    
              z += 1
              nomorlooping = z
              sisalooping = len(gadget_borrow) - nomorlooping 
              
              while nomorlooping < len(gadget_borrow):
                    print("")
                    lanjut = input("Apakah mau menampilkan data lebih lanjut? (Y/N) : ")
                    if lanjut == "Y":
                          if (sisalooping>=5):
                                for z in range(5):  
                                      namagadget = 0
                                      for i in range(len(gadget)):
                                            if (gadget[i][0] == gadget_borrow[nomorlooping][2]):
                                                  namagadget = i
                                      namauser = 0
                                      for i in range(len(user)):
                                            if (user[i][0] == gadget_borrow[nomorlooping][1]):
                                                  namauser = i
                                      print("")
                                      print("ID Peminjaman        :", gadget_borrow[nomorlooping][0])
                                      print("Nama Pengambil       :", cariNamaPengambil(gadget_borrow[nomorlooping][1]))
                                      print("Nama Gadget          :", gadget[namagadget][1])
                                      print("Tanggal Peminjaman   :", datetime.strftime(gadget_borrow[nomorlooping][3], '%d/%m/%Y'))
                                      print("Jumlah               :", gadget_borrow[nomorlooping][4])
                                      nomorlooping += 1
                          else:
                                for z in range(sisalooping): 
                                      namagadget = 0
                                      for i in range(len(gadget)):
                                            if (gadget[i][0] == gadget_borrow[nomorlooping][2]):
                                                  namagadget = i
                                      namauser = 0
                                      for i in range(len(user)):
                                            if (user[i][0] == gadget_borrow[nomorlooping][1]):
                                                  namauser = i
                                      print("")
                                      print("ID Peminjaman        :", gadget_borrow[nomorlooping][0])
                                      print("Nama Pengambil       :", cariNamaPengambil(gadget_borrow[nomorlooping][1]))
                                      print("Nama Gadget          :", gadget[namagadget][1])
                                      print("Tanggal Peminjaman   :", datetime.strftime(gadget_borrow[nomorlooping][3], '%d/%m/%Y'))
                                      print("Jumlah               :", gadget_borrow[nomorlooping][4])
                  
                                      nomorlooping += 1
                                print("")
                    else:
                          break            
        else:
              for z in range(len(gadget_borrow)):  
                      namagadget = 0
                      for i in range(len(gadget)):
                              if (gadget[i][0] == gadget_borrow[z][2]):
                                  namagadget = i
                      namauser = 0
                      for i in range(len(user)):
                              if (user[i][0] == gadget_borrow[z][1]):
                                  namauser = i
                      print("")
                      print("ID Peminjaman        :", gadget_borrow[z][0])
                      print("Nama Pengambil       :", cariNamaPengambil(gadget_borrow[z][1]))
                      print("Nama Gadget          :", gadget[namagadget][1])
                      print("Tanggal Peminjaman   :",datetime.strftime(gadget_borrow[z][3], '%d/%m/%Y'))
                      print("Jumlah               :", gadget_borrow[z][4])
        print("")
    else :
        print("Anda tidak dapat mengakses bagian ini.")