from load import load_data
from save import save_data

''' gadget = []
load_data(gadget, './file_csv/gadget.csv')
gadget.pop(0) # Nanti gausah ditulis karena bakal masuk ke fungsi load data


for data in gadget:
  if data[5]<2000: # data[5] ini maksudnya yang tahun
    print(data[5])


id = ['G1', 'G2', 'G3', 'G1']
unique_id = list(set(id))
print(unique_id) '''

consumable_history = []
header_consumable_history = []

load_data(consumable_history, header_consumable_history, './file_csv/consumable_history.csv')

# Akses tanggal bulan tahun
from datetime import date
print(consumable_history[0][3].day)
print(consumable_history[0][3].month)
print(consumable_history[0][3].year)

print(type(consumable_history[0][3].day))
print(type(consumable_history[0][3].month))
print(type(consumable_history[0][3].year))