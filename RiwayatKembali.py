from load import load_data
from datetime import datetime

global user
global gadget
global gadget_return
global gadget_borrow

global header_user
global header_gadget
global header_gadget_return
global header_gadget_borrow

def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False

gadget_return = sorted(gadget_return, key=lambda x:x[2], reverse=True)

def cariIdPeminjam(id_peminjaman):
  id_peminjam = 0
  for item in gadget_borrow:
    if item[0]==id_peminjaman:
      id_peminjam = item[1]
  
  return id_peminjam

def cariNamaPengambil(id_peminjam):
  nama = ''
  for item in user:
    if item[0]==id_peminjam:
      nama = item[2]
  
  return nama

def cariIdGadget(id_peminjaman):
  id_gadget = 0
  for item in gadget_borrow:
    if item[0]==id_peminjaman:
      id_gadget = item[2]
  
  return id_gadget

def cariNamaGadget(id_gadget):
  nama = ''
  for item in gadget:
    if item[0]==id_gadget:
      nama = item[1]
  
  return nama

def tampilinsatu (satu):
  id_peminjaman = satu[1]
  nama_pengambil = cariNamaPengambil(cariIdPeminjam(id_peminjaman))
  nama_gadget = cariNamaGadget(cariIdGadget(id_peminjaman))
  tanggal = datetime.strftime(satu[2], '%d/%m/%Y')
  jumlah = satu[3]

  print("ID Peminjaman        : " + str(id_peminjaman))
  print("Nama Pengambil       : " + nama_pengambil)
  print("Nama Gadget          : " + nama_gadget)
  print("Tanggal Pengembalian : " + str(tanggal))
  print("Jumlah               : " + str(jumlah))
  print()

def riwayatkembali(user_now):
  if validasi_role(user_now):
    if(len(gadget_return)>=5):
      for i in range(5):
        tampilinsatu(gadget_return[i])
      nomorlooping = i+1
      sisalooping = len(gadget_return) - nomorlooping
      while(nomorlooping<=len(gadget_return)):
        print("")
        lanjut = input("Apakah mau menampilkan data lebih lanjut? (Y/N) : ")
        if lanjut == "Y":
          if (sisalooping>=5):
            for z in range(5):
              tampilinsatu(gadget_return[nomorlooping])
              nomorlooping += 1
          else:
            for z in range(sisalooping):
              tampilinsatu(gadget_return[nomorlooping])
            break
        else:
          break
        sisalooping = len(gadget_return) - nomorlooping
    else:
      for i in range(len(gadget_return)):
        tampilinsatu(gadget_return[i])
  else :
    print("Anda tidak dapat mengakses bagian ini.")
