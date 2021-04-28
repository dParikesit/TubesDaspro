import sys

from register import register
from login import login
from load import batch_load, parser, path_loader
from PencarianRarity import carirarity                  #F03
from PencarianTahun import caritahun                    #F04
from MenambahItem import tambahitem                     #F05
from MengubahItem import ubahjumlah                     #F07
from MeminjamGadget import pinjam                       #F08
from MengembalikanGadget import kembalikan              #F09
from MemintaConsumable import minta                     #F10
from help import help                                   #F16
from exit import exit                                   #F17



# Bikin variabel buat storing data
choice = ''
user=[]
gadget=[]
gadget_borrow = []
gadget_return = []
consumable = []
consumable_history = []
header_user = []
header_gadget = []
header_gadget_borrow = []
header_gadget_return = []
header_consumable = []
header_consumable_history = []
user_now = {
  "id":-1,
  "role":'',
  "name":''
}

def pilihan_program(choice) :
  if choice == 'register' :
      register(user,user_now)
  elif choice == 'carirarity' :
      carirarity(gadget)
  elif choice == 'caritahun' :
      caritahun(gadget)
  elif choice == 'tambahitem' :
      tambahitem(user_now, gadget, consumable)
#  elif choice == 'hapusitem' :
  elif choice == 'ubahjumlah' :
    ubahjumlah(user_now, gadget, consumable)
  elif choice == 'pinjam' :
      pinjam(user_now, gadget, gadget_borrow)
  elif choice == 'kembalikan' :
      kembalikan(user_now, gadget, gadget_return, gadget_borrow)
  elif choice == 'minta' :
      minta(user_now, consumable, consumable_history)
# elif choice == 'riwayatpinjam' :
# elif choice == 'riwayatkembali' :
# elif choice == 'riwayatambil' :
  elif choice == 'help' :
      help()
  elif choice == 'exit' :
      exit(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history)
  else :
    print("Pilihan tidak ada dalam sistem kantongajaib")

path_link = parser()
if (path_loader(path_link) == True):
  batch_load(path_link, user, gadget, gadget_borrow, gadget_return,consumable, consumable_history, header_user, header_gadget,header_gadget_borrow, header_gadget_return, header_consumable,header_consumable_history)
  
  print('===== Selamat datang di "Kantong Ajaib" ! =====')
  print()
else:
  print('Tidak ada nama folder yang diberikan')
  print('Usage: python kantongajaib.py <nama_folder>')
  sys.exit()


user_now['id'], user_now['role'], user_now['name'] = login(user, input('Masukan username: '), input('Masukan password: '))
print()
while (user_now['id'] == -1 or user_now['role'] == ''):
  user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))
  print()

print('Halo', user_now['name'],'!')
print()

choice = input('>>> ')
pilihan_program(choice)
while choice != 'exit':
  choice = input('>>> ')
  pilihan_program(choice)