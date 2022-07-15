import os #paquete operating system que contiene el metodo para eliminar un archivo del sistema op
class NavesEspaciales:
    #defino la variable de clase (estatica)
    ruta_naves = 'naves.txt'

    #defino el metodo de clase (puede acceder directamente a los atributos de clase
    @classmethod #defino el metodo agregar nave
    def agregar_nave(cls, naveEspacial):
        with open(cls.ruta_naves, 'a', encoding='utf8') as archivo: #especifico el nombre de la ruta y accedo al atributo de clase, luego pongo en modo append para anexar informacion
            archivo.write(f'{naveEspacial.tipo}\n{naveEspacial.combustible}\n{naveEspacial.medidas}\n') #mando a llamar el metodo write para escribir la informacion de la nave


    @classmethod #defino el metodo listar naves
    def listar_naves(cls):
        with open(cls.ruta_naves, 'r', encoding='utf8') as archivo:  #recibo el contexto de clase y abro el archivo, lo abro en modo lectura para listar
            print('Lista de naves'.center(50, '-')) #mando a imprimir la lista de naves y centro la lista
            print(archivo.read())


    @classmethod #defino el metodo eliminar nave
    def eliminar_naves(cls):
        os.remove(cls.ruta_naves)#con este metodo indico el nombre de la nave y la ruta para eliminarla
        print(f'nave eliminada: {cls.ruta_naves}') #imprimo el nombre de la nave






