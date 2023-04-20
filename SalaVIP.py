from os import system
system ("cls")

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'


tarjeta = 0

usuarios = []


print(MAGENTA+"=============",WHITE+"    Bienvenido!   ",MAGENTA+" ===============")
print(MAGENTA+"=============",WHITE+" Registre sus datos",MAGENTA+" ===============")


print("")

user = input(WHITE+"Ingrese su nombre: ")

user = str(user)

usuarios.append(user)

while True:
    
    try:
        cc = int(input("Ingrese su numero de cedula: "))
        system('cls')

        break

    except:

        system('cls')
        print("Lo siento, debes ingresar numeros enteros..")
        print("")

        continue

def juego1():

    import random

    options = ('piedra', 'papel', 'tijera')

    computer_wins = 0
    user_wins = 0

    rondas = 1

    while  True:

        global tarjeta

        print('=' * 13)
        print("  RONDA #", rondas)
        print('=' * 13)

        print("Rondas ganadas por ",user,"       ---->",user_wins)
        print("Rondas ganadas por la computadora ---->",computer_wins)

        print("")

        print("Elige!!")

        print("")

        opcion = input("Piedra, Papel o Tijera: ")

        opcion = opcion.lower()

        if not opcion in options:

            print("")
            system ('cls')
            print("La opcion que ingreso no es valida!, Ingrese nuevamente su opcion...")
            print("")

            continue

        else:
        
            print("")

            computer_opcion = random.choice(options)

            system ("cls")

            print(user,"eligio -->", opcion)

            print("")

            print("Computadora eligio -->", computer_opcion)

            print("")

            if opcion == computer_opcion:

                print("Empate!!")
                
            elif opcion == 'piedra':

                if computer_opcion == 'tijera':

                    print("Piedra gana a tijera")
                    print("")
                    print(user,"Gana la ronda #", rondas)
                    user_wins += 1
                    
                else:

                    print("Papel gana a piedra")
                    print("")
                    print("Computadora Gana la ronda #", rondas)
                    computer_wins += 1
                    
            elif opcion == 'papel':

                if computer_opcion == 'piedra':

                    print("Papel gana a piedra")
                    print("")
                    print(user,"Gana la ronda #", rondas)
                    user_wins += 1
                    
                else:

                    print("Tijera gana a papel")
                    print("")
                    print("Computadora Gana la ronda #", rondas)
                    computer_wins += 1
                    
            elif opcion == 'tijera':

                if computer_opcion == 'papel':

                    print("Tijera gana a papel")
                    print("")
                    print(user,"Gana la ronda #", rondas)
                    user_wins += 1
                    
                else:

                    print("Piedra gana a tijera")
                    print("")
                    print("Computadora Gana la ronda #", rondas)
                    computer_wins += 1
                    

            if computer_wins == 3:

                system ('cls')

                print("Rondas ganadas por el Usuario     ---->",user_wins)
                print("Rondas ganadas por la computadora ---->",computer_wins)

                print("")

                print("Rayos!!")

                print("")

                print("El ganador es la computadora!")

                print("")

                break

            elif user_wins == 3:
                system ('cls')

                print("Rondas ganadas por el Usuario     ---->",user_wins)
                print("Rondas ganadas por la computadora ---->",computer_wins)
                
                print("")

                print("El ganador es el Usuario! -->",user)

                tarjeta = tarjeta + 124

                break

            rondas += 1
            
            print("")

def juego2():

    import random

    tex1 = ("Emil necesita las compras para el cumpleaños de su hermana menor!")
    tex2 = ("Emil necesita algunas motos para vender en su negocio!")
    tex3 = ("Emil necesita los utiles para su comienzo a clases!")
    tex4 = ("Emil necesita comprar lo componentes para su nueva computadora!")
    tex5 = ("Emil necesita comprar lo del almuerzo!")
    tex6 = ("Emil necesita comprar lo del desayuno de su papa!")
    tex7 = ("Emil necesita comprar lo de la comida!")
    tex8 = ("Emil necesita comprar frutas!")

    textos = (tex1,tex2,tex3,tex4,tex5,tex6,tex7,tex8)
 
    situacion = random.choice(textos)

    print("=" * 67)

    print(situacion)

    print("=" * 67)

    carrito = []
    
    print("")

    print("Ayuda a Emil con las compras")

    print("")

    while True:
        
        global tarjeta  

        compras = (input("Agrega productos al carrito: "))

        compras = str(compras)

        carrito.append(compras)

        system ('cls')
        print("Por el momento llevas en el carrito:")
        print("")
        print(carrito)
        print("")

        opciones = ('s','n')

        while True:

            otro = input("Desea Agregar otro? (s)/(n): ")

            if otro not in opciones:

                system('cls')
                print("Lo siento, opcion invalaida...")
                print("")

                continue

            else:

                system ('cls')

                break

        if otro == 's':

            system ('cls')

            continue

        else:

            system ('cls')
            print("Excelente llevaremos lo siguiente!")
            print("")
            tarjeta += 74                    
            print(carrito)
            print("")
            print("Ganaste $52 por ayudar a Emil!")
            print("")

        break

