''' from load import load_data
from save import save_data


gadget = []
load_data(gadget, './file_csv/gadget.csv')
gadget.pop(0) # Nanti gausah ditulis karena bakal masuk ke fungsi load data


for data in gadget:
  if data[5]<2000: # data[5] ini maksudnya yang tahun
    print(data[5])


id = ['G1', 'G2', 'G3', 'G1']
unique_id = list(set(id))
print(unique_id) 

consumable_history = []
header_consumable_history = []

load_data(consumable_history, header_consumable_history, './file_csv/consumable_history.csv')

print(consumable_history)

# Akses tanggal bulan tahun
from datetime import date
print(consumable_history[0][3].day)
print(consumable_history[0][3].month)
print(consumable_history[0][3].year)

print(type(consumable_history[0][3].day))
print(type(consumable_history[0][3].month))
print(type(consumable_history[0][3].year)) '''


''' # RACHMAD
from datetime import datetime
tanggal = '01/01/2021'

arr = [0 for i in range (1)]

def is_datetime(tanggal):
  try:
    datetime.strptime(tanggal, '%d/%m/%Y')
    return True
  except ValueError:
    return False

print(is_datetime(tanggal))

tanggal_datetime = datetime.strptime(tanggal, '%d/%m/%Y')
arr[0] = tanggal_datetime
print(arr)
print(arr[0].day) '''


from datetime import datetime

arr = [[1, 1, 'G1', '12/03/2009', 1, 'True'], [2, 2, 'G6', '21/11/2017', 4, 'False'], [3, 3, 'G567', '22/11/2018', 2, 'True'], [4, 4, 'G90', '22/11/2020', 2, 'True'], [5, 5, 'G6', '22/11/1980', 2, 'True'], [6, 6, 'G90', '22/11/2201', 2, 'True'], [7, 2, 'G90', '21/11/2019', 2, 'True']]

# def is_datetime(tanggal):
#   try:
#     datetime.strptime(tanggal, '%d/%m/%Y')
#     return True
#   except ValueError:
#     return False

# for i in range(len(arr)):
#   print(arr[i][3])
#   if is_datetime(arr[i][3]):
#     arr[i][3] = datetime.strptime(arr[i][3], '%d/%m/%Y')

arr = sorted(arr, key=lambda x: datetime.strptime(x[3], "%d/%m/%Y").strftime("%Y-%m-%d"))

print(arr)

#CONTOH SORTING

#CONTOH 1
# c_array=[[1, '07/12/2017'], [2, '30/01/2018'],[5,'31/05/2016'], [3, '30/09/2016'], [4,'30/01/2017'], [6, '31/05/2017']]

# c_array = sorted(c_array, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y").strftime("%Y-%m-%d"), reverse = True)

# print(c_array)

#CONTOH 2
# list = [['G', 10], ['A', 22], ['S', 1], ['P', 14], ['V', 13], ['T', 7], ['C', 0], ['I', 219]]

# list = sorted(lst, key=lambda x: x[1], reverse=True)

# print(list)
