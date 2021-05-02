import sys

from register import register                           #F01
from login import login                                 #F02
from PencarianRarity import carirarity                  #F03
from PencarianTahun import caritahun                    #F04
from MenambahItem import tambahitem                     #F05
from MenghapusItem import hapusitem                     #F06
from MengubahItem import ubahjumlah                     #F07
from MeminjamGadget import pinjam                       #F08
from MengembalikanGadget import kembalikan              #F09
from MemintaConsumable import minta                     #F10
from RiwayatPinjam import riwayatpinjam                 #F11
from RiwayatKembali import riwayatkembali               #F12
from RiwayatAmbil import riwayatambil                   #F13
# from load import loader                                 #F14, dipakai di file variabel.py
from save import save                                   #F15
from help import help                                   #F16
from exit import exit                                   #F17
from variabel import choice,user,gadget,gadget_borrow,gadget_return,consumable,consumable_history,header_user,header_gadget,header_gadget_borrow,header_gadget_return,header_consumable,header_consumable_history,user_now


def pilihan_program(choice) :
  if choice == 'register' :
      register(user,user_now)
  elif choice == 'carirarity' :
      carirarity(gadget)
  elif choice == 'caritahun' :
      caritahun(gadget)
  elif choice == 'tambahitem' :
      tambahitem(user_now, gadget, consumable)
  elif choice == 'hapusitem' :
      hapusitem(user_now, gadget, consumable)
  elif choice == 'ubahjumlah' :
      ubahjumlah(user_now, gadget, consumable)
  elif choice == 'pinjam' :
      pinjam(user_now, gadget, gadget_borrow)
  elif choice == 'kembalikan' :
      kembalikan(user_now, gadget, gadget_return, gadget_borrow)
  elif choice == 'minta' :
      minta(user_now, consumable, consumable_history)
  elif choice == 'riwayatpinjam' :
      riwayatpinjam(user_now)
  elif choice == 'riwayatkembali' :
      riwayatkembali(user_now)
  elif choice == 'riwayatambil' :
      riwayatambil(user_now)
  elif choice == 'save':
    save(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history)
  elif choice == 'help' :
      help()
  elif choice == 'exit' :
      exit(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history)
  else :
    print("Pilihan tidak ada dalam sistem kantongajaib")

user_now['id'], user_now['role'], user_now['name'] = login(user)
print()

print('Halo', user_now['name'],'!')
print()

choice = input('>>> ')
pilihan_program(choice)
while choice != 'exit':
  choice = input('>>> ')
  pilihan_program(choice)