def juego3():

    import random
    import math

    global tarjeta

    op = ('s')

    while True:

        n = input("Presione (s) para lanzar el dardo: ")

        n = str(n)

        if n not in op:

            system ('cls')
            print("Opcion invalida....")
            print("")

            continue

        else:    

            system ('cls')

            x = random.randint(0,80)
            y = random.randint(0,80)

            print("el punto al azar es x="+ str(x) + " y=" + str(y))

            result= math.sqrt((x-80)**2+(y-80)**2)

            print("")

            print("el resulta es:"+str(result))

            print("")

        if result<=10:

            print("Felicitaciones! gano $162") 
            print("")     
            print("Tenias",tarjeta)

            tarjeta = tarjeta + 162

            print("")
            print("Ahora tienes",tarjeta)

            break

        elif result >10 and result <=40:

            print("Felicitaciones! gano $100")
            print("")
            print("Tenias",tarjeta)

            tarjeta = tarjeta + 100

            print("")
            print("Ahora tienes",tarjeta)

            break

        elif result > 40 and result <=80:

            print ("Felicitaciones! gano $68")
            print("")
            print("Tenias",tarjeta)

            tarjeta = tarjeta + 68

            print("")
            print("Ahora tienes",tarjeta)

            break

        else:
            print("el dardo callo fuera gano $36")
            print("")
            print("Tenias",tarjeta)
            tarjeta = tarjeta + 36
            print("")
            print("Ahora tienes",tarjeta)

            break
        
while True:

    print("La tarjeta es tototalmente gratis!")

    print("")

    vtarjeta = input("Enter para adquirir la tarjeta: ")

    system ('cls')

    print(RED+"¡Debes agregarle saldo!")
    print("")
    print(WHITE+"El juego mas enconomico es de 48, puedes agregar eso o mas!")
    print("")

    break 

while True: 

    try :

        tarjeta = int(input("Cuanto deseas recargarle a la tarjeta?: "))   
        system('cls')
        print(MAGENTA+"BIENVENID@ A LA SALA DE VIDEOJUEGOS VIP DE ---> (Emil Sanchez)"+WHITE)
        print("")  
         
        break 

    except:

        system ('cls')
        print("Lo siento, ingrese numeros enteros....")
        print("")

        continue

                
