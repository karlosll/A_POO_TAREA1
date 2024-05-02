#-----------------------------------------------------
from utilities import borrarPantalla, gotoxy
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input(f"Elija opcion[1...{len(self.opciones)}]: ") 
        return opc   
    

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

#-----------------

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor



    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    
#crear decorador para digitos de cedula-------------------



    def ecuadorian_id_base_10(func):
        def wrapper(*args, **kwargs):
            mensajeError = "ERROR:Cédula no válida."
            while True:
                valor = func(*args, **kwargs)
                if valor.isdigit() and len(valor) == 10:
                    # Verificar si es cédula ecuatoriana
                    primer_digito = int(valor[0])
                    if primer_digito >= 0 and primer_digito <= 5:
                        return valor
                gotoxy(args[2], args[3])
                print(mensajeError)
                time.sleep(1)
                gotoxy(args[2], args[3])
                print(" " * 50)
        return wrapper
    
    @ecuadorian_id_base_10
    def cedula(self,mensajeError,col,fil):
        while True:
            #gotoxy(col, fil)
            valor = input("Ingrese el DNI del Cliente: ")
            if valor.isdigit() and len(valor) == 10:
                break
            else:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*50)
        return valor

#@agregar decorador---------------    
  #  def cedula():
   #     pass
    
 

if __name__ == '__main__':
    # instanciar el menu
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida = Valida()
    if(opciones_menu==1):
      numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
      print("Número validado:", numero_validado)
    
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
    
    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)
