from pathlib import Path
data_folder = Path("C:/Users/NelsonDavid/Desktop/ArriendiPython-alfa-master")

def GuardarArticulo(identificacion,nombre,precio):
	identificacion=str(identificacion)
	nombre=str(nombre)
	precio=str(precio)
	guardar=open("baseArticulo.csv","a")
	guardar.write(identificacion)
	guardar.write(",")
	guardar.write(nombre)
	guardar.write(",")
	guardar.write(precio)
	guardar.write("\n")
	guardar.close()

def GuardarUsuario(identificacion,nombre,_password):
	identificacion=str(identificacion)
	nombre=str(nombre)
	_password=str(_password)
	guardar=open("baseUsuario.csv","a")
	guardar.write(identificacion)
	guardar.write(",")
	guardar.write(nombre)
	guardar.write(",")
	guardar.write(_password)
	guardar.write("\n")
	guardar.close()