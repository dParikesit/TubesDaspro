def gacha(user_now, consumable):
  if validasi_role(user_now) :
      print("===== INVENTORY =====")

      for i in range (len(consumable)) :
        print(str(i)+'. '+consumable[i][1]+" (Rarity "+consumable[i][4]+") ("+consumable[i][3])

  else :
      print("Anda tidak dapat mengakses bagian ini.")
