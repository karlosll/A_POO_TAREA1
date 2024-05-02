from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient, VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
#----------------------------------------MENU-CLIENTES----------------------------------
class CrudClients(ICrud):
    #--------------------------------1.-INGRESAR-------------------------------------
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(green_color + "█" * 90 + reset_color)
        gotoxy(2, 2); print("██" + " " * 34 + "Registro de Cliente" + " " * 34 + "██")
        
        #print("Ingrese DNI del cliente: ")
        dni=validar.cedula("Error: 10 digitos",23,4)   
        
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        valor = float(input("Ingrese el valor del cliente: "))
        
        #---------------------------------sss
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni", dni)
        if client:
            print("El cliente ya existe en la base de datos.")
            input("Presione Enter para volver al menú principal...")
            return
        
        new_client = {
            "dni": dni,
            "nombre": nombre,
            "apellido": apellido,
            "valor": valor
        }
        
        client = json_file.read()
        client.append(new_client)
        json_file = JsonFile(path+'/archivos/clients.json')
        json_file.save(client)
        
        
       
        print("Cliente registrado exitosamente.")
        input("Presione Enter para volver al menú principal...")
        
#--------------------------------------------------------------------------------

        
#------------------ACTUALIZAR---CLIENTES----------------------------------        
        
    def update(self):
    
         # Mostrar los clientes existentes para que el usuario pueda elegir
        print("Clientes registrados:")
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        for i, client in enumerate(clients, start=1):
            print(f"{i}. {client['nombre']} {client['apellido']} - DNI: {client['dni']}")

        try:
            # Solicitar al usuario que elija el cliente a actualizar
            indice = int(input("Ingrese el número del cliente que desea actualizar: "))
            if 1 <= indice <= len(clients):
                # Obtener el cliente seleccionado
                cliente_actualizar = clients[indice - 1]
                
                # Solicitar los nuevos datos del cliente
                print("Ingrese los nuevos datos del cliente (deje vacío para mantener los datos existentes):")
                nuevo_dni = input(f"DNI ({cliente_actualizar['dni']}): ") or cliente_actualizar['dni']
                nuevo_nombre = input(f"Nombre ({cliente_actualizar['nombre']}): ") or cliente_actualizar['nombre']
                nuevo_apellido = input(f"Apellido ({cliente_actualizar['apellido']}): ") or cliente_actualizar['apellido']
                nuevo_valor = (input(f"Valor ({cliente_actualizar['valor']}): ")) or cliente_actualizar['valor']
                
                # Actualizar los datos del cliente
                cliente_actualizar['dni'] = nuevo_dni
                cliente_actualizar['nombre'] = nuevo_nombre
                cliente_actualizar['apellido'] = nuevo_apellido
                
                cliente_actualizar['valor'] = float(nuevo_valor)
                
                # Guardar los cambios en el archivo JSON
                json_file.save(clients)
                
                print("Cliente actualizado exitosamente.")
            else:
                print("Número de cliente fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

        input("Presione Enter para volver al menú principal...")
            
        
    
    
    
    
    def delete(self):
        #------------------------------------ELIMINAR--CLIENTES--------------------------------
            # Mostrar los clientes existentes
        print("Clientes registrados:")
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        for i, client in enumerate(clients, start=1):
            print(f"{i}. {client['nombre']} {client['apellido']} - DNI: {client['dni']}")

        # Solicitar al usuario que elija el cliente a eliminar
        try:
            indice = int(input("Ingrese el número del cliente que desea eliminar: "))
            if 1 <= indice <= len(clients):
                cliente_eliminado = clients.pop(indice - 1)
                print(f"Se ha eliminado al cliente: {cliente_eliminado['nombre']} {cliente_eliminado['apellido']}")
                json_file.save(clients)  # Guardar los cambios en el archivo JSON
            else:
                print("Número de cliente fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

        input("Presione Enter para volver al menú principal...")


 #--------------------------CONSULTAR --CLIENTES-----------------------   
    def consult(self):
        print('\033c', end='')  
        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read()
        total_clients = len(clients)

        print(green_color + "Consulta de Clientes" + reset_color)
        print(f"El total de clientes es: {total_clients}\n")

        if total_clients > 0:
            print("Listado de clientes:")
            for i, client in enumerate(clients, start=1):
                print(f"{i}. {client['nombre']} {client['apellido']} - DNI: {client['dni']}")
        else:
            print("Aun no a registrado clientes.")

        input("Presione ENTER para volver al menú principal...")
            
    

class CrudProducts(ICrud):
 #--------------------------------------Craer--new--products------------- 
    def create(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█" * 90 + reset_color)
        gotoxy(2, 2)
        print("██" + " " * 34 + "Registro de Producto" + " " * 34 + "██")

        # Solicitar los datos del nuevo producto
        id_producto = int(input("Ingrese el ID del producto: "))
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))

        # Verificar si el producto ya ex(iste en el archivo JSON
        json_file = JsonFile(path + '/archivos/products.json')
        existing_products = json_file.read()
        for product in existing_products:
            if product["id"] == id_producto:
                print("ESE PRODUCTO YA EXISTE.")
                input("Presione Enter para volver al menú principal...")
                return
        
        new_product = {
            "id": id_producto,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        }
        existing_products.append(new_product)
        json_file.save(existing_products)

        print("Producto Se GUARDO exitosamente.")
        input("Presione ENTER para volver al menú principal......")
    
###########----------ACTUALIZAR---PRODUCTOS----------------------    
    def update(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█" * 90 + reset_color)
        gotoxy(2, 2)
        print("██" + " " * 34 + "Modificación de Producto" + " " * 34 + "██")

        # Mostrar los productos existentes para que el usuario pueda elegir
        print("Productos registrados:")
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product['descripcion']} / Presio: {product['precio']} / Cantidad: {product['stock']}")

        try:
            # Solicitar al usuario que elija el producto a actualizar
            indice = int(input("Ingrese el número del producto que desea actualizar: "))
            if 1 <= indice <= len(products):
                # Obtener el producto seleccionado
                producto_actualizar = products[indice - 1]
                
                # Solicitar los nuevos datos del producto
                print("Ingrese los nuevos datos del producto (deje vacío para mantener los datos existentes):")
                nueva_descripcion = input(f"Descripción ({producto_actualizar['descripcion']}): ") or producto_actualizar['descripcion']
                nuevo_precio = float(input(f"Precio ({producto_actualizar['precio']}): ")) or producto_actualizar['precio']
                nuevo_stock = int(input(f"Stock ({producto_actualizar['stock']}): ")) or producto_actualizar['stock']
                
                # Actualizar los datos del producto
                producto_actualizar['descripcion'] = nueva_descripcion
                producto_actualizar['precio'] = nuevo_precio
                producto_actualizar['stock'] = nuevo_stock
                
                # Guardar los cambios en el archivo JSON
                json_file.save(products)
                
                print("Producto actualizado exitosamente.")
            else:
                print("Número de producto fuera de rango.")
        except ValueError:
            print("Ingrese un número por favor.")

        input("Presione Enter para volver al menú principal......")
    
        
    def delete(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█" * 90 + reset_color)
        gotoxy(2, 2)
        print("██" + " " * 34 + "Eliminación de Producto" + " " * 34 + "██")

        # Mostrar los productos existentes para que el usuario pueda elegir
        print("Productos registrados:")
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product['descripcion']} / stock: {product['stock']}")

        try:
            # Solicitar al usuario que elija el producto a eliminar
            indice = int(input("Ingrese el número del producto que desea eliminar: "))
            if 1 <= indice <= len(products):
                producto_eliminado = products.pop(indice - 1)
                print(f"Se ha eliminado el producto: {producto_eliminado['descripcion']} / ID: {producto_eliminado['id']}")
                json_file.save(products)  # Guardar los cambios en el archivo JSON
            else:
                print("Número de producto fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

        input("Presione Enter para volver al menú principal...")
            
        
    def consult(self):
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█" * 90 + reset_color)
        gotoxy(2, 2)
        print("██" + " " * 34 + "Consulta de Productos" + " " * 35 + "██")

        # Leer los productos desde el archivo JSON
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()

        total_productos = len(products)

        print(f"Total de productos registrados: {total_productos}\n")

        if total_productos > 0:
            # Mostrar todos los productos y sus precios
            print("Listado de productos:")
            for product in products:
                print(f"ID: {product['id']} -> Descripción: {product['descripcion']} / Precio: {product['precio']} / Stock: {product['stock']}")

            # Calcular el producto más caro y el más barato
            precios = [product['precio'] for product in products]
            producto_mas_caro = max(products, key=lambda x: x['precio'])
            producto_mas_barato = min(products, key=lambda x: x['precio'])

            print(f"\nProducto más caro: {producto_mas_caro['descripcion']} -> Precio: {producto_mas_caro['precio']}")
            print(f"Producto más barato: {producto_mas_barato['descripcion']} -> Precio: {producto_mas_barato['precio']}")

            # Calcular la cantidad total de productos
            total_stock = sum(product['stock'] for product in products)
            print(f"\nTotal de productos en stock: {total_stock}")
        else:
            print("Aún no hay productos registrados.")

        input("\nPresione ENTER para volver al menú principal...")

class CrudSales(ICrud):
    def create(self):
        #-------------------------------------------1.-REGISTRAR--VENTAS----------------------9
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni=validar.solo_numeros("Error: Solo numeros",23,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line);
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)    
#--------------------MODIFICAR---------------------------------------------
    def update(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Modificación de Venta"+" "*34+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura a modificar: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            if invoices:
                invoice_data = invoices[0]
                print(f"Factura encontrada: {invoice_data}")
                
            else:
                print(f"No se encontró la factura {invoice}.")
        else:
            print("La factura ingresada no es válida.")
        x=input("Presione una tecla para continuar...")
            
#---------------------------ELIMINAR------------------------------------
    def delete(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Eliminación de Venta"+" "*34+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura a eliminar: ")
        
        print("Función para eliminar una venta")
        factura = input("Ingrese el número de factura de la venta que desea eliminar: ")
        json_file = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file.read()  # Leer todas las facturas

        # Crear una lista nueva sin la factura que se desea eliminar
        updated_invoices = [invoice for invoice in invoices if invoice["factura"] != int(factura)]

        # Verificar si se eliminó alguna factura
        if len(invoices) != len(updated_invoices):
            json_file.save(updated_invoices)  # Guardar los cambios en el archivo
            print("Venta eliminada exitosamente.")
        else:
            # Si no se encontró la factura
            print("Venta no encontrada.")

        input("Presione Enter para volver al menú principal...")
        
#-------------------------------CONSULTAR-----------------------------------        
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Venta"+" "*35+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            print(f"Impresion de la Factura#{invoice}")
            print(invoices)
        else:    
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            print("Consulta de Facturas")
            for fac in invoices:
                print(f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}")
            
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), 
            invoices,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices))
            total_client = list(filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices))

            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            print("filter cliente: ",total_client)
            print(f"map Facturas:{totales_map}")
            print(f"              max Factura:{max_invoice}")
            print(f"              min Factura:{min_invoice}")
            print(f"              sum Factura:{tot_invoices}")
            print(f"              reduce Facturas:{suma}")
        x=input("presione una tecla para continuar...")    

        #---------------------------------
        
#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        #---------------------------------1----CLIENTES--------------------------------------------------------------------
        while opc1 !='5':
            borrarPantalla() 
            clients = CrudClients()
            menu_clients = Menu("Menu Cientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                clients.create()
            elif opc1 == "2":
                clients.update()
                
            elif opc1 == "3":
                clients.delete()
                time.sleep(2)
                
            elif opc1 == "4":
                clients.consult()
                
            print("Regresando al menu Clientes...")
            # time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        #2---------------------------------------------2.-MENU---PRODUCTOS---------------------------------
        while opc2 !='5':
            borrarPantalla()
            products =CrudProducts()    
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                products.create()
            elif opc2 == "2":
                products.update()
            elif opc2 == "3":
                products.delete()
            elif opc2 == "4":
                products.consult()
            #--------------------------------------3.-----MENU--VENTA---------------------------------------------------
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
            elif opc3 == "3":
                sales.update()
                time.sleep(2)    
            elif opc3 == "4":
                sales.delete()
                time.sleep(2)    
     
    print("Regresando al menu Principal...")
    # time.sleep(2)            

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()








