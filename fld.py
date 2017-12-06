import pyautogui
import time
import keyboard
from pymsgbox import *
import sys

while True:
  t1 = prompt(text = 'Digite o numero de vezes que isso irá acontecer', title = '')#int(input(" >>> "))
  u = prompt(text = 'Digite o texto', title = '')#str(input("Digite o texto >>> "))
  h1 = prompt(text = "Digite o delay entre as letras (bom para marcar alguem no Whatsapp! valor > ou = à 0.5)\nou implesmente aperte ENTER para continuar e utilizar o padrão (0.02 secs)", title = '')#input("Digite o delay entre as letras (bom para marcar alguem no Whatsapp! valor > ou = à 0.5)\nou implesmente aperte ENTER para continuar e utilizar o padrão (0.02 secs) >>> ")

  t = int(t1)
  
  if h1 == "":
    h = 0.02
  else:
    h = h1

  #print ("Pressione S para iniciar")
  alert(text = "Após fechar esse tutorial pressione S para iniciar", title = "Passo: 1 - Iniciar", button = "Entendi")
  #print ("Pressione DELETE para parar")
  alert(text = "Caso queira parar no meio da execução\nPressione e segure DELETE", title = "Passo: 2 - Sair", button = "Prosseguir")
  while t > 0:
      if keyboard.is_pressed('s'):
        #print ("\n\nStarting in 5 secs!")
        alert(text = "Após pressionar OK o programa iniciará em 5 segundos!", title = "Iniciar!", button = "ok")
        time.sleep(5)
        for i in range(0, t):
          pyautogui.typewrite(u, h)
          pyautogui.press('enter')
          time.sleep(0.5)
          pyautogui.press('enter')
          if keyboard.is_pressed('delete'):
              alert(text = "Tecla DELETE pressionada! \nScript encerrado!", title = "Encerrado", button = "ok")
              t = 0              
              break              
          else:
              try:
                pass
              except Exception:
                pass
      else:
          try:
                pass
          except Exception:
                pass
  alert(text = "Processo finalizado!", title = "Fim", button = "FIM")

        
      
      

  
        
  
  

  
