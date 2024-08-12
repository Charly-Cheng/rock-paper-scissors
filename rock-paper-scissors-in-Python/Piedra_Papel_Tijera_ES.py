import random
import time
import os
pc=control=contar_usario=contar_pc=contar_empate=contar_total= 0
usario=st=5
lista = ["Salir","Piedra✊","Tijera✌","Papel🤚"]
def sleeptime (controltime):
  while (controltime!=0):
    print(end=" Continuando en {} segundos\r".format(controltime) )
    time.sleep(1) 
    controltime-=1
#Empezamos
while(usario!=0):
    control=0  
     # Controla que el usuario ingrese 1,2,3
    while (control!=1):
      os.system('cls')
      print (" Este es el juego de {}、{}、{} ".format(lista[1],lista[2],lista[3]))
      usario=input("\n 1. {} \n 2. {} \n 3. {} \n 0. {}\n\n  Elige Por favor： ".format(lista[1],lista[2],lista[3],lista[0]))
      if (str.isdigit(usario)): # determina si el usuario ingreso un valor numerico
        usario=int(usario)
      if (not((usario == 1)or(usario == 2)or(usario == 3)or(usario == 0))):
        print("\n Ingrese un valor correcto por favor\n")
        #espera dos segundos
        sleeptime (2)
        
      else:control=1
      #si el usuario ingresa 1,2,3, empieza el juego
      if ((usario == 1)or(usario == 2)or(usario == 3)):
        print ( f"\n Ud eligio：{lista[usario]}" )
        pc = random.randint(1,3)  #La computadora genera un valor aleatorio entre 1 y 3
        print ( f" La computadora eligio ：{lista[pc]} ")
        if (usario == pc):
            contar_empate+=1
            contar_total+=1
            print("\n Empate\n" )
            print ( f"Total de Partidas: {contar_total} \n {contar_empate} Vezes Empate \n {contar_usario} Vezes Gana Usted \n {contar_pc} Vezes Gana La Computadora \n" )
            sleeptime (st)
        else:
            if ((usario == 1 and pc == 2) or(usario == 2 and pc == 3) or(usario == 3 and pc == 1)):
              contar_usario+=1
              contar_total+=1
              print ("\n Usted ha ganado \n")
              print ( f"Total de Partidas: {contar_total} \n {contar_empate} Vezes Empate \n {contar_usario} Vezes Gana Usted \n {contar_pc} Vezes Gana La Computadora \n" )
              sleeptime (st)
            else: 
              contar_pc+=1
              contar_total+=1
              print ("\n La computadora ha ganado \n")
              print ( f"Total de Partidas: {contar_total} \n {contar_empate} Vezes Empate \n {contar_usario} Vezes Gana Usted \n {contar_pc} Vezes Gana La Computadora \n" )
              sleeptime (st)

print ( f"\n Usted elig：{lista[usario]}\n" )
print ( f"Total de Partidas: {contar_total} \n {contar_empate} Vezes Empate \n {contar_usario} Vezes Gana Usted \n {contar_pc} Vezes Gana La Computadora \n" )
input ("\n Te Deseamos Tenga Un Buen Dia \n\n Apretar ENERT a Salir\n")
