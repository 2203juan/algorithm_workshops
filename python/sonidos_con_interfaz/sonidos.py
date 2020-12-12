from tkinter import *
from tkinter import messagebox
import pygame

def playsound(name):
  file = name
  pygame.init()
  pygame.mixer.init()
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()


#--------------------SONIDOS------------------------------------------
# CAMBIAR test.mp3 por el sonido que se quiere poner
# AQUI VAN LOS SONIDOS DEL NIVEL 1
def sonido1():
  playsound("test.mp3")


def sonido2():
  playsound("test.mp3")

def sonido3():
  playsound("test.mp3")

# AQUI VAN LOS SONIDOS DEL NIVEL 2
def sonido4():
  playsound("test.mp3")


def sonido5():
  playsound("test.mp3")

def sonido6():
  playsound("test.mp3")

# AQUI VAN LOS SONIDOS DEL NIVEL 3
def sonido7():
  playsound("test.mp3")


def sonido8():
  playsound("test.mp3")

def sonido9():
  playsound("test.mp3")

def original_1():
  # cargar el sonido original del nivel 1
  playsound("test.mp3")

def original_2():
  # cargar el sonido original del nivel 2
  playsound("test.mp3")

def original_3():
  # cargar el sonido original del nivel 3
  playsound("test.mp3")

#-------------------------------------------------------------------------------


#---------------------------------------------------------
# FUNCIONES DE VERIFICACION DE RESPUESTA

#NIVEL 1
def verificar1(ans):
  ans = ans.get()
  if ans == 1:
    messagebox.showinfo(message="Correcto!", title="Bien hecho")
  else:
    messagebox.showinfo(message="Respuesta incorrecta", title="Ups!")

  root3.destroy()
  root2.destroy()

#NIVEL 2
def verificar2(ans):
  ans = ans.get()
  if ans == 3:
    messagebox.showinfo(message="Correcto!", title="Bien hecho")
  else:
    messagebox.showinfo(message="Respuesta incorrecta", title="Ups!")
  root4.destroy()
  root5.destroy()

#NIVEL 3
def verificar3(ans):
  ans = ans.get()
  if ans == 2:
    messagebox.showinfo(message="Correcto!", title="Bien hecho")
  else:
    messagebox.showinfo(message="Respuesta incorrecta", title="Ups!")
  root6.destroy()
  root7.destroy()

  #-------------------------------------------------------------------------------


#---------------------------------------------
# FUNCIONES PARA MOSTRAR PREGUNTAS

def ans1():
  global root3
  """
  Aqui debes poner las opciones de respuesta del nivel 1

  Ponga la opcion correcta en la opcion_a
  """

  opcion_a = "Opcion a"
  opcion_b = "Opcion b"
  opcion_c = "Opcion c"



  color = "#fff636"
  root3 = Toplevel()
  root3.geometry("400x250")
  var = IntVar()

  R1 = Radiobutton(root3, text = opcion_a, variable = var, value = 1,command = lambda: verificar1(var),padx = 200)
  R1.configure(background =color)
  R1.configure(font = ("Courier", 16, "italic"))
  R1.pack( anchor = W )

  R2 = Radiobutton(root3, text = opcion_b, variable = var, value = 2,command = lambda: verificar1(var),padx = 200,pady = 50)
  R2.configure(background = color)
  R2.configure(font = ("Courier", 16, "italic"))
  R2.pack( anchor = W )

  R3 = Radiobutton(root3, text = opcion_c, variable = var, value = 3,command = lambda: verificar1(var),padx = 200,pady = 100)
  R3.configure(background = color)
  R3.configure(font = ("Courier", 16, "italic"))
  R3.pack( anchor = W)


def ans2():
  global root5
  """
  Aqui debes poner las opciones de respuesta del nivel 1

  Ponga la opcion correcta en la opcion_c
  """
  opcion_a = "Opcion a"
  opcion_b = "Opcion b"
  opcion_c = "Opcion c"



  color = "#fff636"
  root5 = Toplevel()
  root5.geometry("400x250")
  var = IntVar()

  R1 = Radiobutton(root5, text = opcion_a, variable = var, value = 1,command = lambda: verificar2(var),padx = 200)
  R1.configure(background =color)
  R1.configure(font = ("Courier", 16, "italic"))
  R1.pack( anchor = W )

  R2 = Radiobutton(root5, text = opcion_b, variable = var, value = 2,command = lambda: verificar2(var),padx = 200,pady = 50)
  R2.configure(background = color)
  R2.configure(font = ("Courier", 16, "italic"))
  R2.pack( anchor = W )

  R3 = Radiobutton(root5, text = opcion_c, variable = var, value = 3,command = lambda: verificar2(var),padx = 200,pady = 100)
  R3.configure(background = color)
  R3.configure(font = ("Courier", 16, "italic"))
  R3.pack( anchor = W)



def ans3():
  global root7
  """
  Aqui debes poner las opciones de respuesta del nivel 1

  Ponga la opcion correcta en la opcion_b
  """
  opcion_a = "Opcion a"
  opcion_b = "Opcion b"
  opcion_c = "Opcion c"




  color = "#fff636"
  root7 = Toplevel()
  root7.geometry("400x250")
  var = IntVar()

  R1 = Radiobutton(root7, text = opcion_a, variable = var, value = 1,command = lambda: verificar3(var),padx = 200)
  R1.configure(background =color)
  R1.configure(font = ("Courier", 16, "italic"))
  R1.pack( anchor = W )

  R2 = Radiobutton(root7, text = opcion_b, variable = var, value = 2,command = lambda: verificar3(var),padx = 200,pady = 50)
  R2.configure(background = color)
  R2.configure(font = ("Courier", 16, "italic"))
  R2.pack( anchor = W )

  R3 = Radiobutton(root7, text = opcion_c, variable = var, value = 3,command = lambda: verificar3(var),padx = 200,pady = 100)
  R3.configure(background = color)
  R3.configure(font = ("Courier", 16, "italic"))
  R3.pack( anchor = W)

 #------------------------------------------------------------


 #-------------------------------------------------------

 # FUNCIONES PARA PONER SONIDOS


