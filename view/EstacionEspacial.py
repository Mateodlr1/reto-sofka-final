from Model.Naves import  Naves
from Controller.NavesEspaciales import NavesEspaciales as ne

opcion = None
while opcion != 4:   #mientras sea diferente se muestra este bloque de codigo
    try: #valido las entradas por si  el usuario no digita un numero valido
         print('Opciones: ')  #imprimo las opciones
         print('1. Agregar Nave')
         print('2. Listar naves')
         print('3. Eliminar nave')
         print('4. Salir') #solicito la informacion al usuario
         opcion = int(input('escribe tu opcion (1-4): ')) #convierto la entrada a un tipo entero

         if opcion == 1:
             tipo_nave = input('Proporciona el tipo de la nave: ')
             combustible_nave = input('Que combustible usa?: ')
             medidas_nave = input('Cuanto mide la nave?: ')
             nave = Naves(tipo_nave, combustible_nave, medidas_nave)
             ne.agregar_nave(nave) #accedo a los metodos de naves espaciales

         elif opcion == 2: #metodo listar envia todo hacia la consola
             ne.listar_naves()

         elif opcion == 3: #mando a llamar el metodo eliminar naves
             ne.eliminar_naves()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None #valor inicial
else:
    print('salimos del programa')
