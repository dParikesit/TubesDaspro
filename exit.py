from save import batch_save

def exit(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history) :
    Pilihan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah di ubah? (Y/N)"))
    if Pilihan == "Y" or Pilihan == "y" :
      batch_save(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history)
    else :
        # ini isi apa yaaa
        pass