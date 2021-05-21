''' comentado el  ejemplo de Clase 1 sin constructor --------- 


class Coche():

#___________4 propiedades **
	#atributos del coche
	largoChais=250
	anchoChais=120
	ruedas=4
	enMarcha=False

	#Métodos es diferente a Función
	#Un método es una función especial que pertenece a la clase.
	#Una función es una función que no pertencene a ninguna clase

	# "self"  es el objeto perteneciente a la clase, lo que en otro lenguaje es conocido como "this"
	#Debe ser obligatorio ponerlo.
	#pass dentro de una función vacia es para que no nos de fallos si todavía no la vamos a crear.
#________*
#_________________2 comportamientos **
	def arrancar(self):
		self.enMarcha=True

	def estado(self):
		if(self.enMarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"
#___________________*




miCoche = Coche() #Instanciar una clase, no utilizar new como en Java

print("El largo del coche es: " , miCoche.largoChais) # con coma si viene de clase
print("El coche tiene ", miCoche.ruedas , "ruedas.")
#El recibe su mismo objeto, aquí pasamos a True
miCoche.arrancar() 
print(miCoche.estado())

print("------- A continuación creamos el segundo objetos")

miCoche2= Coche() #Instanciar una clase, no utilizar new como en Java

print("El largo del coche es: " , miCoche2.largoChais) # con coma si viene de clase
print("El coche tiene ", miCoche2.ruedas , "ruedas.")
#El recibe su mismo objeto, aquí pasamos a True
print(miCoche2.estado())

'''

#Ejemplo de clase con constructor


class Coche():

#___________4 propiedades **
	#Constructor predeterminado en Python

		def __init__(self):

			self.__largoChais=250
			self.__anchoChais=120
			self.__ruedas=4  # encapsulada para que no lo puedan modificar desde afuera.
			self.__enMarcha=False

	#Métodos es diferente a Función
	#Un método es una función especial que pertenece a la clase.
	#Una función es una función que no pertencene a ninguna clase

	# "self"  es el objeto perteneciente a la clase, lo que en otro lenguaje es conocido como "this"
	#Debe ser obligatorio ponerlo.
	#pass dentro de una función vacia es para que no nos de fallos si todavía no la vamos a crear.
#________*
#_________________2 comportamientos **
		def arrancar(self, arrancamos):
			self.__enMarcha=arrancamos
			
			if (self.__enMarcha):
				chequeo = self.__chequeoInterno()
			
			if(self.__enMarcha and chequeo):
				return "El coche está en marcha"
			elif(self.__enMarcha and chequeo==False):
				return "Algo ha salido mal en el chequeo, no podemos arrancar"
			else:
				return "El coche está parado"

		def estado(self):
			print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChais, "y un largo de ", self.__largoChais)
			

		#Encapsular método

		def __chequeoInterno(self):
			print("Realizando chequeo interno")

			self.gasolina="ok"
			self.aceite="ok"
			self.puertas="cerradas"

			if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
				return True
			else:
				return False
#___________________*




miCoche = Coche() #Instanciar una clase, no utilizar new como en Java

#El recibe su mismo objeto, aquí pasamos como atributo  True o False, ya que recibe un solo parámetro
print(miCoche.arrancar(True))

print("------- A continuación creamos el segundo objetos")

miCoche2= Coche() #Instanciar una clase, no utilizar new como en Java

#El recibe su mismo objeto, aquí pasamos a True
