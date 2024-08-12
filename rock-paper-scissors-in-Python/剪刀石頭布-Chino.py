import random
import time
import os
pc=control= 0
usario=st=5
lista = ["離開","石頭✊","剪刀✌","布🤚"]
def sleeptime (controltime):
  while (controltime!=0):
    print(end=" 等待{}秒後繼續\r".format(controltime) )
    time.sleep(1) 
    controltime-=1
#開始進入
while(usario!=0):
    control=0  
     # 控制用戶輸入的數值是 1,2,3
    while (control!=1):
      os.system('cls')
      print (" 這是與電腦玩{}、{}、{}的遊戲 ".format(lista[1],lista[2],lista[3]))
      usario=input("\n 1. {} \n 2. {} \n 3. {} \n 0. {}\n\n  請選擇： ".format(lista[1],lista[2],lista[3],lista[0]))
      if (str.isdigit(usario)): # 判斷用戶輸入的是否為數值
        usario=int(usario)
      if (not((usario == 1)or(usario == 2)or(usario == 3)or(usario == 0))):
        print("\n 請輸入正確的數值\n")
        #等待st秒後繼續
        sleeptime (2)
        
      else:control=1
      #用戶輸入的數值是 1,2,3, 開始進程
      if ((usario == 1)or(usario == 2)or(usario == 3)):
        print ( f"\n 您選擇：{lista[usario]}" )
        pc = random.randint(1,3)  #電腦隨機生成1-3的值
        print ( f"\n 電腦選擇 ：{lista[pc]} ");
        if (usario == pc):
            print ("\n 平手\n" )
            sleeptime (st)
        else:
            if ((usario == 1 and pc == 2) or(usario == 2 and pc == 3) or(usario == 3 and pc == 1)):
              print ("\n 玩家贏了\n")
              sleeptime (st)
            else: 
              print ("\n 電腦贏了\n" )
              sleeptime (st)
print ( f"\n 您選擇：{lista[usario]}\n" )
input ("\n祝您玩得愉快 , 歡迎再來玩\n\n按 ENERT 離開\n")

