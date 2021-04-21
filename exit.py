def exit() :
    Pilihan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah di ubah? (Y/N)"))
    if Pilihan == "Y" or Pilihan == "y" :
        save_data(pre_save_data(user), './file_csv/user.csv')
        save_data(pre_save_data(gadget), './file_csv/gadget.csv')
        save_data(pre_save_data(gadget_borrow), './file_csv/gadget_borrow_history.csv')
        save_data(pre_save_data(gadget_return), './file_csv/gadget_return_history.csv')
        save_data(pre_save_data(consumable), './file_csv/consumable.csv')
        save_data(pre_save_data(consumables_history), './file_csv/consumable_history.csv')
    else :
        # ini isi apa yaaa