while True:
    
    if tarjeta > 0:
        
        print("Hola",user)
        print("")
        print("Saldo de su tarjeta -->",tarjeta,GREEN+"$")
        WHITE
        print("")
        print(BLUE+"------------",WHITE+"Juegos",BLUE+"--------------")
        print("")
        print(WHITE+"1. Piedra, Papel o Tijera         ----> $82")
        print("2. De compras con Emil            ----> $48")
        print("3. Gana Dinero Lanzando el Dardo  ----> $94")
        print("")
        print("4. Salir")
        print("")

        opcion = int(input("Ingrese el numero del juego que desea ejecutar --> "))

        opcion = str(opcion)

        if opcion == '1':

            if tarjeta < 82:

                system ('cls')
                print("Dinero insuficiente...")
                print("")
                while True:     
                    try :
                        tarjeta = int(input("Cuanto deseas recargarle a la tarjeta?: "))   
                        tarjeta += tarjetamas
                        system ('cls')
                            
                    except:
                        system ('cls')
                        print("Ingrese un numero entero")
                        print("")
                        continue
                

            else:

                tarjeta = tarjeta - 82
                system ("cls")
                print("Buena eleccion! Jugaras ( Piedra, papel o Tijeras :)! )")
                print("")
                juego1()
                print("")
                print("Saldo de su tarjeta -->", tarjeta)
                print("")
                continuar = input("Enter para regresar al menu: ")
                system ("cls")

                continue
                
        elif opcion == '2': 
                        
                    if tarjeta < 48:

                        system ('cls')
                        print("Dinero insuficiente...")
                        print("")
                        tarjetamas = int(input("Cuanto deseas recargarle a la tarjeta?: "))
                        tarjeta += tarjetamas
                        system ('cls')

                        continue

                    else:

                        tarjeta = tarjeta - 48
                        system ("cls")                 
                        print("Buena eleccion! Jugaras ( De compras con Emil :)! )")
                        print("")
                        juego2()
                        print("")
                        continuar = input("Enter para regresar al menu: ")
                        system ("cls")

                        continue

                        
                    
        elif opcion == '3':

            if tarjeta < 94:

                system ('cls')
                print("Dinero Insuficiente...")
                print("")
                tarjetamas = int(input("Cuanto deseas recargarle a la tarjeta?: "))
                tarjeta += tarjetamas
                system ('cls')

                continue

            else:

                tarjeta = tarjeta - 94
                system ("cls")  
                print("Buena eleccion! Jugaras (A lanzar el dardo!)")
                print("")
                juego3()
                print("")
                continuar = input("Enter para regresar al menu:")
                system ("cls") 

                continue


        elif opcion == '4':
                    
                    system ('cls')
                    op = ('s','n')

                    while True:    

                        usernew = input("Desea entrar otro usuario? (S)/(n): ")
                        usernew = str(usernew)

                        if usernew not in op:

                            system ('cls')
                            print("Opcion invalida") 
                            print("")
                            continue

                        else:
                            system('cls')
                            break                 


                    if usernew == 's':

                        system ('cls')
                        print(MAGENTA+"=============",WHITE+"    Bienvenido!   ",MAGENTA+" ===============")
                        print(MAGENTA+"=============",WHITE+" Registre sus datos",MAGENTA+" ===============")

                        print("")

                        user = input("Ingrese su nombre: ")
                        user = str(user)                                                    
                            
                        if user in usuarios:

                            system ('cls')

                            print(WHITE+"Hola de nuevo!",user)

                            print("")

                            print("Tienes en tu tarjeta el siguiente saldo -->",tarjeta)
                            
                            print("")
                        

                            while True:
                                    mas = input("Deseas Agregar mas dinero? (S)/(n): ")

                                    mas = mas.lower()

                                    system ('cls')

                                    if mas not in op:

                                        system('cls')
                                        print("Lo siento, esa opcion no existe...")
                                        print("")
                                        continue

                                    else:

                                        if mas == 's':      

                                            tarjetamas1 = int(input("Cuanto dinero deseas agregarle a la tarjeta?: "))

                                            tarjeta+=tarjetamas1

                                            system ('cls')

                                            break
                                        else:

                                            system('cls')
                                            break

                        else:
                            while True:
                                try:
                                    cc = int(input("Ingrese su numero de cedula: "))
                                    system('cls')
                                    break                              
                                except:
                                    system('cls')
                                    print("Lo siento, debes escribir numeros enteros")
                                    print("")
                                    continue                               
                                    
                            print("El anterior Usuario te dejo su tarjeta con un saldo de",tarjeta)

                            op = ('s','n')

                            print("")

                            while True:

                                    mas = input("Deseas Agregar mas dinero? (S)/(n): ")

                                    mas = mas.lower()

                                    system ('cls')

                                    if mas not in op:

                                        system ('cls')
                                        print("Lo siento, esa opcion no existe...")
                                        print("")

                                        continue
                                    else:

                                        system ('cls')
                                    
                                    if mas == 's':  

                                        while True:

                                            try: 

                                                tarjetamas1 = int(input("Cuanto dinero deseas agregarle a la tarjeta?: "))  
                                                system('cls')                                                                                                                     
                                                break

                                            except:

                                                system ('cls')
                                                print("Lo siento, debes escribir numeros enteros")
                                                print("")
                                        
                                    elif mas == 'n':
                                        system ('cls')

                                        break


                                    tarjeta+=tarjetamas1

                                    continue
        
                    elif usernew == 'n':

                        system ('cls')

                        print("Para el jugador(a)",user,"identificado con cc",cc,"el juego a Finalizado")

                        print("")

                        print("El saldo de su tarjeta fue", tarjeta)

                        print("")

                        print("Adios!")

                        print("")

                        print("")
                        print("")

                        print("Creador --> Emil Sanchez R.")

                        print("")
                        print("")
                        print("")

                        break
                                            

        else:
            system('cls')

            print("")

            print("Este juego no existe o aun no se a elaborado..")

            print("")
            
            continue
    else:

        system ('cls')
        print("Dinero insuficiente....")

        print("")

        while True:
            try: 
                tarjetamas1 = int(input("Cuanto dinero deseas agregarle a la tarjeta?: "))                                                                                                                       
                break
            except:
                system ('cls')
                print("Lo siento, debes escribir numeros enteros")
                print("")
                continue
        tarjeta += tarjetamas

        system ('cls')

        continue
        