def nivel1():
  global root2
  color = "#33ffa8"
  root2 = Tk()
  root2.geometry("400x250")

  pregunta = "\nAQUI SE ESCRIBE LA PREGUNTA 1?\n"
  label = Label(root2,text = pregunta)
  label.pack()
  

  R1 = Radiobutton(root2, text="Sonido 1", variable=var, value = 1,command = sonido1,padx = 200)
  R1.configure(background =color)
  R1.configure(font = ("Courier", 16, "italic"))
  R1.pack( anchor = W )

  R2 = Radiobutton(root2, text="Sonido 2", variable=var, value = 2,command = sonido2,padx = 200,pady = 50)
  R2.configure(background =color)
  R2.configure(font = ("Courier", 16, "italic"))
  R2.pack( anchor = W )

  R3 = Radiobutton(root2, text="Sonido 3", variable=var, value = 3,command = sonido3,padx = 200,pady = 100)
  R3.configure(background = color)
  R3.configure(font = ("Courier", 16, "italic"))
  R3.pack( anchor = W)

  Bplay = Button(root2, text ="Play", command = original_1).place(x = 320,y = 5)
  B1 = Button(root2, text ="Responder", command = ans1).place(x = 270,y = 220)

def nivel2():
  global root4
  color = "#33ffa8"
  root4 = Tk()
  root4.geometry("400x250")

  pregunta = "\nAQUI SE ESCRIBE LA PREGUNTA 2?\n"
  label = Label(root4,text = pregunta)
  label.pack()
  
  R1 = Radiobutton(root4, text="Sonido 1", variable=var, value = 1,command = sonido4,padx = 200)
  R1.configure(background =color)
  R1.configure(font = ("Courier", 16, "italic"))
  R1.pack( anchor = W )

  R2 = Radiobutton(root4, text="Sonido 2", variable=var, value = 2,command = sonido5,padx = 200,pady = 50)
  R2.configure(background =color)
  R2.configure(font = ("Courier", 16, "italic"))
  R2.pack( anchor = W )

  R3 = Radiobutton(root4, text="Sonido 3", variable=var, value = 3,command = sonido6,padx = 200,pady = 100)
  R3.configure(background = color)
  R3.configure(font = ("Courier", 16, "italic"))
  R3.pack( anchor = W)

  Bplay = Button(root4, text ="Play", command = original_2).place(x = 320,y = 5)
  B2= Button(root4, text ="Responder", command = ans2).place(x = 270,y = 220)
  

def nivel3():
  global root6
  color = "#33ffa8"
  root6 = Tk()
  root6.geometry("400x250")

  pregunta = "\nAQUI SE ESCRIBE LA PREGUNTA 3?\n"
  label = Label(root6,text = pregunta)
  label.pack()

  R1 = Radiobutton(root6, text="Sonido 1", variable=var, value = 1,command = sonido7,padx = 200)
  R1.configure(background =color)
  R1.configure(font = ("Courier", 16, "italic"))
  R1.pack( anchor = W )

  R2 = Radiobutton(root6, text="Sonido 2", variable=var, value = 2,command = sonido8,padx = 200,pady = 50)
  R2.configure(background =color)
  R2.configure(font = ("Courier", 16, "italic"))
  R2.pack( anchor = W )

  R3 = Radiobutton(root6, text="Sonido 3", variable=var, value = 3,command = sonido9,padx = 200,pady = 100)
  R3.configure(background = color)
  R3.configure(font = ("Courier", 16, "italic"))
  R3.pack( anchor = W)

  Bplay = Button(root6, text ="Play", command = original_2).place(x = 320,y = 5)
  B3 = Button(root6, text ="Responder", command = ans3).place(x = 270,y = 220)




def menu():
  # menu principal
  global var
  root = Tk()
  color = "#33ff52"
  root.geometry("400x250")
  var = IntVar()
  R1 = Radiobutton(root, text="NIVEL 1", variable = var, value = 1,command = nivel1,padx = 200)
  R1.configure(background =color)
  R1.configure(font = ("Courier", 16, "italic"))
  R1.pack( anchor = W )

  R2 = Radiobutton(root, text="NIVEL 2", variable = var, value = 2,command = nivel2,padx = 200,pady = 50)
  R2.configure(background =color)
  R2.configure(font = ("Courier", 16, "italic"))
  R2.pack( anchor = W )

  R3 = Radiobutton(root, text="NIVEL 3", variable = var, value = 3,command = nivel3,padx = 200,pady = 100)
  R3.configure(background = color)
  R3.configure(font = ("Courier", 16, "italic"))
  R3.pack( anchor = W)

  label = Label(root)
  label.pack()
  root.mainloop()

root_main = Tk()
color = "#0099fc"
root_main.geometry("400x250")
root_main.configure(bg=color)
pregunta = "\n\n\nBIENVENIDO AL SISTEMA\n"
label = Label(root_main,text = pregunta)
label.pack()
label.configure(background =color)
label.configure(font = ("Courier", 20, "italic"))
label.pack( anchor = N )

B_main = Button(root_main, text ="Start", command = menu).place(x = 170,y = 220)
B2main = Button(root_main, text ="Salir", command = quit).place(x = 270,y = 220)

root_main.mainloop()