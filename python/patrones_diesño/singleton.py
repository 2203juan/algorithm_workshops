class Singleton(object):
   
   __instance = None

   def __init__(self):
      """ Constructor. """
      if Singleton.__instance != None:
         raise Exception("No pude haber más de una instancia, patrón Singleton!")
      
      else:
         Singleton.__instance = self

   @staticmethod 
   def getInstance():
      """ Método estático de acceso. """
      if Singleton.__instance == None:
         Singleton()

      return Singleton.__instance

   def showMessage(self):
      print("Hello World")



def main():
   s = Singleton()
   s = Singleton.getInstance()
   s.showMessage()
   #Singleton() #raise Exception
main()