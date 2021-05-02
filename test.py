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
load_data(gadget_borrow, header_gadget_borrow, './file_csv/gadget_borrow_history.csv')
load_data(gadget_return, header_gadget, './file_csv/gadget_return_history.csv')
load_data(user, header_user, './file_csv/user.csv')

def validasi_role(user_now) :
    if user_now['role'] == "Admin" :
      return True
    else :
      return False

gadget_borrow = sorted(gadget_borrow, key=lambda x:x[3], reverse=True)

def cariNamaPengambil(id_peminjam):
  nama=''
  for item in user:
    if item[0]==id_peminjam:
      nama=item[2]
  
  return nama

def cariSatu(satu):
  nama = cariNamaPengambil(satu[1])

  print(nama)

cariSatu(gadget_borrow[0])