from save import save

def exit(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history) :
    Pilihan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah di ubah? (Y/N)"))
    
    if Pilihan == "Y" or Pilihan == "y" :
      save(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history)
    else :
        pass