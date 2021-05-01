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

# def validasi_role(user_now) :
#     if user_now['role'] == "Admin" :
#       return True
#     else :
#       return False

gadget_return = sorted(gadget_return, key=lambda x:x[2])

###########################################################

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

def riwayatkembali():
  if(len(gadget_return)>=5):
      while
  else:
    for i in range()

riwayatkembali()